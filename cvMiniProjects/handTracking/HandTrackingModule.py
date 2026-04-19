import cv2
import time
import mediapipe as mp


class HandTracker:
    """
    This class handles everything related to hand detection:
    - initializing MediaPipe
    - capturing video
    - detecting hands
    - drawing landmarks
    """

    def __init__(self, model_path="hand_landmarker.task", cam_index=0, max_hands=2):
        """
        Constructor (runs when object is created)

        model_path → path to .task model file (brain of system)
        cam_index → which camera to use (0 = default webcam)
        max_hands → how many hands to detect
        """

        # Store user inputs
        self.model_path = model_path
        self.cam_index = cam_index
        self.max_hands = max_hands

        # -------- Setup MediaPipe (new API) --------
        self.mp = mp

        # These are required classes from MediaPipe Tasks API
        self.BaseOptions = self.mp.tasks.BaseOptions
        self.HandLandmarker = self.mp.tasks.vision.HandLandmarker
        self.HandLandmarkerOptions = self.mp.tasks.vision.HandLandmarkerOptions
        self.VisionRunningMode = self.mp.tasks.vision.RunningMode

        # Create configuration for hand detection
        self.options = self.HandLandmarkerOptions(
            base_options=self.BaseOptions(model_asset_path=self.model_path),
            running_mode=self.VisionRunningMode.VIDEO,  # video mode needs timestamp
            num_hands=self.max_hands
        )

        # -------- Initialize Camera --------
        self.cap = cv2.VideoCapture(self.cam_index)

        # Time variable for FPS calculation
        self.pTime = 0

    def run(self):
        """
        Main loop:
        - reads camera frames
        - detects hands
        - draws landmarks
        - shows FPS
        """

        # Create hand detector object using given options
        with self.HandLandmarker.create_from_options(self.options) as landmarker:

            while True:
                # Read frame from camera
                success, img = self.cap.read()

                # If camera fails, break loop
                if not success:
                    print("Camera not working!")
                    break

                # Convert image from BGR → RGB (MediaPipe needs RGB)
                imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                # Convert OpenCV image to MediaPipe image format
                mp_image = self.mp.Image(
                    image_format=self.mp.ImageFormat.SRGB,
                    data=imgRGB
                )

                # Generate timestamp (required for VIDEO mode)
                timestamp = int(time.time() * 1000)

                # Detect hands in current frame
                results = landmarker.detect_for_video(mp_image, timestamp)

                # -------- Draw Landmarks --------
                if results.hand_landmarks:
                    for handLms in results.hand_landmarks:

                        # Get image size
                        h, w, c = img.shape

                        # Loop through each landmark
                        for id, lm in enumerate(handLms):

                            # Convert normalized (0–1) → pixel coordinates
                            cx, cy = int(lm.x * w), int(lm.y * h)

                            # Print landmark info (for debugging/learning)
                            print(f"ID: {id}, X: {cx}, Y: {cy}")

                            # Draw small circle on each landmark
                            cv2.circle(img, (cx, cy), 5, (255, 0, 255), -1)

                            # Highlight wrist (landmark 0)
                            if id == 0:
                                cv2.circle(img, (cx, cy), 10, (0, 255, 0), -1)

                # -------- FPS Calculation --------
                cTime = time.time()
                fps = 1 / (cTime - self.pTime) if self.pTime != 0 else 0
                self.pTime = cTime

                # Display FPS on screen
                cv2.putText(img, f'FPS: {int(fps)}', (10, 70),
                            cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

                # Show final output window
                cv2.imshow("Hand Tracking", img)

                # Press 'q' to exit
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        # Release camera and close windows
        self.cap.release()
        cv2.destroyAllWindows()


# -------- Main Function (entry point) --------
def main():
    """
    This function runs when file is executed directly
    Here we can take input from user
    """

    print("Using MediaPipe from:", mp.__file__)
    print("Version:", mp.__version__)

    # -------- User Inputs --------
    cam_index = int(input("Enter camera index (0 or 1): "))
    model_path = input("Enter model path (default: hand_landmarker.task): ")

    # If user presses enter, use default
    if model_path.strip() == "":
        model_path = "hand_landmarker.task"

    # Create object of HandTracker class
    tracker = HandTracker(model_path=model_path, cam_index=cam_index)

    # Run the tracker
    tracker.run()


# -------- Run only if this file is executed --------
if __name__ == "__main__":
    main()
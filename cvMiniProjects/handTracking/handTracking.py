import cv2
import time
import mediapipe as mp

print(mp.__file__)
print(mp.__version__)

# -------- MediaPipe NEW API SETUP --------
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path="hand_landmarker.task"),
    running_mode=VisionRunningMode.VIDEO,
    num_hands=2
)

# -------- Camera --------
cap = cv2.VideoCapture(0)

pTime = 0

with HandLandmarker.create_from_options(options) as landmarker:
    while True:
        success, img = cap.read()
        if not success:
            break

        # Convert to RGB
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Convert to MediaPipe Image
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=imgRGB)

        # Timestamp required for VIDEO mode
        timestamp = int(time.time() * 1000)

        results = landmarker.detect_for_video(mp_image, timestamp)

        # -------- Draw Landmarks --------
        if results.hand_landmarks:
            for handLms in results.hand_landmarks:
                h, w, c = img.shape

                for id, lm in enumerate(handLms):
                    # print(id, lm) 
                    # Getting the pixel values via multiplying the normalized values with the dimensions of the image
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    print(id, cx, cy)
                    # Draw point
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), -1)

                    if id == 0:
                        cv2.circle(img, (cx, cy), 10, (0, 255, 0), -1)
                    
        # -------- FPS --------
        cTime = time.time()
        fps = 1 / (cTime - pTime) if pTime != 0 else 0
        pTime = cTime

        cv2.putText(img, f'FPS: {int(fps)}', (10, 70),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
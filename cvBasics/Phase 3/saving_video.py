import cv2

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')

recorded = cv2.VideoWriter('recorded_video.avi',codec,20,(frame_width,frame_height))

while True:
    success, frame = camera.read()
    if not success:
        print("Could not read frame from webcam. Exiting...")
        break
    recorded.write(frame)
    cv2.imshow('Recording Video', frame)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        print("Quiting.....")
        break
    
camera.release()
recorded.release()
cv2.destroyAllWindows()
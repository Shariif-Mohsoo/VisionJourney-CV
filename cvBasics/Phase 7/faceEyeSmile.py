import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml'
)

smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_smile.xml'
)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        # Region of Interest
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        cv2.imshow("Cropped Face", roi_color)

        # Detect eyes
        eyes = eye_cascade.detectMultiScale(roi_gray,1.1,10)

        if len(eyes) >= 2:
            cv2.putText(frame,'Eyes Detected',(x,y-10),
                        cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)

            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        # Detect smile
        smiles = smile_cascade.detectMultiScale(roi_gray,1.7,22)

        if len(smiles) > 0:
            cv2.putText(frame,'Smiling',(x,y-40),
                        cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,0,255),2)

            for (sx,sy,sw,sh) in smiles:
                cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)

    # Show frame OUTSIDE loop
    cv2.imshow("Face Detection with Eyes and Smile", frame)

    # Key check OUTSIDE loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
import cv2

# Load cascades
face_cascade = cv2.CascadeClassifier(r"FACE_detection/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r"FACE_detection/haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier(r"FACE_detection/haarcascade_smile.xml")

# Start camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera not detected.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Define regions of interest (ROI) correctly
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detect eyes in face ROI
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        if len(eyes) > 0:
            cv2.putText(frame, "Eyes Detected", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Detect smile in face ROI
        smile = smile_cascade.detectMultiScale(roi_gray, 1.7, 22)
        if len(smile) > 0:
            cv2.putText(frame, "Smiling", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

    cv2.imshow("Smart Face Detector", frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# import cv2

# # Load cascades
# face_cascade = cv2.CascadeClassifier(r"FACE_detection/haarcascade_frontalface_default.xml")
# eye_cascade = cv2.CascadeClassifier(r"FACE_detection/haarcascade_eye.xml")
# smile_cascade = cv2.CascadeClassifier(r"FACE_detection/haarcascade_smile.xml")

# # Start camera
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Camera not detected.")
#         break

#     # Flip the frame horizontally (mirror effect)
#     frame = cv2.flip(frame, 1)

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Detect faces
#     faces = face_cascade.detectMultiScale(gray, 1.1, 5)

#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

#         # Define regions of interest (ROI) correctly
#         roi_gray = gray[y:y + h, x:x + w]
#         roi_color = frame[y:y + h, x:x + w]

#         # Detect eyes in face ROI
#         eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
#         if len(eyes) > 0:
#             cv2.putText(frame, "Eyes Detected", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

#         # Detect smile in face ROI
#         smile = smile_cascade.detectMultiScale(roi_gray, 1.7,)
#         if len(smile) > 0:
#             cv2.putText(frame, "Smiling", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

#     cv2.imshow("Smart Face Detector", frame)

#     # Exit on 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()






import cv2
import time

# Load cascades
face_cascade = cv2.CascadeClassifier(r"FACE_detection/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r"FACE_detection/haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier(r"FACE_detection/haarcascade_smile.xml")

# Start camera
cap = cv2.VideoCapture(0)

# FPS calculation
prev_time = time.time()

def fancy_box(img, x, y, w, h, color=(0,255,0), thickness=2):
    """Draw a stylish rounded rectangle box."""
    cv2.rectangle(img, (x,y), (x+w, y+h), color, thickness)
    cv2.circle(img, (x, y), 10, color, -1)
    cv2.circle(img, (x+w, y), 10, color, -1)
    cv2.circle(img, (x, y+h), 10, color, -1)
    cv2.circle(img, (x+w, y+h), 10, color, -1)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera not detected.")
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate FPS
    curr_time = time.time()
    fps = int(1 / (curr_time - prev_time))
    prev_time = curr_time

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    detection_status = "No Face Detected"

    for (x, y, w, h) in faces:
        fancy_box(frame, x, y, w, h, (0, 255, 0), 2)
        detection_status = "Face Detected"

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Eyes detection
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        if len(eyes) > 0:
            detection_status = "Eyes Detected"
            cv2.putText(frame, "Eyes Found", (x, y - 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

        # Smile detection
        smile = smile_cascade.detectMultiScale(roi_gray, 1.7, 22)
        if len(smile) > 0:
            detection_status = "Smiling "
            cv2.putText(frame, "Smiling", (x, y - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2)

    # Status Bar
    cv2.rectangle(frame, (0,0), (frame.shape[1], 40), (30,30,30), -1)
    cv2.putText(frame, f"Status: {detection_status}", (10, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2)

    # Display FPS
    cv2.putText(frame, f"FPS: {fps}", (frame.shape[1]-100, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

    cv2.imshow("Smart Face Detector Pro", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

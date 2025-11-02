import cv2

cap=cv2.VideoCapture(0)#0 if want to use webcam
                       #1 if want to use usb cable

while True :
    ret ,frame=cap.read() #ret=True/False, frame=image
    
    if not ret :
        print("Could not read frame")
        break
    cv2.imshow("webcam feed",frame)

    if cv2.waitKey(1) & 0xFF==ord("q") :#if press q video will stop
        print("quitting..")
        break
cap.release()
cv2.destroyAllWindows
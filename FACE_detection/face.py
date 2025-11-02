import cv2

face_cascade=cv2.CascadeClassifier(r"FACE_detection/haarcascade_frontalface_default.xml")

cap=cv2.VideoCapture(0)

while True :
    ret,frame=cap.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.1,5)

    """
    detectMultiScale()-scan and detect faces
    1.1--scale factor balanced,not too slow nor fast
    mineNeghbors=5(safe cheaking)
    =3 loose cheaking
    =6 strict cheaking
    """
    for(x,y,w,h) in faces :
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    """
    (x,y)- top=left corner 

    (x+w.y+h)

    face=[
    (100,150,80,80) face1
    (250,120,90,90)] face2

    x - how far from left
    y - how far from right
    w - width of face
    h - height of face
    """

    cv2.imshow("webcam face detection",frame)

    if cv2.waitKey(1) &0xFF==ord("q") :
        break

cap.release()
cv2.destroyAllWindows()

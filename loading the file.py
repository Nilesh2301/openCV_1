import cv2

image=cv2.imread(r"c:\Users\Nilesh gupta\Downloads\ugc.webp")

if image is not None:
    cv2.imshow("image is showing",image)
    cv2.waitKey(0)  #to wait in the window
    cv2.destroy()    #to cut the window

else:
    print("image is Not founded")
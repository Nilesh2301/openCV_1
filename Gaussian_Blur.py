#cv2.GaussianBlur(image,(kernal_size_x),kernal_size_y,sigma)
#kernal_size always odd , sigma=opencv blur according to meself
import cv2
image=cv2.imread(r"c:\Users\Nilesh gupta\Pictures\Screenshots\Screenshot 2025-11-01 112548.png")

blured=cv2.GaussianBlur(image,(7,7),0)
cv2.imshow("originalimage",image)
cv2.imshow("blured image",blured)
cv2.waitKey(0)
cv2.destroyAllwindows()
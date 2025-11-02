#cv2.medianBlur(image,kernal_size)
import cv2
image=cv2.imread(r"c:\Users\Nilesh gupta\Downloads\images.jpeg")
blurred=cv2.medianBlur(image,5)
cv2.imshow("original",image)
cv2.imshow("clean image",blurred)
cv2.waitKey(0)
cv2.distroyAllwindows()
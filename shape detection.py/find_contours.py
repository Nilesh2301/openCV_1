"""
contours mean edge which conncets the image
binary image=black &white image
*contours,=heirarchy=cv2.findContours(image,mode,method)
"""
import cv2
img=cv2.imread(r"c:\Users\Nilesh gupta\Downloads\images.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(gray,240,255,cv2.THRESH_BINARY)

#FIND CONTOURS
contours,heirarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#FOR SHOWING
#cv2.drawContours(thresh,contours,contours_index,thickness)
#contour_index--kaunsa shape draw 
#*0 first,1 second,-1 all shape


cv2.drawContours(img,contours,-1,(0,255,0),3)
cv2.imshow("contours",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
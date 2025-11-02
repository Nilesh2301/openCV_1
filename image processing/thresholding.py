#cv2.threshold(image,thresh_value,max_value,method)
#work as conver to gray scale according to britness
#threshold1-0-255 and max will 255
import cv2

image=cv2.imread(r"c:\Users\Nilesh gupta\Downloads\download (4).png",cv2.IMREAD_GRAYSCALE)

ret,thresh_image=cv2.threshold(image,120,255,cv2.THRESH_BINARY)
cv2.imshow("original image",image)
cv2.imshow("THRESHOLD IMAGE",thresh_image)
cv2.waitKey(0)
cv2.destroyAllWindows


"""
90-0 black
130-255 white
180-255 white
50-0 black
100,120,150
for best
"""
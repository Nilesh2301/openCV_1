#cv2.Canny(image,threshold1,threshold2)
#to detect border,seperate objext,feature extraction
import cv2
image=cv2.imread(r"c:\Users\Nilesh gupta\Downloads\download (4).png",cv2.IMREAD_GRAYSCALE)

edges=cv2.Canny(image,50,150)
cv2.imshow("original image",image)
cv2.imshow("edge image",edges)
cv2.waitKey(0)
cv2.destroyAllWindows
#cv2.filter2D(source,ddepth,kernal(3x3 matrix))

import cv2
import numpy as np
image=cv2.imread(r"c:\Users\Nilesh gupta\Downloads\download (3).jpeg")
sharpen_kernal=np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]   
])
sharpend=cv2.filter2D(image,-1,sharpen_kernal)

cv2.imshow("original",image)
cv2.imshow("sharped image",sharpend)
cv2.waitKey(0)
cv2.destroyAllwinows()

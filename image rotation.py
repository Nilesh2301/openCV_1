import cv2
image=cv2.imread(r"resized_output.png")



if image is not None:
    w,h=image.shape[:2]
    center=(w//2,h//2)
    M=cv2.getRotationMatrix2D(center,90,1.0)  #cv2.getRotationMatrix(center,angle,scale)
    rotated_image=cv2.warpAffine(image,M,(w,h))  #cv2.warAffine(image,M,(width,height))
    cv2.imshow("original image",image)
    cv2.imshow("image rotated 90",rotated_image)
    cv2.waitKey(0)
    cv2.destroy()
    

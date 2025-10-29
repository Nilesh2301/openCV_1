import cv2

image=cv2.imread(r"c:\Users\Nilesh gupta\Downloads\ugc.webp")
if image is not None :
    grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("image is showing",grey)
    cv2.waitKey(0)  
    cv2.destroy()    

        

else:
    print("iamge is not found")     
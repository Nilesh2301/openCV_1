import cv2
image=cv2.imread(r"c:\Users\Nilesh gupta\Downloads\download (1).jpeg")
if image is None:
    print("opps! change by art your image  not working")
else:
    print("image loaded successfully!")
    h,w,c=image.shape
    print(f"image loaded \nHeight :{h}\nWidth :{w}\nChannel:{c}")
    cv2.circle(image,(100,100),100,(0,0,250),-1) #cv2.circle(image,centre,radius,color,thickness) if -1 mean fill the color

    cv2.imshow("circle showing",image)
    cv2.waitKey(0)

    cv2.destroyAllWindows


import cv2
image=cv2.imread(r"c:\Users\Nilesh gupta\Downloads\download (1).jpeg")
if image is None:
    print("opps! your image is not working")
else:
    print("image loaded successfully!")
    h,w,c=image.shape
    print(f"image loaded \nHeight :{h}\nWidth :{w}\nChannel:{c}")
    pt1=(50,100)
    pt2=(250,100)
    color=(255,0,0)
    thickness=10
    cv2.line(image,pt1,pt2,color)
    cv2.imshow("line showing",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows

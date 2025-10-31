import cv2
image=cv2.imread(r"c:\Users\Nilesh gupta\Downloads\download (1).jpeg")
if image is None:
    print("opps! your image is not working")
else:
    h,w,c=image.shape
    print(f"image loaded\nHeight:{h}\nWidth:{w}")
    pt1=(50,50)
    pt2=(180,80)
    color=(0,0,255)
    thickness=3
    cv2.rectangle(image,pt1,pt2,color,thickness)
    cv2.imshow("image focusing rectangle",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows


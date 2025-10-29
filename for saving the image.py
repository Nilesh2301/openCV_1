import cv2

image=cv2.imread(r"c:\Users\Nilesh gupta\Downloads\ugc.webp")
if image is not None :
    succes=cv2.imwrite("image is saving as 'image.png'",image)
    if succes:
        print("image  saved succesfully")
    else:
        print("try again later")

else:
    print("iamge is not found")     
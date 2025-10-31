#cv2.putText(image,text,org,font,fontscale,color,thickness)
#org-(x,y),font-font type,fontscale=size,
import cv2
image=cv2.imread(r"c:\Users\Nilesh gupta\Downloads\download (1).jpeg")
if image is None:
    print("opps! your image is not working")
else:
    print("image loaded successfully!")
    cv2.putText(image,"HELLO PYTHON",(40,50),
               cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255), 2)

    cv2.imshow("adding text over here",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows
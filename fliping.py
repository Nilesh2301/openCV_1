import cv2
image=cv2.imread(r"c:\Users\Nilesh gupta\Pictures\Screenshots\Screenshot 2025-10-20 132105.png")
if image is not None :
    flipped_verticle=cv2.flip(image,0)  #cv2.flip(image,fliped code) if fc=0(flip top to bottom)
    flipped_horizontal=cv2.flip(image,1)    #if fc=1(flip left to right),if -1 (both) 
    flipped_both=cv2.flip(image,-1)                     
    cv2.imshow("image shown both",flipped_both)
    cv2.imshow("image shown verticle",flipped_verticle)
    cv2.imshow("image shown horizontal",flipped_horizontal)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
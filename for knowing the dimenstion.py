import cv2
image=cv2.imread(r"c:\Users\Nilesh gupta\Pictures\Screenshots\Screenshot 2025-10-20 132105.png")
if image is not None :
    h,w,c=image.shape
    print(f"image Loaded:\nHeight: {h}\nwidth: {w}\nChannels: {c}")
else:
    print("could not load image")

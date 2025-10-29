import cv2
image=cv2.imread(r"c:\Users\Nilesh gupta\Downloads\periodic-table-elements-atomic-number-name-symbol-properties.png")

if image is  None :
  print("image not found")

else:
  print("image loaded")
  resized=cv2.resize(image,(1000,500))#(width,height)

  cv2.imshow("original image",image)
  cv2.imshow("resized image",resized)

  cv2.imwrite("resized_output.png",resized)

  cv2.waitKey(0)
  cv2.destroy()
import cv2
image=cv2.imread(r"c:\Users\Nilesh gupta\Downloads\periodic-table-elements-atomic-number-name-symbol-properties.png")

if image is not None :
  croped=image[100:200 ,50:150]
  cv2.imshow("priginal image",image)
  cv2.imshow("croped image",croped)
  cv2.waitKey()
  cv2.destroy()
##Resizing
import cv2

img=cv2.imread("Resources/earth.jpg")
print(img.shape)


imgResize=cv2.resize(img,(623,462)) # width first then height
print(imgResize.shape)

cv2.imshow("image",img)
cv2.imshow("image Resize",imgResize)


##Cropping

imgCropped= imgResize[0:200,200:500] # height first then width
cv2.imshow("image Cropped",imgCropped)

cv2.waitKey(0)
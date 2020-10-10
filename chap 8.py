import cv2
import  numpy as np

def getContours(img):
   contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
   for cnt in contours:
       area= cv2.contourArea(cnt)
       print(area)
       cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)


path='Resources/shapes.jpg'
img=cv2.imread(path)
imgContour=img.copy()

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny=cv2.Canny(imgBlur,50,50)
getContours(imgCanny)

imgBlank=np.zeros_like(img)



cv2.imshow("Original",img)
cv2.imshow("Gray",imgGray)
cv2.imshow("Blur",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Blank",imgBlank)
cv2.imshow("Contours",imgContour)
update ()
cv2.waitKey(0)

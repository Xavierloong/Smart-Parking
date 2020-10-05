#Warp Prespective
import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

width,height = 250,350
# pts1 = np.float32([[123,107],[214,68],[181,237],[268,198]]) #Card K
# pts1 = np.float32([[40,230],[145,221],[53,366],[155,361]]) #Card Q
pts1 = np.float32([[213,326],[307,338],[193,460],[290,475]]) #Card A
pts2= np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("image",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)

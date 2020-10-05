import cv2
##Read image
img = cv2.imread("Resources/lady.jpg")

cv2.imshow("Output",img)
cv2.waitKey(0)


##Read Video
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success,img = cap.read()
    cv2.imshow("nature",img)
    if cv2.waitKey(1)& 0xFF ==  ord('q'):
        break



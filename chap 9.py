import cv2

#C:\Users\Xavier Loong\anaconda3\pkgs\libopencv-3.4.2-h20b85fd_0\Library\etc\haarcascades
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
img = cv2.imread('Resources/lady.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces= faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


cv2.imshow("Result",img)
cv2.waitKey(0)
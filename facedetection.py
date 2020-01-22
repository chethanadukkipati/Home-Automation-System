import cv2
face_cascade=cv2.CascadeClassifier('/home/pi/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
test=cv2.imread('/home/pi/trainingdata/person1/2.jpg')
gray_img=cv2.cvtColor(test,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray_img,1.1,10)
print('Faces Found:',len(faces))
cv2.imshow('Testimage',gray_img)
cv2.waitKey(0)
cv2.destroyWindow('Testimage')



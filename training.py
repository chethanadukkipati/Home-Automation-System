import cv2
import os
import numpy as np
def function20():
    subjects= ["","chethana","Sampreeth","Dinesh"]
    from subprocess import call
    call(["fswebcam","/home/pi/test.jpg"])
    def detect_face(img):
        gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        face_cascade=cv2.CascadeClassifier('/home/pi/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_default.xml')
        faces=face_cascade.detectMultiScale(gray_img,1.1,10)
        if(len(faces)==0):
            return None,None
        (x,y,w,h)=faces[0]
        return gray_img[y:y+w,x:x+h],faces[0]
    def training_data(datafolderpath):
        faces=[]
        labels=[]
        dirs=os.listdir(datafolderpath)
        for dir_name in dirs:
            if not dir_name.startswith("person"):
                continue;
            label=int(dir_name.replace("person",""))
            subject_dir_path=datafolderpath+ "/" + dir_name
            subject_images_names=os.listdir(subject_dir_path)
            for image_name in subject_images_names:
                if image_name.startswith("."):
                   continue;
                image_path=subject_dir_path + "/" +image_name
                image=cv2.imread(image_path)
                cv2.imshow("Training on image....",image)
                cv2.waitKey(100)
                face,rect=detect_face(image)
                if face is not None:
                    faces.append(face)
                    labels.append(label)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        return faces,labels
    faces,labels=training_data("/home/pi/trainingdata/")
    face_recognizer=cv2.face.createLBPHFaceRecognizer()
    face_recognizer.train(faces,np.array(labels))
    def predict(test_img):
        img=test_img.copy()
        face,rect=detect_face(img)
        label,confidence=face_recognizer.predict(face)
        label_text=subjects[label]
        return img,confidence,label
    test_img1=cv2.imread("/home/pi/trainingdata/person1/1.jpg")
    predicted_img1,val,value=predict(test_img1)
    if(val<60):
       #cv2.imshow(subjects[value],cv2.resize(predicted_img1,(400,500)))
       #cv2.waitKey(0)
       #cv2.destroyAllWindows()
       return "Identity Matched",subjects[value]
    else:
       #cv2.imshow("Not authorized person",cv2.resize(predicted_img1,(400,500)))
    #cv2.waitKey(0)
       #cv2.destroyAllWindows()
        return "No face matches detected",subjects[value]
 


import cv2
face=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye=cv2.CascadeClassifier("haarcascade_eye.xml")
cap=cv2.VideoCapture(0)
while 1:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    f1=face.detectMultiScale(img,1.3,1)
    f2=eye.detectMultiScale(img,1.3,1)

    for (x,y,w,h) in f1:
        cv2.rectangle(img,(x,y),(x+w,y+h),(100,155,255),3)
        f2=gray[y:y+h,x:x+w]
        f3=img[y:y+h,x:x+w]
        x=eye.detectMultiScale(f2,1.3,1)
        for (x1,y1,w1,h1) in x:
           cv2.rectangle(f3,(x1,y1),(x1+w1,y1+h1),(100,155,255),3)
           
           
    cv2.imshow("face",img)
    z=cv2.waitKey(1)
    if z==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

        

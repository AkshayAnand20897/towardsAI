import cv2
cap=cv2.VideoCapture(0)
while 1:
    ret,frame=cap.read()
    a=cv2.flip(frame,1)
    
    cv2.imshow("Title",a)
    if cv2.waitKey(1)&0XFF==ord('q'):
      break
cam = cv2.VideoCapture(1)
s, im = cam.read() # captures image
x=cv2.imwrite("test.jpg",im) # writes image test.bmp to disk
cv2.imshow("Test Picture", x) # displays captured image

cap.release()
cv2.destroyAllWindows()

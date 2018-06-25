import cv2
cap=cv2.VideoCapture(0)
while 1:
    ret,frame=cap.read()
    cv2.imshow("Title",frame)
    if cv2.waitKey(1)&0XFF==ord('q'):
      break
cam = cv2.VideoCapture(1)
cap.release()
cv2.destroyAllWindows()

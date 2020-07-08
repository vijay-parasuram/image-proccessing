import cv2
print('1')

import time
cap = cv2.VideoCapture(0)   #cam related
fourcc = cv2.VideoWriter_fourcc(*'XVID')    #rec related
out =cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))    #rec related
while(cap.isOpened()):  #.isOpened used to not run when .videocapture argument is wrong
    ret, frame = cap.read() #cam related
    if ret==True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    #cam related
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))   #cam related
        out.write(frame)    #rec related
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #cam related
        cv2.imshow('frame', gray)   #cam related
        if cv2.waitKey(1) & 0xFF == ord('q') :  #to close video
            break
    else:
        break
cap.release()   #cam related
cv2.destroyAllWindows()
time.sleep(1)
import cv2
import numpy as np
def click_event(event,x,y,flags,param) :
    if event == cv2.EVENT_LBUTTONDOWN :
        print(x,',',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strxy = str(x)+', '+str(y)
        cv2.putText(img,strxy,(x,y),font,1,(255,255,0),2)
        cv2.imshow('image',img)
img=np.zeros((512,512,3),np.uint8)
cv2.imshow('image',img)
print('1')
cv2.setMouseCallback('image',click_event)
print('2')
cv2.waitKey()
print('3')
cv2.destroyAllWindows()
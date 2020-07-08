# in this code we will draw line on image
import cv2
img = cv2.imread('smarties.png',1)
import numpy
#img = numpy.zeros([512,512,3],numpy.uint8)  # black image
hfm=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


img=cv2.line(img,(0,0),(255,255),(36, 102, 136),3)
img=cv2.arrowedLine(img,(0,255),(255,255),(36, 102, 136),3)
img=cv2.rectangle(img,(125,125),(250,250),(36, 102,0),-1)
img=cv2.circle(img,(447,63),63,(0,255,0),-1)
font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,'opencv',(10,500),font,4,(255,255,255),10,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
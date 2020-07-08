import cv2
import numpy as npS
def nothing (x) :
    pass
cv2.namedWindow("Tracking")
cv2.createTrackbar("TH","Tracking",0,255,nothing)
cv2.waitKey(1000)
cv2.destroyAllWindows()
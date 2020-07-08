import cv2
import numpy as npS
def nothing(x) :
    pass

cv2.namedWindow("Tracking")
cv2.createTrackbar("TH","Tracking",0,255,nothing)
while True :
    img=cv2.imread('sudoku.png',0)
    t_h = cv2.getTrackbarPos("TH", "Tracking")
    _,th1 =cv2.threshold(img,t_h,255,cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imshow("image", img)
    cv2.imshow("th1", th1)
    cv2.imshow("th2", th2)
    cv2.imshow("th3", th3)
    key=cv2.waitKey(1)
    if key ==27 :
        break
cv2.destroyAllWindows()

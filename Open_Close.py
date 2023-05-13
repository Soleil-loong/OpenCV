import cv2
import numpy as np
img = cv2.imread('dige.png')
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#腐蚀操作
#腐蚀操作的前提一般要求图片是二值的,如黑白
kernel = np.ones((3,3),np.uint8) #3x3大小范围去腐蚀
erosion = cv2.erode(img,kernel,iterations = 1)      #腐蚀操作

cv2.imshow('erosion', erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()


#膨胀4次
kernel = np.ones((3,3),np.uint8)
dige_dilate1 = cv2.dilate(img,kernel,iterations = 1)
dige_dilate2 = cv2.dilate(dige_dilate1,kernel,iterations = 1)
dige_dilate3 = cv2.dilate(dige_dilate2,kernel,iterations = 1)
dige_dilate4 = cv2.dilate(dige_dilate3,kernel,iterations = 1)

cv2.imshow('dilate', dige_dilate4)
cv2.waitKey(0)
cv2.destroyAllWindows()

#开运算则是先腐蚀，再膨胀
#闭运算与开运算相反



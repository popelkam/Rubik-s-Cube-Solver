import cv2
import numpy as np

img = cv2.imread('mixedRubik.jpg')

#ORANGE
lower = np.array([5, 100, 100],np.uint8)
upper = np.array([15, 255, 255],np.uint8)

#BLUE
#lower = np.array([85,85,100],np.uint8)
#upper = np.array([125,255,255],np.uint8)

#RED - through research has two lower and upper ranges
#lower = np.array([0,100,100],np.uint8)
#upper = np.array([10,255,255],np.uint8)

#GREEN
#lower = np.array([35,75,100],np.uint8)
#upper = np.array([100,255,190],np.uint8)

#YELLOW
#lower = np.array([20,100,100],np.uint8)
#upper = np.array([50,255,255],np.uint8)

#WHITE
#lower = np.array([0,0,0],np.uint8)
#upper = np.array([1,1,225],np.uint8)

hsvImg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

colorThreshold = cv2.inRange(hsvImg, lower, upper)
colorImg = cv2.bitwise_and(img,img,mask=colorThreshold)

cv2.imshow('threshold', colorThreshold)
cv2.imshow('colorOutput', colorImg)

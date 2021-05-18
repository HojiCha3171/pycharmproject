import cv2
import numpy as np

img = cv2.imread("C:\\Users\\tuzuk\\Desktop\\hand.JPG")

gray = cv2.cvtColor(img,cv2.COLOR_RGBA2GRAY)
   
ret,thresh = cv2.threshold(gray,127,255,0)
imgEdge,contours,hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv2.moments(cnt)
print(M)
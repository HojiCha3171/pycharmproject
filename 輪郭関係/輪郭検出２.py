import cv2
import numpy as np

img = cv2.imread("C:\\Users\\tuzuk\\Desktop\\test.JPG")

if len(img.shape) == 3:
     height, width, channels = img.shape[:3]
else:
     height, width = img.shape[:2]
     channels = 1
     #グレースケール化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)

ret,thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)    

cnts = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

cnt = cnts[1][0]

#print(cnt[0])

cnt = cnts[1][0]



'''
result = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)

cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\point.JPG",result)

'''
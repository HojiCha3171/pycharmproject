import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("C:\\Users\\tuzuk\\Desktop\\hand.JPG")
    
gray = cv2.cvtColor(img,cv2.COLOR_RGBA2GRAY)
    
ret, th2 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)    

contours =  cv2.findContours(th2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]

area = cv2.contourArea(cnt)
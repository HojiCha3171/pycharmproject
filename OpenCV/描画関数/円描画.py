import numpy as np
import cv2

img = cv2.imread("C:\\Users\\tuzuk\\Desktop\\test.JPG")

img = cv2.circle(img, (2185,872), 15, (0,0,255), -1)
img = cv2.circle(img, (2302, 880), 15, (0,0,255), -1)
img = cv2.circle(img, (2172, 922), 15, (0,0,255), -1)
img = cv2.circle(img, (2289, 929), 15, (0,0,255), -1)
img = cv2.circle(img, (2138, 1019), 15, (0,0,255), -1)
img = cv2.circle(img, (2332, 1181), 15, (0,0,255), -1)
img = cv2.circle(img, (2008, 1361), 15, (0,0,255), -1)
img = cv2.circle(img, (2579, 1397), 15, (0,0,255), -1)
img = cv2.circle(img, (1914, 1606), 15, (0,0,255), -1)
img = cv2.circle(img, (2676, 1653), 15, (0,0,255), -1)
img = cv2.circle(img, (1945, 1908), 15, (0,0,255), -1)
img = cv2.circle(img, (2555, 1945), 15, (0,0,255), -1)
img = cv2.circle(img, (2419, 2287), 15, (0,0,255), -1)
img = cv2.circle(img, (2387, 2685), 15, (0,0,255), -1)



cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\test820.JPG", img)

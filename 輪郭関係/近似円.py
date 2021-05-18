import cv2

import numpy as np


img = cv2.imread("C:\\Users\\tuzuk\\Desktop\\CIMG4557.JPG")


gau=cv2.GaussianBlur(img,(21,21),0)


gray = cv2.cvtColor(gau, cv2.COLOR_BGR2GRAY)   


ret, th = cv2.threshold(gray,130,255,cv2.THRESH_BINARY)
cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\CIMG45571.JPG",th)

src = np.array(th, dtype = "float32")


cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\volto_out2.png", src)


if len(src.shape) == 3:
     height, width, channels = src.shape[:3]

else:
     height, width = src.shape[:2]


     channels = 1

     
     print("dtype(src) " + str(src.dtype))



image, contours, hierarchy =  cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


cnt = contours[0]


print("dtype(cnt): " + str(cnt.dtype))


cnt_ = np.array(cnt, dtype = "float32")


print("dtype(cnt_): " + str(cnt_.dtype))


(x,y), radius = cv2.minEnclosingCircle(cnt)

center = (int(x),int(y))

radius = int(radius)

print(center)


img = cv2.circle(img,center,radius,(0,0,255),2)
cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\CIMG4557.JPG",img)

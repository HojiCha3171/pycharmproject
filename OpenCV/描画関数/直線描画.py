import cv2

img = cv2.imread("C:\\Users\\tuzuk\\Desktop\\tmp1.JPG")

img = cv2.line(img,(0, 1651),(3999, 2252),(255,0,0),15)

img = cv2.line(img,(2133, 2079),(2550, 0),(0,255,0),15)


cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\tmp1.JPG",img)
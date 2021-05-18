import cv2

img = cv2.imread("C:\\Users\\tuzuk\\Desktop\\tmp_th2_output.jpg")

resized = cv2.resize(img,(4000,3000))

cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\tmp_th2_output.jpg",resized)




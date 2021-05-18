import cv2

img = cv2.imread("C:\\Users\\tuzuk\\Desktop\\CIMG5288.JPG")

cv2.rectangle(img, (0, 10), (width, height), color=(0, 0, 0), thickness=-1)

cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\CIMG88.JPG", img)


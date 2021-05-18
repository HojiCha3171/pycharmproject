import cv2
import numpy as np

img = cv2.imread("C:\\Users\\tuzuk\\Desktop\\CIMG5343.JPG")


# BGR空間から HSV空間に変換
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

print('img',img[100,60])
print('hsv',hsv[100,60])

# BGR空間で緑色の範囲を定義
BGR_lower_back = np.array([30,70,30])
BGR_upper_back = np.array([80,120,80])

# BGR空間で緑色の範囲を定義
HSV_lower_back = np.array([40,70,40])
HSV_upper_back = np.array([100,120,100])



# HSV イメージから青い物体だけを取り出すための閾値
mask1 = cv2.inRange(img, BGR_lower_back, BGR_upper_back)
mask2 = cv2.inRange(img, HSV_lower_back, HSV_upper_back)


cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\1.JPG",img)
cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\2.JPG",mask1)
cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\3.JPG",mask2)


tmp = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,alpha = cv2.threshold(tmp,127,255,cv2.THRESH_BINARY)
b, g, r = cv2.split(img)
rgba = [b,g,r, alpha]
dst = cv2.merge(rgba,4)
cv2.imwrite("uuuuuu.png",_ )
cv2.imwrite("uuu.png", dst)
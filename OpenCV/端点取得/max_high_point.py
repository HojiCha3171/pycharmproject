import cv2
import numpy as np
from matplotlib import pyplot as plt
'''

# 入力画像を読み込み
img = cv2.imread("C:\\Users\\tuzuk\\Desktop\\point.JPG")
    
# グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

ret, th2 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)    

# 方法1(NumPyでヒストグラムの算出)
hist, bins = np.histogram(th2.ravel(),256,[0,256])


# ヒストグラムの中身表示
print(hist)

cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\point.JPG",th2)

# グラフの作成
plt.xlim(0, 255)
plt.plot(hist)
plt.xlabel("Pixel value", fontsize=20)
plt.ylabel("Number of pixels", fontsize=20)
plt.grid()
plt.show()
'''

img = cv2.imread("C:\\Users\\tuzuk\\Desktop\\point.JPG")

gray = cv2.cvtColor(img,cv2.COLOR_RGBA2GRAY)
    
ret, th2 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)    

print(img.shape)

x = th2.shape[0]
y = th2.shape[1]

for h in range(y):
    for w in range(x):
       value = img[w,h]
       
if  value == [0,0,0]:
        
print(max(list))
       

    
    
    

























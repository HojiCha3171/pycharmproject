import cv2 

im = cv2.imread("C:\\Users\\tuzuk\\Desktop\\IMG_2875.JPG")

    #新しい配列に入力画像の一部を代入
dst = im[300:3000,200:2700]

    #書き出し
cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\IMG_28275.JPG",dst)
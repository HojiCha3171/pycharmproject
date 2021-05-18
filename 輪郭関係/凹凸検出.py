import cv2
import numpy as np
import imutils
#created by 佐伯　晃

#内包面積が最も大きい輪郭を探す
def getLargestContoursAreaIndex(coutours):
    largestIndex = -1
    largestArea = 0
    
    for i in range(0, len(contours)):
        if largestArea < cv2.contourArea(contours[i]):
            largestArea = cv2.contourArea(contours[i])
            largestIndex = i

    return largestIndex

image = cv2.imread("C:\\Users\\tuzuk\\Desktop\\998.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (15, 15), 0)
#色認識
ret,thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)    

cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\range_2019-12-21.JPG", thresh)

#gray_image = cv2.cvtColor(img, cv.COLOR_BGR2GRAY)
#ret, threshold_image = cv2.threshold(img, 127, 255, cv.THRESH_BINARY)

contours_image, contours, hierarchy =  cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

print(contours)

print(getLargestContoursAreaIndex(contours))


#輪郭座標（配列）
cnt = contours[getLargestContoursAreaIndex(contours)]

hull = cv2.convexHull(cnt,returnPoints = False)

defects = cv2.convexityDefects(cnt,hull)

#print(defects)

print('defects',defects.shape[0])


far_list = []

for i in range(defects.shape[0]):
    
    if i > 0:
        f = defects[i-1,0]
        ff = f
    
        s,e,f,d = defects[i,0]
    
    
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far_e = tuple(cnt[f][0])
        far_s = tuple(cnt[ff][0])
    
    
        cv2.circle(image,far_s,8,[255,0,0],-1)
        cv2.line(image,start,end,[0,255,0],5)
        cv2.line(image,far_s,far_e,[0,255,0],5)
    
    '''
    print("start",start)
    print("end",end)
    print("far",far_s)
    '''
    #far_list.append(far)


#print('far_list',len(far_list))








    #cv2.line(image,start,end,[0,255,0],2)

    
cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\350.JPG", image)

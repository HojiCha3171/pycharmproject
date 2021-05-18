import cv2 

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

image = cv2.imread("C:\\Users\\tuzuk\\Desktop\\CIMG5608.JPG")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (15, 15), 0)
#色認識
ret,thresh = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY)    

cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\range_2019-07-02.JPG", thresh)

#gray_image = cv2.cvtColor(img, cv.COLOR_BGR2GRAY)
#ret, threshold_image = cv2.threshold(img, 127, 255, cv.THRESH_BINARY)

contours_image, contours, hierarchy =  cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

print(contours)

print(getLargestContoursAreaIndex(contours))

cnt = contours[getLargestContoursAreaIndex(contours)]

#print([cnt])

output_image = cv2.drawContours(image, [cnt], 0, (0, 0, 255), 20)

for i in range(0, len(contours)):
    output_all_image = cv2.drawContours(image, contours, i, (255, 0, 0), 10)

output_all_image = cv2.drawContours(output_all_image, [cnt], 0, (0, 0, 255), 20)

cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\range_2019-07-02.JPG", thresh)
#cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\threshold_2019-07-02.JPG", threshold_image)
cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\contours_2019-07-02.JPG", output_image)
cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\contours_all_2019-07-02.JPG", output_all_image)

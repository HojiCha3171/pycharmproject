import numpy as np
import cv2

#動画を取得
#端末に接続されたデバイスでストリームしたければ0などのデバイス割り当て番号
#既にある動画を使いたければ動画のパスを引数に与える
video = cv2.VideoCapture('C:\\Users\\tuzuk\\Desktop\\CIMG5408.MOV')

# VideoCaptureに失敗したら無視してプログラムを終了
while video.isOpened():

    # フレームの読み込み
    ret, frame = video.read()

    # フレームを読めなかった(動画を最後まで読み切った)ら終了
    if not ret:
        break

    # 画面サイズを取得
    # フローには書いてないけど大抵使うので書いておきます
    (height, width) = frame.shape[:2]

  
    #内包面積が最も大きい輪郭を探す
def getLargestContoursAreaIndex(coutours):
    largestIndex = -1
    largestArea = 0
    
    for i in range(0, len(contours)):
        if largestArea < cv2.contourArea(contours[i]):
            largestArea = cv2.contourArea(contours[i])
            largestIndex = i

    return largestIndex

image = frame

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (15, 15), 0)
#色認識
ret,thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)    

cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\range_2019-07-02.JPG", thresh)

#gray_image = cv2.cvtColor(img, cv.COLOR_BGR2GRAY)
#ret, threshold_image = cv2.threshold(img, 127, 255, cv.THRESH_BINARY)

contours_image, contours, hierarchy =  cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


#print(contours)


#print(getLargestContoursAreaIndex(contours))


#輪郭座標（配列）
cnt = contours[getLargestContoursAreaIndex(contours)]

#print([cnt])

output_image = cv2.drawContours(image, [cnt], 0, (0, 0, 255), 10)

for i in range(0, len(contours)):
    output_all_image = cv2.drawContours(image, contours, i, (255, 0, 0), 10)

output_all_image = cv2.drawContours(output_all_image, [cnt], 0, (0, 0, 255), 10)

cnts =  cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cnts = imutils.grab_contours(cnts)
c = max(cnts, key=cv2.contourArea)

extBot = tuple(c[c[:, :, 1].argmax()][0])
extLeft = tuple(c[c[:, :, 0].argmin()][0])


hull = cv2.convexHull(cnt,returnPoints = False)

defects = cv2.convexityDefects(cnt,hull)

#print(defects)

print('defects',defects.shape[0])


i = 0
root_list = []

while i <= defects.shape[0]-1:
    
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    
    '''
    print("start",start)
    print("end",end)
    print("far",far)
    '''
    print(i)

    #cv2.line(image,start,end,[0,255,0],2)
    cv2.circle(image,far,15,[255,0,0],-1)
    
    if far[0] <= extBot[0]+80 and extBot[1]-80 <= far[1] :
        
        i = i + 1
        continue

    elif far[0] <= extLeft[0]+50 and extLeft[1]-80 <= far[1] :
        
        i = i + 1
        continue
    
    elif far[1] <= extBot[1] and extLeft[1] <= far[1] :
        root_list.append(far)
        
        i = i + 1
        continue

    i = i + 1
    
if len(root_list) == 1:
    pointB = (root_list[0][0],root_list[0][1])

elif len(root_list) >= 1:
    
    i = 0
    pointB_x = 0
    pointB_y = 0
    while i <=len(root_list)-1:
        pointB_x = root_list[i][0]+pointB_x
        pointB_y = root_list[i][0]+pointB_x
        
        i = i+1
        
        print('pointB_x',pointB_x)
        print('pointB_y',pointB_y)
        
        
#pointB = (int((root_list[0][0]+root_list[1][0])/2),int((root_list[0][1]+root_list[1][1])/2))
pointB = (int(pointB_x/len(root_list)),int(pointB_y/len(root_list)))

print('root_list',root_list)
print('extBot',extBot,'extLeft',extLeft)

print('pointB',pointB)
print('pointA',extBot)

cv2.circle(image,pointB,25,[255,0,0],-1)
cv2.circle(image,extBot,25,[0,0,255],-1)


    # 現在読んでいるフレームを描画
    # 処理結果見えなくていいから軽量化したい場合はここをコメントアウト
cv2.imshow("frame", frame)


# メモリ開放
video.release()
cv2.destroyAllWindows()
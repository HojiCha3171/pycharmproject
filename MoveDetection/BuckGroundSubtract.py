import cv2
import numpy as np
import subprocess

cap = cv2.VideoCapture(0)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.createBackgroundSubtractorMOG2()

# 取得した中で最大の輪郭を取得
Area = []
largestIndex = 0
frame_number = 0

while(True):

    frame_number = frame_number + 1

    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)



    # ぼかし処理
    #gauss = cv2.GaussianBlur(fgmask, (15, 15), 0)

    # 全体の画素数
    whole_area = fgmask.size
    # 白部分の画素数
    white_area = cv2.countNonZero(fgmask)
    # 黒部分の画素数
    black_area = whole_area - white_area

    #if white_area/whole_area*100 > 10 and white_area/whole_area*100 < 20:
        #frame = cv2.circle(frame,(50,50),30,(200,0,0),thickness=-1)

    if white_area/whole_area*100 > 10 and frame_number > 30:
        frame = cv2.circle(frame,(50,50),30,(0,0,200),thickness=-1)
        subprocess.Popen(["C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"])
        break

    cv2.imshow('frame', frame)
    #print(frame_number)


    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

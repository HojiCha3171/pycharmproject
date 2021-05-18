import cv2
import numpy as np
import openpyxl as px

cap = cv2.VideoCapture("C:\\Users\\tuzuk\\Desktop\\test.mp4")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('test,avi', fourcc, 20.0, (640, 480))

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
fgbg = cv2.createBackgroundSubtractorMOG2()

frame_number = 0

while (cap.isOpened()):
    ret, frame = cap.read()

    frame_number = frame_number + 1

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    fgmask = fgbg.apply(gray)

    blur = cv2.GaussianBlur(fgmask, (15, 15), 0)

    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, dp=1.3, minDist=20, param1=100, param2=60, minRadius=0,
                               maxRadius=0)
    if circles != None:
        print(circles)

    """
    if circles == None or ex:
        circles = np.uint16(np.around(circles))

        for circle in circles[0, :]:
            # 円周を描画する
            cv2.circle(frame, (circle[0], circle[1]), circle[2], (0, 165, 255), 5)
            # 中心点を描画する
            cv2.circle(frame, (circle[0], circle[1]), 2, (0, 0, 255), 3)


        cv2.imshow('frame', blur)
    """
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
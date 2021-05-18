import cv2
import numpy as np
import openpyxl as px

cap = cv2.VideoCapture("C:\\Users\\tuzuk\\Desktop\\test.mp4")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("C:\\Users\\tuzuk\\Desktop\\test1.mp4",fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=100, param2=60, minRadius=0,
                               maxRadius=0)

    print(circles)

    circles = np.uint16(np.around(circles))

    for circle in circles[0, :]:
        # 円周を描画する
        cv2.circle(frame, (circle[0], circle[1]), circle[2], (0, 165, 255), 5)
        # 中心点を描画する
        cv2.circle(frame, (circle[0], circle[1]), 2, (0, 0, 255), 3)

    out.write(frame)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
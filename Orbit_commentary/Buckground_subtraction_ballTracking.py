import cv2
import numpy as np
import openpyxl as px

cap = cv2.VideoCapture("C:\\Users\\tuzuk\\Desktop\\test.mp4")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('test,avi',fourcc, 20.0, (640,480))

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
fgbg = cv2.createBackgroundSubtractorMOG2()

frame_number = 0


while(cap.isOpened()):
    ret, frame = cap.read()

    frame_number = frame_number + 1

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    fgmask = fgbg.apply(gray)

    blur = cv2.GaussianBlur(fgmask,(15,15),0)

    ret, thresh = cv2.threshold(blur, 127, 255, 0)
    imgEdge, contours, hierarchy = cv2.findContours(thresh, 1, 2)

    cnt = contours[0]

    (x, y), radius = cv2.minEnclosingCircle(cnt)
    center = (int(x), int(y))
    radius = int(radius)
    frame = cv2.circle(frame, center, radius, (0, 255, 0), 2)

    
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
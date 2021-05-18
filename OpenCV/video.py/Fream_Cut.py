import numpy as np
import cv2

cap = cv2.VideoCapture("C:\\Users\\tuzuk\\Desktop\\CIMG5572.MOV")
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
writer = cv2.VideoWriter("C:\\Users\\tuzuk\\Desktop\\out.MOV", fourcc, fps, (width, height))

i = 0 
while True:
    # 1フレームずつ取得する。
    ret, frame = cap.read()
    
    print(i)
    i = i+1
    if not ret:
        break  # 映像取得に失敗
    
 
import os

import cv2

output_dirpath = 'output'

# VideoCapture を作成する。
cap = cv2.VideoCapture("C:\\Users\\tuzuk\\Desktop\\CIMG.mp4")
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# 保存用ディレクトリを作成する。
os.makedirs(output_dirpath, exist_ok=True)

while True:
    # 1フレームずつ取得する。
    ret, frame = cap.read()
    if not ret:
        break  # 映像取得に失敗
    
    # フレームを画像として保存する。
    frame_no = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
    filepath = os.path.join(output_dirpath, 'frame_{:04d}.png'.format(frame_no))
    cv2.imshow("C:\\Users\\tuzuk\\Desktop\\tmp\\aa", frame)

cap.release()
cv2.destroyAllWindows()
import cv2

video_path = "C:\\Users\\tuzuk\\Desktop\\AboutCV\\WebCamera\\test.mp4"
cap = cv2.VideoCapture(video_path)
dir = "C:\\Users\\tuzuk\\Desktop\\AboutCV\\movie_disassenbled" #出力先

num = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imwrite(dir+"\\picture{:0=3}".format(num)+".jpg",frame)
        print("save picture{:0=3}".format(num)+".jpg")
        num += 1
    else:
        break

cap.release()

import cv2
import sys

img = cv2.imread("C:\\Users\\tuzuk\\Desktop\\CIMG2466.JPG", cv2.IMREAD_UNCHANGED)

 # カラーとグレースケールで場合分け
if len(img.shape) == 3:
     height, width, channels = img.shape[:3]
else:
     height, width = img.shape[:2]
     channels = 1


 
  # カラーとグレースケールで場合分け

print("width: " + str(width))
print("height: " + str(height))
print("channels: " + str(channels))
print("dtype: " + str(img.dtype))
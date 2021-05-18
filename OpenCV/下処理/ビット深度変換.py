import numpy as np
import cv2

img = cv2.imread("C:\\Users\\tuzuk\\Desktop\\CIMG2466.JPG")

def Info_of_Bit(img) :
    
 src = np.array(img, dtype = "float32")

 cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\CIMG2466.JPG", src)

 if len(src.shape) == 3:
     height, width, channels = src.shape[:3]
 else:
     height, width = src.shape[:2]
     
     channels = 1

 print("width: " + str(width))
 print("height: " + str(height))
 print("channels: " + str(channels))
 print("dtype: " + str(src.dtype))
 
import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

img = cv2.imread("C:\\Users\\tuzuk\\Desktop\\Hands\\hand.JPG")

#平均値
blur=cv2.blur(img,(21,21))

#ガウシアン
gau=cv2.GaussianBlur(img,(21,21),0)

cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\Hands\\hand_ave.JPG",blur)
cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\Hands\\hand_gau.JPG",gau)
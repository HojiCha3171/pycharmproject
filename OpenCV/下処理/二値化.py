import cv2
import numpy as np

def main():
    
    img = cv2.imread("C:\\Users\\tuzuk\\Desktop\\tmp.JPG")
    
    gau=cv2.GaussianBlur(img,(99,99),0)
    
    gray = cv2.cvtColor(img,cv2.COLOR_RGBA2GRAY)
    
    ret,thresh1 = cv2.threshold(gray,107,255,cv2.THRESH_BINARY)
    
    cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\tmp_th2.JPG",thresh1)
    
if __name__ == "__main__":
        main()

import cv2

def main():
    img = cv2.imread("C:\\Users\\tuzuk\\Desktop\\green.jpg")

    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    cv2.imwrite("C:\\Users\\tuzuk\\Desktop\\green.jpg",gray)
    
if __name__ == '__main__':
    main()

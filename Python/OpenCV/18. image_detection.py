# 이미지 검출(경계선)
# Canny Edge Detection : 경계선 검출 알고리즘 중 하나. 대중적

import cv2 

def empty(pos):
    pass

img = cv2.imread('snowman.png')

# 트랙바 생성하여 임계값 조절 
name = "Trackbar"
cv2.namedWindow(name)
cv2.createTrackbar('threshold1', name, 0, 255, empty) # minVal
cv2.createTrackbar('threshold2', name, 0, 255, empty) # maxVal

while True:
    threshold1 = cv2.getTrackbarPos('threshold1', name)
    threshold2 = cv2.getTrackbarPos('threshold2', name)

    canny = cv2.Canny(img, threshold1, threshold2)
    # 대상 이미지, minVal(하위 임계값), maxVal(상위 임계값)

    cv2.imshow('img', img)
    cv2.imshow(name, canny)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
# 이미지 변형(흑백)

import cv2 

# 이미지를 흑백으로 읽음
img = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)

# 이미지를 불러온 다음 흑백으로 변경
img2 = cv2.imread('cat.jpg')
dst = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) 

cv2.imshow('img', img)
cv2.imshow('img_whiteBlack',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
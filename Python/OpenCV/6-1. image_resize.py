# 크기 조정 : 이미지
# 1. 고정크기
# 2. 비율설정

import cv2 

# 이미지 : 고정크기
img = cv2.imread('cat.jpg')
img_fixed = cv2.resize(img, (400,500)) # width, height 고정크기   

# 이미지 : 비율설정
img_scale = cv2.resize(img, None, fx=0.5, fy=0.5) # x, y 비율 정의 (0.5배)

## 보간법(interpolation)
# cv2.INTER_AREA : 크기를 줄일 때 사용
# cv2.INTER_CUBIC : 크기를 늘릴 때 사용 (속도 느림, 퀄리티 좋음)
# cv2.INTER_LINEAR : 크기를 늘릴 때 사용 (기본값) 

img_inter = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA) # x, y 비율 정의 (0.5배)
img_inter2 = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC) # x, y 비율 정의 (1.5배)


cv2.imshow('img', img)
cv2.imshow('resize fixed', img_fixed)
cv2.imshow('resize scale', img_scale)
cv2.imshow('resize inter', img_inter)
cv2.imshow('resize inter2', img_inter2)
cv2.waitKey(0)
cv2.destroyAllWindows()
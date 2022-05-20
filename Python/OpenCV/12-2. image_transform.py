# 이미지 변형(원근)
# 회전된 이미지 세우기

import cv2 
import numpy as np

img = cv2.imread('poker.jpg')

width, height = 530, 710 # 그림판으로 이미지 카드사이즈 확인 후 설정

src = np.array([[702, 143],[1133, 414],[726, 1007],[276, 700]], dtype=np.float32) # Input 4개 지점
dst = np.array([[0, 0],[width, 0],[width, height],[0, height]], dtype=np.float32) # Output 4개 지점

matrix = cv2.getPerspectiveTransform(src, dst)             # 이미지 일부 포인트(src)를 출력하고자 하는 창에 매칭 
result = cv2.warpPerspective(img, matrix, (width, height)) # 이미지, 변환, 창크기(해상도)

cv2.imshow('img',img)
cv2.imshow('result',result)

cv2.waitKey()
cv2.destroyAllWindows()
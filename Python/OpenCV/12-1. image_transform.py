# 이미지 변형(원근)
# 사다리꼴 이미지 펼치기

import cv2 
import numpy as np

img = cv2.imread('newspaper.jpg')

width, height = 640, 240 # 가로 크기 640, 세로 크기 240 으로 결과물 출력

# 좌상, 우상, 우하, 좌하 (시계 방향으로 4 지점 정의)
src = np.array([[511, 352],[1008, 345],[1122, 584],[455, 594]], dtype=np.float32) # Input 4개 지점
dst = np.array([[0, 0],[width, 0],[width, height],[0, height]], dtype=np.float32) # Output 4개 지점

matrix = cv2.getPerspectiveTransform(src, dst)             # 이미지 일부 포인트(src)를 출력하고자 하는 창에 매칭 
result = cv2.warpPerspective(img, matrix, (width, height)) # 이미지, 변환, 창크기(해상도)

cv2.imshow('img',img)
cv2.imshow('result',result)

cv2.waitKey()
cv2.destroyAllWindows()
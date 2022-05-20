# 도형 그리기

import cv2
import numpy as np

# 세로 480 x 가로 640, 3 Channel (RGB) 스케치북 만들기
img = np.zeros((480,640,3), dtype=np.uint8) # 이미지 공간 생성

## 이미지 채우기 ------------------------------------------------------------------------------------
#img[:] = (255,255,255)                      # 전체 공간을 흰색(255)으로 채우기 
#img[100:200, 200:300] = (255,255,255)       # 일부 공간을 흰색으로 채우기 [세로영역, 가로영역]

## 직선 그리기 --------------------------------------------------------------------------------------
# cv2.LINE_4  : 상하좌우 4방향으로 연결된 선 
# cv2.LINE_8  : 대각선을 포함한 8방향으로 연결된 선(기본값)
# cv2.LINE_AA : 부드러운 선(anti-aliasing)

COLOR = (0,255,255) # RGB : Yellow
THICKNESS = 3 # 두께

# 그릴 위치(img), 시작점, 끝점, 색깔, 두께, 선 종류
cv2.line(img, (50,100),(400,50), COLOR, THICKNESS, cv2.LINE_8) 
cv2.line(img, (50,200),(400,150), COLOR, THICKNESS, cv2.LINE_4)
cv2.line(img, (50,300),(400,250), COLOR, THICKNESS, cv2.LINE_AA)

## 원 그리기 ----------------------------------------------------------------------------------------
COLOR = (255,255,0)
RADIUS = 50 # 반지름
THICKNESS = 10

# 그릴 위치(img), 원의 중심점, 반지름, 색깔, 두께, 선 종류
cv2.circle(img, (200,100),RADIUS,COLOR,THICKNESS,cv2.LINE_AA)  # 속이 빈 원
cv2.circle(img, (400,100),RADIUS,COLOR,cv2.FILLED,cv2.LINE_AA) # 속이 찬 원

## 사각형 그리기 ------------------------------------------------------------------------------------
COLOR = (0,255,0)
THICKNESS = 3

# 그릴 위치(img), 왼쪽 위 좌표, 오른쪽 아래 좌표, 색깔, 두께
cv2.rectangle(img, (100,100),(200,200),COLOR,THICKNESS)      # 속이 빈 사각형
cv2.rectangle(img, (300,100),(400,300),COLOR,cv2.FILLED)     # 속이 찬 사각형

## 다각형 그리기 ------------------------------------------------------------------------------------
COLOR = (0,0,255)
THICKNESS = 3

pts1 = np.array([ [200,100], [300,100], [300,200] ]) # 꼭지점 좌표 설정
pts2 = np.array([ [400,200], [600,300], [300,200] ]) 

# 그릴 위치, 그릴 좌표, 닫힘 여부, 색깔, 두께, 선종류
cv2.polylines(img, [pts1,pts2], True, COLOR, THICKNESS, cv2.LINE_AA) # 속이 빈 다각형
# 그릴 위치, 그릴 좌표, 색깔
cv2.fillPoly(img, [pts1,pts2], COLOR) # 속이 찬 다각형


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
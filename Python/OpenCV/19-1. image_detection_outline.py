# 이미지 검출(윤곽선)
# 윤곽선 : 경계선을 연결한 선
# step : 흑백변환 -> 2진화(otsu) -> 윤곽선검출 -> 윤곽선 그리기

## 윤곽선 찾기 모드
# cv2.RETR_EXTERNAL : 가장 외곽의 윤곽선만 찾음
# cv2.RETR_LIST     : 모든 윤곽선 찾음 (계층정보 없음)
# cv2.RETR_TREE     : 모든 윤곽선 찾음 (계층 정보를 트리 구조로 생성)


import cv2 

img = cv2.imread('card.png')
target_img = img.copy() # 사본 이미지 

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

contours, hierarchy = cv2.findContours(otsu, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # 윤곽선 검출
# 윤곽선 정보, 계층구조 = 이미지, 윤곽선 찾는 모드(mode), 윤곽선 찾을때 사용하는 근사치 방법(method)

COLOR = (0,200,0) # 녹색
cv2.drawContours(target_img, contours, -1, COLOR, 2) # 윤곽선 그리기 , -1:모든 윤곽선 그리기
# 대상 이미지, 윤곽선 정보, 인덱스(-1 : 전체), 색깔, 두께

cv2.imshow('img',img)
cv2.imshow('gray',gray)
cv2.imshow('otsu',otsu)
cv2.imshow('contour',target_img)


cv2.waitKey(0)
cv2.destroyAllWindows()
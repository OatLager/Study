# 이미지 출력

import cv2

img = cv2.imread('cat.jpg') # 해당 경로의 이미지 파일 읽어오기
img_color = cv2.imread('cat.jpg', cv2.IMREAD_COLOR) 
img_gray = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)
img_unchanged = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)

cv2.imshow('img1', img)      # img(1,2,3,4) 라는 이름의 창에 img(color, gray, unchanged) 를 표시
cv2.imshow('img2', img_color)
cv2.imshow('img3', img_gray)
cv2.imshow('img4', img_unchanged)

key = cv2.waitKey(0)        # 지정된 시간동안 사용자 키 입력 대기 ms (0=무한정 대기)
print(key)                  # 사용자 키 아스키코드 확인
cv2.destroyAllWindows()     # 모든 창 닫기

## 읽기 옵션
# cv2.IMREAD_COLOR     : 컬러 이미지, 투명 영역은 무시(기본값)
# cv2.IMREAD_GRAYSCALE : 흑백 이미지
# cv2.IMREAD_UNCHANGED : 투명 영역까지 포함

# Shape : 이미지의 height, width, channel 정보 
shape = img.shape
print(shape)
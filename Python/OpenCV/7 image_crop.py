# 이미지 자르기 
# : 영역을 잘라서 새로운 윈도우(창)에 표시

import cv2 

img = cv2.imread('cat.jpg')
#size = img.shape # 이미지 크기 확인 : (426,640,3)
#print(size)

crop = img[100:300, 200:400] # 세로 100:200, 가로 300:400 이미지 자름
img[100:300, 400:600] = crop # 기존 이미지에 자른 이미지 삽입


cv2.imshow('img',img)       # 원본 이미지
cv2.imshow('crop', crop)    # 잘린 이미지

cv2.waitKey(0)
cv2.destroyAllWindows()

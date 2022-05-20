# 이미지 검출(윤곽선) 
# - 윤곽선의 경계 사각형 그리기
# - 사각형 면적 구하기

import cv2 

img = cv2.imread('card.png')
target_img = img.copy() # 사본 이미지 

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

contours, hierarchy = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) # 윤곽선 검출
# 윤곽선 정보, 계층구조 = 이미지, 윤곽선 찾는 모드(mode), 윤곽선 찾을때 사용하는 근사치 방법(method)
# mothod : CHAIN_APPROX_NONE - 모든 좌표, CHAIN_APPROX_SIMPLE - 윤곽선 꼭지점 좌표만

COLOR = (0,200,0) # 녹색

idx = 1
for cnt in contours:
    if cv2.contourArea(cnt) > 25000: # 윤곽선 면적 구하기
        x, y, width, height = cv2.boundingRect(cnt)
        cv2.rectangle(target_img, (x,y), (x+width,y+height), COLOR, 2) # 사각형 그리기

        crop = img[y:y+height, x:x+width] # 원본 이미지에서 윤곽선 찾은 크기만큼 자르기 
        cv2.imshow(f'card_crop_{idx}', crop)    
        cv2.imwrite(f'card_crop_{idx}.png', crop) # 자른 파일 저장
        idx += 1 

cv2.imshow('img',img)
cv2.imshow('gray',gray)
cv2.imshow('otsu',otsu)
cv2.imshow('contour',target_img)


cv2.waitKey(0)
cv2.destroyAllWindows()
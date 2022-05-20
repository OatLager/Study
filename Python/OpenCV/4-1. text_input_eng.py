# 텍스트 삽입 

## OpenCV에서 사용하는 글꼴 종류
# cv2.FONT_HERSHEY_SIMPLEX : 보통 크기의 산 세리프(sans-serif) 글꼴
# cv2.FONT_HERSHEY_PLAIN : 작은 크기의 산 세리프 글꼴
# cv2.FONT_HERSHEY_SCRIPT_SIMPLEX : 필기체 스타일 글꼴
# cv2.FONT_HERSHEY_TRIPLEX : 보통 크기의 세리프 글꼴
# cv2.FONT_ITALIC : 기울임(이탤릭체), 다른 폰트와 함께 사용.

import cv2
import numpy as np

img = np.zeros((480,640,3), dtype=np.uint8)

SCALE = 1 # 크기
COLOR = (255,255,255) # 색깔 (흰색)
THICKNESS = 1 # 두께 

# 그릴 위치, 텍스트 내용, 시작 위치, 폰트 종류, 크기, 색깔, 두께
cv2.putText(img, "Nado Simplex", (20,50), cv2.FONT_HERSHEY_SIMPLEX, SCALE,COLOR,THICKNESS)
cv2.putText(img, "Nado Simplex", (20,150), cv2.FONT_HERSHEY_PLAIN, SCALE,COLOR,THICKNESS)
cv2.putText(img, "Nado Simplex", (20,250), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, SCALE,COLOR,THICKNESS)
cv2.putText(img, "Nado Simplex", (20,350), cv2.FONT_HERSHEY_TRIPLEX, SCALE,COLOR,THICKNESS)
cv2.putText(img, "Nado Simplex", (20,450), cv2.FONT_HERSHEY_TRIPLEX | cv2.FONT_ITALIC, SCALE,COLOR,THICKNESS)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
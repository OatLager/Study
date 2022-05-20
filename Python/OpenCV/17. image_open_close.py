# 이미지 변환(열림 & 닫힘)
# 열림(opening) : 침식 후 팽창. 깎아서 노이즈 제거 후 살 찌움
# : dilate(erode(image))
# 닫힘(closing) : 팽창 후 침식. 구멍을 메운 후 다시 깎음

import cv2 
import numpy as np

kernel = np.ones((3,3), dtype=np.uint8)

img = cv2.imread('erode.png',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('dilate.png',cv2.IMREAD_GRAYSCALE)

# 열림
erode1 = cv2.erode(img, kernel, iterations=4)
dilate1 = cv2.dilate(erode1, kernel, iterations=4)

# 닫힘
dilate2 = cv2.dilate(img2, kernel, iterations=6)
erode2 = cv2.erode(dilate2, kernel, iterations=6)

# 원본 이미지
cv2.imshow('gray',img)
cv2.imshow('gray2',img2)
# 열림 이미지
cv2.imshow('erode',erode1)
cv2.imshow('dilate',dilate1)
# 닫힘 이미지
cv2.imshow('erode2',erode2)
cv2.imshow('dilate2',dilate2)


cv2.waitKey(0)
cv2.destroyAllWindows()
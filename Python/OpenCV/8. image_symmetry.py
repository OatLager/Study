# 이미지 대칭

import cv2 

img = cv2.imread('cat.jpg')

# 좌우 대칭
filp_horizontal = cv2.flip(img, 1)   # filpCode > 0 : 좌우 대칭 Horizontal

# 상하 대칭
filp_vertical = cv2.flip(img, 0)     # filpCode = 0 : 상하 대칭 Vertical

# 상하 좌우 대칭
filp_all = cv2.flip(img,-1)          # filpCode = -1 : 상하 좌우 대칭 

cv2.imshow('img', img)
cv2.imshow('flip_horizontal', filp_horizontal)
cv2.imshow('filp_vertical', filp_vertical)
cv2.imshow('filp_all', filp_all)

cv2.waitKey(0)
cv2.destroyAllWindows()

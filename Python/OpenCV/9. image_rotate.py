# 이미지 회전

import cv2 

img = cv2.imread('cat.jpg')

# 시계 방향 : 90도 
rotate_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
# cv2.ROTATE_90_CLOCKWISE        = 시계 방향으로 90도 회전
# cv2.ROTATE_180                 = 180도 회전
# cv2.ROTATE_90_COUNTERCLOCKWISE = 시계 반대방향으로 90도 회전(시계 방향으로 270도 회전)

cv2.imshow('img', img)
cv2.imshow('rotate_90', rotate_90)

cv2.waitKey(0)
cv2.destroyAllWindows()
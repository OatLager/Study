
# 이미지 저장

import cv2
img = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE) # 흑백으로 이미지 불러오기

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

result = cv2.imwrite('save_cat.jpg',img) # save_cat 이름으로 이미지 저장 (jpg, png 등 확장자 변경 가능)
print(result)  # -> 결과가 True이면 저장 완료
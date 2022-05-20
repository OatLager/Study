# 마우스 이벤트 등록

import cv2
from cv2 import EVENT_MOUSEMOVE
from cv2 import EVENT_RBUTTONDBLCLK 

# 함수 정의
def mouse_handler(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN: # 마우스 왼쪽 버튼 누름
        print('마우스 왼쪽 버튼 Down')
        print(x,y)
    elif event == cv2.EVENT_LBUTTONUP:
        print('마우스 왼쪽 버튼 Up')
        print(x,y)
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        print('마우스 왼쪽 버튼 더블클릭')
    elif event == cv2.EVENT_MOUSEMOVE:
        print('마우스 이동')
    elif event == cv2.EVENT_RBUTTONDBLCLK: 
        print('마우스 오른쪽 버튼 클릭')

img = cv2.imread('poker.jpg')

cv2.namedWindow('img') # img 란 이름의 윈도우를 먼저 만들어두는 것, 여기에 마우스 이벤트를 처리하기 위한 핸들러 적용
cv2.setMouseCallback('img', mouse_handler)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
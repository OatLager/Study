# 이미지 스캔 : 마우스 왼쪽 4번 클릭 선 추가.

import cv2
import numpy as np

point_list = []
src_img = cv2.imread('poker.jpg')

COLOR = (255,0,255) # 핑크색
THICKNESS = 3
drawing = False # 선을 그릴지 여부

# 함수 정의
def mouse_handler(event, x, y, flags, param):
    global drawing
    dst_img = src_img.copy()

    if event == cv2.EVENT_LBUTTONDOWN: # 마우스 왼쪽 버튼 누름
       drawing = True # 선을 그리기 시작 
       point_list.append((x,y))

    if drawing:
        prev_point = None # 직선의 시작점

        for point in point_list:
            cv2.circle(dst_img, point, 15, COLOR, cv2.FILLED) # 마우스 클릭시 원모양 점으로 표시 (이미지, 중심점, 크기, 색깔, 채우기)

            if prev_point:
                cv2.line(dst_img, prev_point, point, COLOR, THICKNESS, cv2.LINE_AA)
            prev_point = point

        next_point = (x, y)

        if len(point_list) == 4:
            show_result() # 결과 출력 : 마우스 4번 클릭시 
            next_point = point_list[0] # 첫 번째 클릭한 지점
        cv2.line(dst_img, prev_point, next_point, COLOR, THICKNESS, cv2.LINE_AA)
    

    cv2.imshow('img',dst_img) 

def show_result():
    width, height = 530, 710 # 그림판으로 이미지 카드사이즈 확인 후 설정

    src = np.float32(point_list) # Input 4개 지점
    dst = np.array([[0, 0],[width, 0],[width, height],[0, height]], dtype=np.float32) # Output 4개 지점

    matrix = cv2.getPerspectiveTransform(src, dst)             # 이미지 일부 포인트(src)를 출력하고자 하는 창에 매칭 
    result = cv2.warpPerspective(src_img, matrix, (width, height)) # 이미지, 변환, 창크기(해상도)
    cv2.imshow('result', result)


cv2.namedWindow('img') # img 란 이름의 윈도우를 먼저 만들어두는 것, 여기에 마우스 이벤트를 처리하기 위한 핸들러 적용
cv2.setMouseCallback('img', mouse_handler)

cv2.imshow('img',src_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
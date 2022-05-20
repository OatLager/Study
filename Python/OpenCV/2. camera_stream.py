# 카메라 출력

import cv2
#cap = cv2.VideoCapture(0) # 0번째 카메라 장치 (Device ID)

## IP Camera 출력
url = 'rtsp://username : password@192.168.2.119:554'

cap = cv2.VideoCapture(url)

## 프레임 속성 받아오기
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(w, h) # ex) 640*480

## set 명령어로 원하는 프레임 속성 지정 가능
# ex) 640*480 -> 320*240
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)


if not cap.isOpened():    # 카메라가 열리지 않은 경우
    exit()                # 프로그램 종료 

while True: 
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('camera',frame)
    
    if cv2.waitKey(1) == ord('q'): # 사용자가 q를 입력하면
        break

cap.release()
cv2.destroyAllWindows()

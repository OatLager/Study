# 크기 조정 : 영상
# 1. 고정크기
# 2. 비율설정

import cv2 


cap = cv2.VideoCapture('cat.mp4')

while cap.isOpened():       # 동영상 파일이 올바르게 열렸는지 확인
    ret, frame = cap.read() # ret : 파일 열림 여부, frame : 받아온 이미지 프레임
    if not ret:
        print('더 이상 가져올 프레임이 없습니다.')
        break

    # 기본
    #cv2.imshow('video', frame)
    # 고정크기
    #frame_fixed = cv2.resize(frame, (400,500)) # width, height 고정크기 
    #cv2.imshow('video_fixed', frame_fixed)

    # 비율설정
    frame_scale = cv2.resize(frame, None, fx=1.5, fy=1.5,interpolation=cv2.INTER_CUBIC) # x, y 비율 정의 (1.5배)
    cv2.imshow('video_scale', frame_scale)

    if cv2.waitKey(25) == ord('q'):          # 영상 재생속도 조절 가능/ q버튼으로 종료
        print('사용자 입력에 의해 종료합니다')
        break

cap.release()           # 자원 해제
cv2.destroyAllWindows() # 모든 창 닫기
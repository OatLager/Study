# 동영상 파일 출력

import cv2

cap = cv2.VideoCapture('cat.mp4')

while cap.isOpened():       # 동영상 파일이 올바르게 열렸는지 확인
    ret, frame = cap.read() # ret : 파일 열림 여부, frame : 받아온 이미지 프레임
    if not ret:
        print('더 이상 가져올 프레임이 없습니다.')
        break

    cv2.imshow('video', frame)

    if cv2.waitKey(25) == ord('q'):          # 영상 재생속도 조절 가능/ q버튼으로 종료
        print('사용자 입력에 의해 종료합니다')
        break

cap.release()           # 자원 해제
cv2.destroyAllWindows() # 모든 창 닫기
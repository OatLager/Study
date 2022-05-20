# 동영상 저장

import cv2

cap = cv2.VideoCapture('cat.mp4')

# 코덱 정의
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # *'DIVX' = 'D','I','V','X'
# DIVX - DIVX MPEG-4
# XVID - XVID MPED-4
# FMP4 - FFMPEG MPEG-4
# X264 - H.264
# MJPG - Motion-JPEG

width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 영상 WIDTH 설정 (원본영상 그대로)
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 영상 HEIGHT 설정 (원본영상 그대로)
fps = cap.get(cv2.CAP_PROP_FPS)                     # 영상 FPS 설정 (원본영상 그대로), 영상 속도 조절가능.

# 저장 파일명, 코덱, FPS, 크기(width, height)
out = cv2.VideoWriter('save_cat.avi',fourcc,fps,(width,height))

while cap.isOpened():       # 동영상 파일이 올바르게 열렸는지 확인
    ret, frame = cap.read() # ret : 파일 열림 여부, frame : 받아온 이미지 프레임
    if not ret:
        print('더 이상 가져올 프레임이 없습니다.')
        break

    out.write(frame) # 영상 데이터만 저장(소리x)
    cv2.imshow('video', frame)

    if cv2.waitKey(25) == ord('q'):          # 영상 재생속도 조절 가능/ q버튼으로 종료
        print('사용자 입력에 의해 종료합니다')
        break

out.release()
cap.release()           # 자원 해제
cv2.destroyAllWindows() # 모든 창 닫기
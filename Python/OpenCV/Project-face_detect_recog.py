# 얼굴 인식하여 캐릭터 씌우기
# Face Detection 
# mediapipe lib :  https://google.github.io/mediapipe/solutions/face_detection
# 패키지 설치    : pip install mediapipe

import cv2
import mediapipe as mp

## 얼굴을 찾고, 찾은 얼굴에 표시를 해주기 위한 변수 정의
mp_face_detection = mp.solutions.face_detection # 얼굴 검출을 위해 face_detection 모듈을 사용
mp_drawing = mp.solutions.drawing_utils         # 얼굴의 특징을 그리기 위한 drawing_utils 모듈을 사용


## 카메라 연결 ---------------------------------------------------------------------
# For webcam input:
cap = cv2.VideoCapture(0)

# For ip camera input: viewpro
#url = 'rtsp://username : password@192.168.2.119:554'
#cap = cv2.VideoCapture(url)

##
with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.7) as face_detection:
    # model_selection :
    # - 0 : 카메라로부터 2m 이내의 근거리 
    # - 1 : 5m 정도의 거리에 적합
    # min_detection_confidence : 얼굴 인식을 위한 threshold 0~1 (0.5 = 50%)

  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # mediapipe에서 RGB로 처리하기때문에 BGR->RGB 변환
    results = face_detection.process(image)

    # Draw the face detection annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    ## 영상에서 얼굴이 검출되면 표시
    if results.detections: 
      # 6개 특징 : 오른쪽 눈, 왼쪽 눈, 코 끝부분, 입 중심, 오른쪽 귀, 왼쪽 귀
      for detection in results.detections:
        mp_drawing.draw_detection(image, detection)
        # print(detection)

        # 특정 위치 가져오기
        keypoints = detection.location_data.relative_keypoints
        right_eye = keypoints[0] # 오른쪽 눈 위치 0~1
        left_eye  = keypoints[1] # 왼쪽 눈 위치 0~1

        h, w, _ = image.shape # 이미지로부터 세로, 가로 크기 가져옴
        right_eye = (int(right_eye.x * w), int(right_eye.y * h)) # 이미지 내에서 실제 좌표 x, y 계산
        left_eye  = (int(left_eye.x * w), int(left_eye.y * h))

        # 양 눈에 동그라미 그리기
        cv2.circle(image, right_eye, 10, (255,0,0), 10, cv2.LINE_AA) # 오른쪽 눈 : 파란색 동그라미
        cv2.circle(image, left_eye, 10, (0,255,0), 10, cv2.LINE_AA) # 왼쪽 눈 : 초록색 동그라미

    # Flip the image horizontally for a selfie-view display. 
    cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1)) # flip : 좌우반전 

    if cv2.waitKey(5) & 0xFF == 27: # esc로 종료 
      break

cap.release()
cv2.destroyAllWindows()
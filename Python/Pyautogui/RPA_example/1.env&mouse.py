# https://www.youtube.com/watch?v=exgO1LFl9x8&t=0s

import pyautogui

size = pyautogui.size() #현재 화면의 스크린 사이즈를 가져옴
print(size) # 현재 화면의 스크린 사이즈 확인 ex) 2560*1600
            # size[0] : width, size[1] : height

# 마우스 이동 (절대 좌표)
pyautogui.moveTo(100,100) # 지정한 위치로 마우스를 이동 (가로x, 세로y)
pyautogui.moveTo(500,500, duration=2) # 2초 동안 500,500 위치로 이동

# 마우스 이동 (상대 좌표)
pyautogui.move(-100,-100, duration=1) # 현재 커서가 있는 위치로부터 이동
p = pyautogui.position()
print(p[0], p[1])
print(p.x, p.y)

## action 
# sleep : 대기
pyautogui.sleep(3) # 3초 대기
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용
# click : 마우스 클릭
pyautogui.click(100,100,duration=1) # 좌표를 마우스 클릭
pyautogui.click(clicks=500) # 500번 클릭
# click 세분화, 누르기(Down)&떼기(Up) 
pyautogui.mouseDown()
pyautogui.mouseUp()
# doubleClick : 더블 클릭
pyautogui.doubleClick()

# 드래그 방법 1
pyautogui.moveTo(200,200)
pyautogui.mouseDown()
pyautogui.moveTo(500,500)
pyautogui.mouseUp()
# 드래그 방법 2 (상대좌표)
pyautogui.drag(100,0, duration=0.25) # 현재 위치 기준으로 x=100, y=0만큼 드래그 
                                     # 빠른 동작으로 실행이 안될때는 duration을 사용함.
# 드래그 방법 3 (절대좌표)
pyautogui.dragTo(100,0, duration=0.25)

# 마우스 클릭(오른쪽, 휠)
pyautogui.rightClick() # 마우스 오른쪽 클릭 
pyautogui.middleClick() # 마우스 휠 클릭

# 스크롤
pyautogui.scroll(300) # 양수 : 위 방향, 음수 : 아래 방향 스크롤

# 마우스 정보 획득
pyautogui.mouseInfo() # 마우스 좌표, 색상 등 정보 획득 가능
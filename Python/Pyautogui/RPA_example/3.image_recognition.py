# cd Python_example\Pyautogui\RPA_example
# 해상도, 이미지 변경시 사용불가
import pyautogui

file_menu = pyautogui.locateOnScreen("file_menu.png")
# fn(win) + shift + s 캡쳐 -> 그림판(자르기) -> 이미지저장

print(file_menu)
pyautogui.click(file_menu)

# 이미지에 해당하는 부분이 둘 이상일 경우 -------------------------
# pyautogui.locataAllOnScreen() 사용. 

# for i in pyautogui.locateAllOnScreen("파일명.png")
#     print(i)
#     pyautogui.click(i, duration=0.25)


# 속도 개선 -----------------------------------------------------
# 1. GrayScale
# p = pyautogui.locateOnScreen("file_menu.png", grayscale=True)
# pyautogui.moveTo(p)

# 2. 범위 지정
# p = pyautogui.locateOnScreen("file_menu.png", region=(x,y,width,height)) # x,y,width,height 범위 지정
# pyautogui.moveTo(p)

# 3. 정확도 조정 - opencv 사용
# isntall : pip install opencv-python
# p = pyautogui.locateOnScreen("file_menu.png", confidence=0.9) # confidence : 정확도 (0.9=90%)
# pyautogui.moveTo(p)


# Example 
# 1. 계속 기다리기

# 2. 일정 시간동안 기다리기 (TimeOut)
import time
import sys

timeout = 10 # 10초 대기
start = time.time() # 시작 시간 설정

file_menu_notepad = None
while file_menu_notepad is None:
    file_menu_notepad = pyautogui.locateOnScreen("file_menu.png")
    end = time.time() # 종료 시간 설정
    if end - start > timeout:
        print("시간 종료")
        sys.exit()

pyautogui.click(file_menu_notepad)
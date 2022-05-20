# pip install pyperclip  # 어떤 문장을 클립보드로 저장 
# -> pyautogui.write()는 한글 불가, pyperclip를 사용하여 클립보드에 저장하여 붙여넣기 방식으로 한글 사용.

import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 1개 띄운 상태에서 창 정보 가져옴
w.activate()

# pyautogui.write("12345")
# pyautogui.write("NadoCoding", interval=0.25) # interval = 글자 쓰는 속도
# pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"], interval = 0.1)

# 특수문자
# ex. shift + 4 -> $ 
pyautogui.keyDown("shift") # shift 키를 누른 상태에서
pyautogui.press("4")       # 숫자 4를 입력하고
pyautogui.keyUp("shift")   # shift 키를 뗀다

# 간편한 조합키
pyautogui.hotkey("ctrl","alt","shift","a")
# ctrl 누르고 > alt 누르고 > shift 누르고 > a 누르고 > a 떼고 > shift 떼고 > alt 떼고 > ctrl 떼고 

# 한글 사용하기
import pyperclip
pyperclip.copy("나도코딩") # "나도코딩" 글자를 클립보드에 저장
pyautogui.hotkey("ctrl","v") # 클립보드에 있는 내용을 붙여넣기

# 함수로 만들어서 쉽게 한글 사용하기
def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")

my_write("쉬운한글")

# 자동화 프로그램 종료
# win : ctrl + alt + del
# mac : cmd + chift + option + q
import pyautogui

# 스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png") # png 파일로 저장

pixel = pyautogui.pixel(50,50)
print(pixel)

p = pyautogui.pixelMatchesColor(50,50, (255,255,255)) # true or false 출력 (x, y, 비교대상(rgb))
print(p)
# pyautogui, opencv 필요

import pyautogui

i = pyautogui.locateOnScreen('7.png')
print(i)
# q = pyautogui.center(i)
# print(q)
# pyautogui.click(q)


i = pyautogui.locateCenterOnScreen('1.png')
print(i)
pyautogui.click(i)

# print(pyautogui.position())
# pyautogui.screenshot('1.png', region=(946,1308,30,30))
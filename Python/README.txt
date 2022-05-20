# HTML/CSS, PYTHON 

Python ====================================================================
참고강의 : https://blog.naver.com/sheld2/222595173620

pyinstaller ---------------------------------------------------------------
: py파일을 실행파일로 생성

참고강의 : https://taedi.net/11

(install)
pip install pyinstaller

(example) 실행파일 생성
py파일 경로에서 다음 명령 실행
pyinstaller --onefile xxx.py

# --onefile : 하나의 실행파일로 생성
# --noconsole : 콘솔창이 뜨지 않게 실행
# --icon=xxx.ico : 실행파일의 아이콘 이미지 설정. (.ico만 가능)
   ex) pyinstaller --icon=xxx.ico --onefile xxx.py

MACRO ======================================================================
1. pyautogui ---------------------------------------------------------------
: 마우스 및 키보드 제어 유용

(install)
pip install pyautogui


2. selenium ----------------------------------------------------------------
: 웹 기반 객체요소 제어 유용

참고강의 : https://www.youtube.com/watch?v=_gkhgS33QIc

(install) 
pip install selenium 

Chrome use. 
check Chrome ver : chrome - 설정 - Chrome 정보 - 버전(ex.99.0.4844.74)
download chromedriver : https://chromedriver.chromium.org/downloads

(example) 제어 가능한 chrome 창 띄우기
from selenium import webdriver
driver = webdriver.Chrome('C:\Users\jhpar\Desktop\GIT-JH\GUI\temp\chromedriver.exe')

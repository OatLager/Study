# 예제 : selenium을 사용하여 자동으로 Chrome에서 특정 사이트를 띄워서 로그인하기.

from selenium import webdriver
import time

# Chrome 띄우기
driver = webdriver.Chrome('D:\Temp\chromedriver.exe')           # 경로설정 오류 주의

# 특정 사이트 접속
# - 사이트 주소 설정
url = 'https://accounts.kakao.com/login?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fodin.game.daum.net%252Fodin%252F%253Ftr%253D18%2526utm_campaign%253Dodin_chapter5_Update%2526utm_medium%253DBrandSA%2526utm_source%253DNaver%2526utm_content%253DBrandsearch_PC%2526utm_term%253DPC_homelink_1223'
# - 사이트 접속
driver.get(url)
time.sleep(1)
# - 사이트 로그인 / 사이트 객체 추출 (F12) 
id_email     = "asgtr0623@naver.com"                            # 계정 아이디
id_pwd       = "qkrwlgns92"                                     # 계정 패스워드
# - 사이트 로그인 / 아이디 입력창 객체 지정 및 입력
input_id     = "//input[@id='id_email_2']"                      # 아이디 입력창 객체 추출 xpath
input_window = driver.find_element_by_xpath(input_id)           # 아이디 입력창 객체 지정
input_window.send_keys(id_email)                                # 아이디 입력
time.sleep(1)
# - 사이트 로그인 / 패스워드 입력창 객체 지정 및 입력
input_pwd    = "//input[@id='id_password_3']"                   # 패스워드 입력창 객체 추출 xpath
input_window = driver.find_element_by_xpath(input_pwd)          # 패스워드 입력창 객체 지정
input_window.send_keys(id_pwd)                                  # 패스워드 입력
time.sleep(1)
# - 사이트 로그인 / 로그인 버튼 클릭 
path_login   = "//button[@class='btn_g btn_confirm submit']"    # 로그인 버튼 객체 추출 xpath
btn_login    = driver.find_element_by_xpath(path_login)         # 로그인 버튼 객체 지정
btn_login.click()                                               # 로그인 버튼 클릭
time.sleep(1)


from selenium import webdriver #pip install selenium      # 업그레이드 : pip install --upgrade selenium
from selenium.webdriver.chrome.service import Service #pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install()) #크롬 드라이버 자동설치

driver = webdriver.Chrome(service=service)

driver.get("https://naver.com")
time.sleep(2)

## selenium 버전 4.5 미만은 위에 처럼 해야 자동 드라이버 설치

## selenium 버전 4.6 이상은 아래처럼만 하면 자동 드라이버 설치

driver = webdriver.Chrome()

driver.get("https://naver.com")
time.sleep(2)
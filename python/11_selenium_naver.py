from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

options = Options()

options.add_argument("--start-maximized") #화면 최대 사이즈
options.add_experimental_option("detach", True) #화면 안꺼지게

driver = webdriver.Chrome(options=options)

url = "https://naver.com"

driver.get(url)
time.sleep(2)

driver.find_element(By.ID, "query").send_keys("뉴진스")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".btn_search").click()
time.sleep(2)

# driver.find_elements(By.CSS_SELECTOR, ".flick_bx")[2].click() #0 1 2
# time.sleep(2)

driver.find_element(By.XPATH, '//*[text()="VIEW"]').click() # 하위에 있는 모든것에서 VIEW를 찾아라 '//a[text()="VIEW"]'라면 a태그
time.sleep(2)

driver.find_element(By.NAME, "query").clear()
time.sleep(2)

driver.find_element(By.NAME, "query").send_keys("에스파")
time.sleep(2)

driver.find_element(By.NAME, "query").send_keys(Keys.ENTER)
time.sleep(2)

for i in range(10):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(2)

html = driver.page_source # 모든것을 하고 난 뒤에 위치를 설정

soup = BeautifulSoup(html, "html.parser")

view_wraps = soup.select(".view_wrap")


#title_link _cross_trigger 만약 띄어쓰기 빈칸이 있으면 .으로 채워야한다

for view_wrap in view_wraps:
    name = view_wrap.select_one(".name")
    title = view_wrap.select_one(".title_link")
    print(name.text)
    print(title.text)
    print()

print(len(view_wraps))    

# driver.save_screenshot() ()안에 폴더를 입력해야함 #스크린샷 저장

driver.quit()
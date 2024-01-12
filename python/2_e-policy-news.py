from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time



options = Options()

options.add_argument("--start-maximized") #화면 최대 사이즈
options.add_experimental_option("detach", True) #화면 안꺼지게

driver = webdriver.Chrome(options=options)

url = "https://e-policy.or.kr/news/today_news.php"

driver.get(url)


driver.find_element(By.CSS_SELECTOR, ".select").click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[text()="제목+내용"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@title="검색어를 입력하세요."]').send_keys("저", Keys.ENTER)
time.sleep(1)


a_tags = driver.find_elements(By.CSS_SELECTOR, ".subject > a")

links = []

for a_tag in a_tags:
    # 현재 a 태그의 href 속성 값을 가져와서 links 리스트에 추가합니다.
    href_value = a_tag.get_attribute('href')
    links.append(href_value)

# 리스트의 인덱스를 사용하여 요소를 처리
for i in links:
    driver.get(i)
    time.sleep(1)
    driver.back()
    time.sleep(1)
    print(links)
     
    

   
   



# for i in range(13):
#     page = driver.find_element(By.XPATH, '//*[@title="현재페이지"]')
#     action = ActionChains(driver)
#     action.move_to_element(page).perform()
#     current_page = int(page.text)
#     next_page = current_page + 1
#     driver.find_element(By.LINK_TEXT, str(next_page)).click()
#     time.sleep(1)
#     if next_page % 5 == 0:
#             driver.find_element(By.CLASS_NAME, 'next').click()
#             time.sleep(1)
       




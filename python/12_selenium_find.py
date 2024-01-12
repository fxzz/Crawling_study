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

'''
<input id="query" name="query" type="search" title="검색어를 입력해 주세요."
placeholder="검색어를 입력해 주세요." maxlength="255" autocomplete="off"
class="search_input" data-atcmp-element="">
'''

# driver.find_element(By.XPATH, '//*[@title="검색어를 입력해 주세요."]').send_keys("블랙핑크", Keys.ENTER)
# time.sleep(2)

# # driver.find_element(By.XPATH, '//*[text()="VIEW"]').click() 둘다 같다 텍스트를 꼭 찝어서 찾는다면 이방법이 편함
# driver.find_element(By.LINK_TEXT, "VIEW").click()

# driver.find_element(By.PARTIAL_LINK_TEXT, "인플루언").click() #인플루언서를 클릭하는것인데 인플루언을 써도 가능

link_service = driver.find_elements(By.CSS_SELECTOR, ".link_service")

# print(link_service)
# print()
# print(dir(link_service[0])) #dir()은 사용할수있는 메서드나 변수를 보여줌
# print()
# print(len(link_service))

for link in link_service:
    # print(link.get_attribute("outerHTML"))
    print(link.text)
    if link.text == "쇼핑":
        link.click()
        time.sleep(2)

driver.quit()
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time
from bs4 import BeautifulSoup

options = Options()

user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/120.0.0.0"

options.add_argument(f"user-agent={user_agent}")

options.add_argument("--start-maximized") #화면 최대 사이즈
options.add_experimental_option("detach", True) #화면 안꺼지게

driver = webdriver.Chrome(options=options)

url = "https://m2.melon.com/index.htm"

driver.get(url)
time.sleep(2)

print(driver.current_url)

if driver.current_url != url:
    driver.get(url)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".banner_full_close_today").click()
    time.sleep(2)

driver.find_element(By.XPATH, '//*[text()="멜론차트"]').click()
time.sleep(2)

driver.find_elements(By.CSS_SELECTOR, "#moreBtn")[1].click()
time.sleep(2)

#방법1
chartList = driver.find_element(By.CSS_SELECTOR, "#_chartList")
items = chartList.find_elements(By.CSS_SELECTOR, ".list_item")



# 방법2
# items = driver.find_elements(By.CSS_SELECTOR, ".list_item")

# for item in items[:]: #[:]복사
#     try:
#         ranking = item.find_element(By.CSS_SELECTOR, ".ranking_num")
#         print(ranking.text)
#         print()
#     except NoSuchElementException:
#         items.remove(item)

action = ActionChains(driver)

# action.move_to_element(items[90]).perform()

for item in items:
    action.move_to_element(item).perform()
    title = item.find_element(By.CSS_SELECTOR, ".title.ellipsis")
    name = item.find_element(By.CSS_SELECTOR, ".name.ellipsis")

    thumb = item.find_element(By.CSS_SELECTOR, ".inner > span")
    thumb.click()
    time.sleep(1)
    album_url = driver.current_url
    driver.back() #뒤로가기
    time.sleep(1)
    
    
    print(title.text)
    print(name.text)
    print(f"album_url : {album_url}")
    print()
    time.sleep(1)
    
print(len(items))
driver.quit()
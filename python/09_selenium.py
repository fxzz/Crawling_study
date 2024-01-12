from selenium import webdriver
from bs4 import BeautifulSoup
import time

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
keyword = input("검색어를 입력하세요 : ")

url = base_url + keyword
print(url)

driver = webdriver.Chrome()

driver.get(url)
time.sleep(3)

for i in range(5): # 0 1 2 3 4 로 i에 반복
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")  # 스크롤 끝까지 내리기
    time.sleep(2)

html = driver.page_source


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
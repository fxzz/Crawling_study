import requests
from bs4 import BeautifulSoup

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
keyword = input("검색어를 입력하세요 : ")

url = base_url + keyword
print(url)

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}



req = requests.get(url, headers=headers)

html = req.text


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
import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}

base_url = "https://www.coupang.com/np/search?component=&q="

keyword = input("검색할 상품을 입력하세요 : ")

search_url = base_url + keyword

cookie = {"a": "b"}

req = requests.get(search_url, timeout=5, headers=headers, cookies=cookie) #쿠팡은 쿠키까지 넣어줘야함

#print(req.status_code) 응답결과 200

html = req.text

soup = BeautifulSoup(html, "html.parser")

items = soup.select("[class=search-product]")

for item in items:

    rocket = item.select_one(".badge.rocket") #로켓제품만 가져오기
    if not rocket:
        continue

    title = item.select_one(".name").text
    price = item.select_one(".price-value").text
    thumb = item.select_one("")
    
    print(title, price)


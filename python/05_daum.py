import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}

url = "https://news.daum.net/"

req = requests.get(url, headers=headers)
html = req.text

soup = BeautifulSoup(html, "html.parser")

item_issue = soup.select(".item_issue")

for i in item_issue:
  title = i.select_one(".link_txt")
  title_link = title['href']
  title_text = title.text.strip() # strip() 문자열 공백 제거
  #thumb = i.select(".thumb_g")[1]['alt']
  alt = i.select_one(".logo_cp img")["alt"]
  category = i.select_one(".txt_category").text
  print(title_text)
  print(alt)
  print(category)
  print(title_link)
  print()


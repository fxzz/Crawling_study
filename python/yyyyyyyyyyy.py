import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}

url = "http://gall.dcinside.com/board/lists/?id=baseball_new11"
session = requests.Session()

req = session.get(url, headers=headers)
html = req.text

soup = BeautifulSoup(html, "html.parser")

tr_elements = soup.select("tbody .ub-content.us-post")

# 주요 매직 넘버 변수 선언
GALL_NUM_SELECTOR = ".gall_num"
GALL_TITLE_SELECTOR = ".gall_tit.ub-word a"
GALL_WRITER_SELECTOR = ".gall_writer .nickname em"
GALL_DATE_SELECTOR = ".gall_date"
GALL_VIEWS_SELECTOR = ".gall_count"
GALL_RECOMMENDS_SELECTOR = ".gall_recommend"

for tr in tr_elements:
    post_number = tr.select_one(GALL_NUM_SELECTOR).text
    

    print(f"게시물 번호: {post_number}")
  


  

    
session.close()

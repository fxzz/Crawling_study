import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}

url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"

req = requests.get(url, headers=headers)

html = req.text

soup = BeautifulSoup(html, "html.parser")

movie_chart = soup.select_one(".sect-movie-chart")

li_tag = movie_chart.select("li") #태그를 가져올때는 "li" 이렇게 하면 됨

#print(len(li_tag)) len()으로 갯수 확인

# for movie in li_tag:
#     title = movie.select_one(".title").text
#     score = movie.select_one(".score")
#     ticketing = score.select_one(".percent")
#     a = score.select_one(".egg-gage.small > .percent") # .egg-gage.small 안에 자식 .percent 클래스 찾기
#     info = movie.select_one(".txt-info > strong").next_element # <strong>2024.01.10<span>개봉</span></strong> 여기중에 <strong>2024.01.10 만 가져옴
#     print(f"제목:{title}, 예매율:{ticketing.text}, 스코어:{a.text}, 개봉일:{info.strip()}") #strip() 문자 공백 제거 
#     print()

# 1부터 시작
for rank, movie in enumerate(li_tag, 1):
    title = movie.select_one(".title").text
    score = movie.select_one(".score")
    ticketing = score.select_one(".percent")
    a = score.select_one(".egg-gage.small > .percent") # .egg-gage.small 안에 자식 .percent 클래스 찾기
    info = movie.select_one(".txt-info > strong").next_element # <strong>2024.01.10<span>개봉</span></strong> 여기중에 <strong>2024.01.10 만 가져옴
    print(f"순위:{rank}, 제목:{title}, 예매율:{ticketing.text}, 스코어:{a.text}, 개봉일:{info.strip()}") #strip() 문자 공백 제거 
    print()


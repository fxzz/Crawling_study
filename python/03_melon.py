import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}

url = "https://www.melon.com/chart/index.htm"

req = requests.get(url, headers=headers)

html = req.text

soup = BeautifulSoup(html, "html.parser")

lst50 = soup.select(".lst50")
lst100 = soup.select(".lst100")

i = lst50 + lst100

def get_song_nums(text):
    song_num = []
    for num in text:
        if num.isdigit():  #isdigit() 문자열중에 숫자는 true
            song_num.append(num)
    song_num = "".join(song_num)
    return song_num  


for rank ,lst in enumerate(i, 1):
    title = lst.select_one(".ellipsis.rank01 a")
    singer = lst.select_one(".ellipsis.rank02 a")
    singer_link = get_song_nums(singer['href'])
    
    album = lst.select_one(".ellipsis.rank03 a")
    album_link = get_song_nums(album['href'])
    print(f"{rank} : {title.text} : {singer.text} : https://www.melon.com/artist/timeline.htm?artistId={singer_link} : {album.text} : https://www.melon.com/album/detail.htm?albumId={album_link}")
    
    print()
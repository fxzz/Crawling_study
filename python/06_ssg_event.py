import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}

url = "https://www.ssg.com/event/eventMain.ssg"

req = requests.get(url, headers=headers)

html = req.text

soup = BeautifulSoup(html, "html.parser")

evt_osmu_lst = soup.select(".evt_osmu_lst")[0]

links = evt_osmu_lst.select(".eo_link")



for a in links:
  link = a['href']
  if link.startswith("https"):
    print(link)
  else:
    print(f"https://www.ssg.com/{link}") #링크가 몇개만 nevntId=1000000010956&domainSiteNo=6005&_mpop=new 이렇게 올때
  
  eo_in = a.select_one(".eo_in")

  text_list = eo_in.find_all(string=True)

  for text in text_list:
      if text != "\n":
          print(text)
          print()
 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

options = Options()

user_data = r"C:\python\user"

options.add_experimental_option("detach", True) # 옵션을 줘서 화면을 안꺼짐 , 잘안씀

options.add_argument(f"user-data-dir={user_data}")


options.add_argument(f"user-agent={user_agent}")

options.add_argument("--start-maximized") # 최대 크기 화면 , 잘씀 , 아래 2개도 잘씀
options.add_experimental_option("excludeSwitches", ["enable-automation"]) # 크롬 상단에 테스트 메세지 안뜨게
options.add_experimental_option("excludeSwitches", ["enable-logging"])  # 불필요한 메세지 제거

#options.add_argument("--mute-audio") # 유튜브나 자동 재생되는 사이트 음소거
#options.add_argument("incognito") # 시크릿모드 접속


#options.add_argument("--headless") # 헤드리스모드 : 크롬 창이 안켜지고 데이터를 가져옴, 용도: 작업끝내고 확실할때 사용
#options.add_argument("--disable-gpu") 헤드리스 모드가 안될때 같이 사용



driver = webdriver.Chrome(options=options)

driver.get("https://naver.com")

print(driver.page_source)

# driver.quit() # 작업이 완료되면 크롬을 닫음 
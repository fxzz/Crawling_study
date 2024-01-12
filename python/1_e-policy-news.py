import psycopg2
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
options = Options()

options.add_argument("--start-maximized") #화면 최대 사이즈
options.add_experimental_option("detach", True) #화면 안꺼지게

driver = webdriver.Chrome(options=options)



conn = {
    'port': '5432',
    'user': 'postgres',
    'password': '1234',
}
connection = psycopg2.connect(**conn)
cursor = connection.cursor()
insert_query = """
    INSERT INTO test.main (id, subject, date, views)
    VALUES (%s, %s, %s, %s)
"""
select_query = """
    SELECT id FROM test.main WHERE id = %s
"""


def current_page_crawling():
    tbody = driver.find_element(By.CSS_SELECTOR, "tbody")
    tr_tags = tbody.find_elements(By.CSS_SELECTOR, "tr")

    for tr_tag in tr_tags:
        td_tags = tr_tag.find_elements(By.CSS_SELECTOR, "td")

        id = td_tags[0].text
        subject = td_tags[1].text
        date = td_tags[2].text
        views = td_tags[3].text

        print(f"insert( id : {id}, subject : {subject}, date : {date}, views : {views} )")
        print()
        if not is_id_exist(id):
            cursor.execute(insert_query, (id, subject, date, views))



def move_to_page(num):
    url = f"https://e-policy.or.kr/news/today_news.php?page={num}&prd_cate=&make=all&search="
    driver.get(url)
    
# id가 있으면 true    
def is_id_exist(id): 
    cursor.execute(select_query, (id,))
    result = cursor.fetchone()
    return result is not None


# 시작, 종료, a 태그가 3개면 마지막 페이지라 인식하고 종료
start_page = 1
end_page = 1000000000

# 페이지 이동 및 크롤링
for page in range(start_page, end_page):
    move_to_page(page)
    current_page_crawling()
    paging_a = driver.find_elements(By.CSS_SELECTOR, ".paging > a")
    if len(paging_a) == 3:
        break
# 마지막 페이지 다시 구해야함

# 커밋, 연결 및 커서 닫기
connection.commit()
cursor.close()
connection.close()



    


        
        
    
    


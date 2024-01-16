from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import math
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
import zipfile
import psycopg2
import os
from selenium.webdriver.support.ui import WebDriverWait

## 오류 모음
## 




options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"]) # 크롬 상단에 테스트 메세지 안뜨게

options.add_argument("--start-maximized") #화면 최대 사이즈
options.add_experimental_option("detach", True) #화면 안꺼지게
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)

url = "https://www.data.go.kr/tcs/dss/selectDataSetList.do?keyword=날씨"

driver.get(url)


#PostgreSQL 연결 설정
connection = psycopg2.connect(
    port="5432",
    user="postgres",
    password="1234"
)



time.sleep(2)

# 파일데이터 클릭
driver.find_element(By.CSS_SELECTOR, "#dTypeFILE > a").click()

time.sleep(2)




# 총 페이지 수를 가지고 페이지 사이즈 체크
page_count = driver.find_element(By.CSS_SELECTOR, "#fileCnt2")
total_page = int(page_count.text)
page_size = 10
pages = math.ceil(total_page / page_size)
print(pages)





# 오픈API 상세페이지 크롤링
#def open_api_detail_page_crawling():



# 파일 데이터 상세페이지 크롤링
def file_data_detail_page_crawling():
     
    tbody = driver.find_element(By.CSS_SELECTOR, ".file-meta-table-pc > table > tbody")
    tr = tbody.find_elements(By.CSS_SELECTOR, "tr")
    #파일데이터명
    td_01 = tr[0].find_element(By.CSS_SELECTOR, "td")
    file_name_td01 = td_01.get_attribute("innerText")
    print(f"파일데이터명:{file_name_td01}")

    td = tr[1].find_elements(By.CSS_SELECTOR, "td")
    #분류체계
    td_02 = td[0]
    #제공기관
    td_03 = td[1]
    print(f"분류체계:{td_02.text}, 제공기관:{td_03.text}")

    td = tr[2].find_elements(By.CSS_SELECTOR, "td")
    #관리부서명
    td_04 = td[0]
    #관리부서 전화번호
    td_05 = td[1]
    print(f"관리부서명:{td_04.text}, 관리부서 전화번호:{td_05.text}")

    td = tr[3].find_elements(By.CSS_SELECTOR, "td")
    #보유근거
    td_06 = td[0]
    #수집방법
    td_07 = td[1]
    print(f"보유근거:{td_06.text}, 수집방법:{td_07.text}")

    td = tr[4].find_elements(By.CSS_SELECTOR, "td")
    #업데이트 주기
    td_08 = td[0]
    #차기 등록 예정일
    td_09 = td[1]
    print(f"업데이트 주기:{td_08.text}, 차기 등록 예정일:{td_09.text}")

    td = tr[5].find_elements(By.CSS_SELECTOR, "td")
    #매체유형
    td_10 = td[0]
    #전체 행
    td_11 = td[1]
    print(f"매체유형:{td_10.text}, 전체 행:{td_11.text}")

    td = tr[6].find_elements(By.CSS_SELECTOR, "td")
    #확장자
    td_12 = td[0]
    #키워드
    td_13 = td[1]
    print(f"확장자:{td_12.text}, 키워드:{td_13.text}")

    td = tr[7].find_elements(By.CSS_SELECTOR, "td")
    #누적 다운로드
    td_14 = td[0]
    #다운로드
    td_15 = td[1]
    print(f"누적 다운로드:{td_14.text}, 다운로드:{td_15.text}")
    
    td = tr[8].find_elements(By.CSS_SELECTOR, "td")
    #등록일
    td_16 = td[0]
    #수정일
    td_17 = td[1]
    print(f"등록일:{td_16.text}, 수정일:{td_17.text}")


    #데이터 한계
    td_18 = tr[9].find_element(By.CSS_SELECTOR, "td")
    print(f"데이터 한계:{td_18.text}")

    #제공형태
    td_19 = tr[10].find_element(By.CSS_SELECTOR, "td")
    print(f"제공형태:{td_19.text}")

    #설명
    td_20 = tr[11].find_element(By.CSS_SELECTOR, "td")
    print(f"설명:{td_20.text}")

    #기타 유의사항
    td_21 = tr[12].find_element(By.CSS_SELECTOR, "td")
    print(f"기타 유의사항:{td_21.text}")

    # # 파일 다운로드 클릭 : target_folder는 다운로드 클릭 시 다운되는 곳
    target_folder = 'C:\\Users\\PC\\Downloads\\'
    #C:\Users\PC\Downloads, 'C:\\Users\\USER\\Downloads\\'

    file_name = file_name_td01 + ".csv" 

    try:
        div_download = driver.find_element(By.CSS_SELECTOR, ".d-flex.float-r.just-pc")
        action = ActionChains(driver)
        action.move_to_element(div_download).perform()
        a_tag = div_download.find_element(By.CSS_SELECTOR, "a")
        if a_tag.text == "다운로드":
           a_tag.click()
           time.sleep(1)
           try:
               alert = Alert(driver)
               alert.accept()   
           except NoAlertPresentException:
                print("alert가 나타나지 않았습니다.")

           time.sleep(10)
           # 나중에 다운로드가 제대로 완료되면 다음으로 가지게 바꿔야함
           create_zip_file(target_folder, file_name)     
           time.sleep(3)
    except NoSuchElementException:
        print("다운로드 요소를 찾을 수 없습니다.")

    detail_pk = insert_detail_page(
    file_name_td01, #파일명
    td_02.text,  # 분류체계
    td_03.text,  # 제공기관
    td_04.text,  # 관리부서명
    td_05.text,  # 관리부서 전화번호
    td_06.text,  # 보유근거
    td_07.text,  # 수집방법
    td_08.text,  # 업데이트 주기
    td_09.text,  # 차기 등록 예정일
    td_10.text,  # 매체유형
    td_11.text,  # 전체 행
    td_12.text,  # 확장자
    td_13.text,  # 키워드
    td_14.text,  # 누적 다운로드
    td_15.text,  # 다운로드
    td_16.text,  # 등록일
    td_17.text,  # 수정일
    td_18.text,  # 데이터 한계
    td_19.text,  # 제공형태
    td_20.text,  # 설명
    td_21.text   # 기타 유의사항
    )

    return detail_pk




        



def create_zip_file(target_folder, file_name):
    file_name_without_extension = os.path.splitext(file_name)[0]
    source_path = os.path.join(target_folder, file_name)
    zip_path = os.path.join(target_folder, file_name_without_extension + ".zip")
    time.sleep(3)
    try:
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            zipf.write(source_path, arcname=file_name)
        print("압축 파일이 성공적으로 생성되었습니다.")
        time.sleep(3)
        os.remove(source_path)
        time.sleep(3)
        
    except Exception as e:
        print(f"압축 파일 생성 중 오류 발생: {e}")








    # 아래 2개만 오류남 이유를 찾는중

    # td = tr[13].find_elements(By.CSS_SELECTOR, "td")
    # #비용부과유무
    # td_23 = td[0]
    # #비용부과기준 및 단위
    # td_24 = td[1]
    # print(f"비용부과유무:{td_23.text}, 비용부과기준 및 단위:{td_24.text}")

    # #이용허락범위
    # td_25 = tr[14].find_element(By.CSS_SELECTOR, "td")
    # print(f"이용허락범위:{td_25.text}")

def insert_detail_page(file_name, classification_system, providing_agency, department_name, 
                department_phone_number, legal_basis, collection_method, update_period, 
                next_registration_date, media_type, total_rows, extension, keywords, 
                cumulative_downloads, downloads, registration_date, modification_date, 
                data_limit, provision_form, description, other_notes):
    #file_path = f'C:\\Users\\USER\\Downloads\\{file_name}', file_path = f'C:\\Users\\PC\\Downloads\\{file_name}'
    file_path = f'C:\\Users\\PC\\Downloads\\{file_name}.zip'
    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()
    except FileNotFoundError:
        print("다운로드한 파일이 없습니다.")
        file_data = ''
    with connection, connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO public.detail (
                    file_name, classification_system, providing_agency, department_name, 
                    department_phone_number, legal_basis, collection_method, update_period, 
                    next_registration_date, media_type, total_rows, extension, keywords, 
                    cumulative_downloads, downloads, registration_date, modification_date, 
                    data_limit, provision_form, description, other_notes, file
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                ) RETURNING id
            """, (file_name, classification_system, providing_agency, department_name, 
                    department_phone_number, legal_basis, collection_method, update_period, 
                    next_registration_date, media_type, total_rows, extension, keywords, 
                    cumulative_downloads, downloads, registration_date, modification_date, 
                    data_limit, provision_form, description, other_notes, file_data))
        connection.commit()
        detail_pk_id = cursor.fetchone()[0]
        return detail_pk_id

   
def insert_main_page(title, content, provider, date, view, download, periodic_data, keywords_str):
    with connection, connection.cursor() as cursor:
        cursor.execute("INSERT INTO public.main (title, content, provider, date, view, download, periodic_data, keywords_str) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id", (title, content, provider, date, view, download, periodic_data, keywords_str))
        connection.commit()
        main_pk_id = cursor.fetchone()[0]
        return main_pk_id
    
def insert_main_detail_relation(main_id, detail_id):
    with connection, connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO public.main_detail_relation (main_id, detail_id)
            VALUES (%s, %s)
        """, (main_id, detail_id))
        connection.commit()


# 메인페이지 크롤링
def page_crawling():
    result_list = driver.find_elements(By.CSS_SELECTOR, ".result-list > ul > li")

    for result in result_list:
        title = result.find_element(By.CSS_SELECTOR, ".title")
        content = result.find_element(By.CSS_SELECTOR, ".ellipsis.publicDataDesc")
    
        # .info-data
        div = result.find_elements(By.CSS_SELECTOR, "div")
        info_data = div[0]
        p = info_data.find_elements(By.CSS_SELECTOR, "p")
        data = p[0]
        span = data.find_elements(By.CSS_SELECTOR, "span")
        # 제공 기간
        provider = span[1].text


        # .info-data
        div = result.find_elements(By.CSS_SELECTOR, "div")
        info_data = div[0]
        p = info_data.find_elements(By.CSS_SELECTOR, "p")
        data = p[1]
        span = data.find_elements(By.CSS_SELECTOR, "span")
        # 수정일
        date = span[1].text

        # .info-data
        div = result.find_elements(By.CSS_SELECTOR, "div")
        info_data = div[0]
        p = info_data.find_elements(By.CSS_SELECTOR, "p")
        data = p[2]
        span = data.find_elements(By.CSS_SELECTOR, "span")
        # 조회수
        view = span[1].text

         # .info-data
        div = result.find_elements(By.CSS_SELECTOR, "div")
        info_data = div[0]
        p = info_data.find_elements(By.CSS_SELECTOR, "p")
        data = p[3]
        span = data.find_elements(By.CSS_SELECTOR, "span")
        # 다운로드
        download = span[1].text

        
        # 주기성 데이터  비어있으면 ""
        try:
            periodic_data_elem = info_data.find_element(By.XPATH, './/p[span[@class="tit" and text()="주기성 데이터"]]/span[@class="data"]')
            periodic_data = periodic_data_elem.text
        except NoSuchElementException:
            periodic_data = ""
        
        print(f"주기성 데이터: {periodic_data}")



        # 키워드: 기온,강수량,일조량  형식
        keyword_elem = info_data.find_element(By.XPATH, './/p[span[@class="tit" and text()="키워드"]]')
        keywords = keyword_elem.text.split(",")
        keywords = [keyword.strip().replace('키워드', '') for keyword in keywords]
        keywords_str = ", ".join(keywords)
        print(f"키워드: {keywords_str}")


        #print(f"title: {title.text}, content: {content.text}, 제공기간: {provider}, 수정일: {date}, 조회수: {view}, 다운로드: {download} ")

        time.sleep(1)
        main_pk_id = insert_main_page(title.text, content.text, provider, date, view, download, periodic_data, keywords_str)
        time.sleep(1)
        

        # 상세 페이지 부분
        title.click()
        time.sleep(2)
        #나중에 if 로 파일데이터, 오픈API 선택해서 상세페이지 크롤링 
        detail_pk = file_data_detail_page_crawling()
        insert_main_detail_relation(main_pk_id, detail_pk)
        driver.back()
        time.sleep(2)
    
    

for page_num in range(1, pages + 1):
    page_nav = driver.find_element(By.CSS_SELECTOR, ".pagination")
    action = ActionChains(driver)
    action.move_to_element(page_nav).perform()
    page_click = page_nav.find_element(By.XPATH, f'//*[text()="{page_num}"]')
    page_click.click()
    time.sleep(5)
    page_crawling()
    





time.sleep(2)
driver.quit() 
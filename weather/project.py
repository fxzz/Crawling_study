import logging
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
import os
from selenium.webdriver.support.ui import WebDriverWait
from detail_page_class import DetailPage
from weather_insert import insert_main_page, insert_detail_page, insert_main_detail_relation
from threading import Thread
from download_file_and_compress import download_and_zip_file

## 오류 모음

##압축은 스레드로, json 데이터를 처음에 받아서 저장 ?해 태그를 어드민에서 동적으로
#https://velog.io/@helloaltjs/Window-JEUS-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0



options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"]) # 크롬 상단에 테스트 메세지 안뜨게

options.add_argument("--start-maximized") #화면 최대 사이즈
options.add_experimental_option("detach", True) #화면 안꺼지게
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)

url = "https://www.data.go.kr/tcs/dss/selectDataSetList.do?keyword=날씨"

driver.get(url)

# 로깅 설정 : 자세하게 찾아보기
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    handlers=[logging.FileHandler('example.log'),
                              logging.StreamHandler()])


download_file_folder = 'C:\\Users\\USER\\Downloads\\'



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

    #파일데이터명
    file_data_name = tbody.find_element(By.XPATH, '//th[text()="파일데이터명"]/following-sibling::td').get_attribute("innerText")
    print(f"파일데이터명:{file_data_name}")
    

    #분류체계
    classification_system = tbody.find_element(By.XPATH, '//th[text()="분류체계"]/following-sibling::td').text
    print(f"분류체계:{classification_system}")
    
    #제공기관
    providing_agency = driver.find_element(By.XPATH, '//th[text()="제공기관"]/following-sibling::td/a').text
    print(f"제공기관:{providing_agency}")


    #관리부서명
    department_name = tbody.find_element(By.XPATH, '//th[text()="관리부서명"]/following-sibling::td').text
    print(f"분류체계:{department_name}")

    # 관리부서 전화번호
    department_phone_number = tbody.find_element(By.XPATH, '//th[text()="관리부서 전화번호"]/following-sibling::td').text
    print(f'관리부서 전화번호: {department_phone_number}')

    # 보유근거
    basis_of_possession = tbody.find_element(By.XPATH, '//th[text()="보유근거"]/following-sibling::td').text
    print(f'보유근거: {basis_of_possession}')

    # 수집방법
    collection_method = tbody.find_element(By.XPATH, '//th[text()="수집방법"]/following-sibling::td').text
    print(f'수집방법: {collection_method}')

    # 업데이트 주기
    update_period = tbody.find_element(By.XPATH, '//th[text()="업데이트 주기"]/following-sibling::td').text
    print(f'업데이트 주기: {update_period}')

    # 차기 등록 예정일
    next_registration_date = tbody.find_element(By.XPATH, '//th[text()="차기 등록 예정일"]/following-sibling::td').text
    print(f'차기 등록 예정일: {next_registration_date}')

    # 매체 유형
    media_type = tbody.find_element(By.XPATH, '//th[text()="매체유형"]/following-sibling::td').text
    print(f'매체 유형: {media_type}')

    # 전체 행
    total_rows = tbody.find_element(By.XPATH, '//th[text()="전체 행"]/following-sibling::td').text
    print(f'전체 행: {total_rows}')

    # 확장자
    extension = tbody.find_element(By.XPATH, '//th[text()="확장자"]/following-sibling::td').text
    print(f'확장자: {extension}')

    # 키워드
    keywords = tbody.find_element(By.XPATH, '//th[text()="키워드"]/following-sibling::td').text
    print(f'키워드: {keywords}')

    # 누적 다운로드(바로가기)
    try:
        cumulative_downloads_element = tbody.find_element(By.XPATH, '//th[contains(text(), "누적 다운로드(바로가기)")]/following-sibling::td')
        cumulative_downloads = cumulative_downloads_element.text
        print(f'누적 다운로드(바로가기): {cumulative_downloads}')
    except NoSuchElementException as e:
        logging.info(f'{e}')
        cumulative_downloads = ""
        
    # 데이터 한계
    try:
        data_limit_element = tbody.find_element(By.XPATH, '//th[text()="데이터 한계"]/following-sibling::td')
        data_limit = data_limit_element.text
        print(f'데이터 한계: {data_limit}')
    except NoSuchElementException as e:
        logging.info(f'{e}')
        data_limit = ""

    # 다운로드(바로가기)
    download_shortcut = tbody.find_element(By.XPATH, '//th[text()="다운로드(바로가기)"]/following-sibling::td').text
    print(f'다운로드(바로가기): {download_shortcut}')
    

    # 등록일
    registration_date = tbody.find_element(By.XPATH, '//th[text()="등록일"]/following-sibling::td').text
    print(f'등록일: {registration_date}')

    # 수정일
    modification_date = tbody.find_element(By.XPATH, '//th[text()="수정일"]/following-sibling::td').text
    print(f'수정일: {modification_date}')

    #제공형태
    provided_form = tbody.find_element(By.XPATH, '//th[text()="제공형태"]/following-sibling::td').text
    print(f'제공형태: {provided_form}')

    #설명
    description = tbody.find_element(By.XPATH, '//th[text()="설명"]/following-sibling::td').text
    print(f'설명: {description}')

    # URL
    try:
        url_element = tbody.find_element(By.XPATH, '//th[text()="URL"]/following-sibling::td')
        url = url_element.text
        print(f'URL: {url}')
    except NoSuchElementException as e:
        logging.info(f'{e}')
        url = ""

    #기타 유의사항
    other_notes = tbody.find_element(By.XPATH, '//th[text()="기타 유의사항"]/following-sibling::td').text
    print(f'기타 유의사항: {other_notes}')

    # 비용부과유무
    cost_assessment = tbody.find_element(By.XPATH, '//th[text()="비용부과유무"]/following-sibling::td').text
    print(f'비용부과유무: {cost_assessment}')

    # 비용부과기준 및 단위
    cost_basis_and_unit = tbody.find_element(By.XPATH, '//th[text()="비용부과기준 및 단위"]/following-sibling::td').text
    print(f'비용부과기준 및 단위: {cost_basis_and_unit}')

    # 이용허락범위
    usage_permission_range = tbody.find_element(By.XPATH, '//th[text()="이용허락범위"]/following-sibling::td').text
    print(f'이용허락범위: {usage_permission_range}')

    
    
    detail_page_obj = DetailPage(
    file_data_name,                 # 파일명
    classification_system,          # 분류체계
    providing_agency,               # 제공기관
    department_name,                # 관리부서명
    department_phone_number,        # 관리부서 전화번호
    basis_of_possession,            # 보유근거
    collection_method,              # 수집방법
    update_period,                  # 업데이트 주기
    next_registration_date,         # 차기 등록 예정일
    media_type,                     # 매체유형
    total_rows,                     # 전체 행
    extension,                      # 확장자
    keywords,                       # 키워드
    cumulative_downloads,           # 누적 다운로드
    download_shortcut,              # 다운로드
    registration_date,              # 등록일
    modification_date,              # 수정일
    data_limit,                     # 데이터 한계
    provided_form,                  # 제공형태
    description,                    # 설명
    url,                            # URL
    other_notes,                    # 기타 유의사항
    cost_assessment,                # 비용부과유무
    cost_basis_and_unit,            # 비용부과기준 및 단위
    usage_permission_range          # 이용허락범위
    )

    detail_pk = insert_detail_page(detail_page_obj)
    return detail_pk



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
        except NoSuchElementException as e:
            logging.info(f"{e}")
            periodic_data = ""
        
        print(f"주기성 데이터: {periodic_data}")



        # 키워드: 기온,강수량,일조량  형식
        keyword_elem = info_data.find_element(By.XPATH, './/p[span[@class="tit" and text()="키워드"]]')
        keywords = keyword_elem.text.split(",")
        keywords = [keyword.strip().replace('키워드', '') for keyword in keywords]
        keywords_str = ", ".join(keywords)
        print(f"키워드: {keywords_str}")

        time.sleep(1)
        main_pk_id = insert_main_page(title.text, content.text, provider, date, view, download, periodic_data, keywords_str)
        time.sleep(1)
        
        # 상세 페이지 부분
        title.click()
        time.sleep(2)
        download_and_zip_file(download_file_folder, driver)
        #나중에 if 로 파일데이터, 오픈API 선택해서 상세페이지 크롤링 
        detail_pk = file_data_detail_page_crawling()
        insert_main_detail_relation(main_pk_id, detail_pk)
        driver.back()
        time.sleep(2)
    
    

for page_num in range(1, pages + 1):
    page_nav = driver.find_element(By.CSS_SELECTOR, ".pagination")
    action = ActionChains(driver)
    action.move_to_element(page_nav).perform()
    if page_num % 10 == 0:
        next_page_link = driver.find_element(By.XPATH, '//a[text()="다음 페이지"]')
        next_page_link.click()
    page_click = page_nav.find_element(By.XPATH, f'//*[text()="{page_num}"]')
    page_click.click()
    time.sleep(5)
    page_crawling()
    





time.sleep(600) ##th1.join() 을 안쓰고 기다림
driver.quit() 

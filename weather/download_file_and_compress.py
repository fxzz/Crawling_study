import logging
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
import zipfile
import os
from threading import Thread

def download_and_zip_file(download_file_folder, driver):
    tbody = driver.find_element(By.CSS_SELECTOR, ".file-meta-table-pc > table > tbody")
    file_data_name = tbody.find_element(By.XPATH, '//th[text()="파일데이터명"]/following-sibling::td').get_attribute("innerText")
    file_name = file_data_name + ".csv" 
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
           except NoAlertPresentException as e:
                logging.info(f'{e}, alert가 나타나지 않았습니다.' )

           
           # 나중에 다운로드가 제대로 완료되면 다음으로 가지게 바꿔야함
           #create_zip_file(download_file_folder, file_name)
           th1 = Thread(target=create_zip_file, args=(download_file_folder, file_name))     
           th1.start()
           #th1.join()
        
    except NoSuchElementException as e:
        logging.debug(f"{e}, alert가 나타나지 않았습니다.")

# 스레드로 수정해야함
def create_zip_file(target_folder, file_name):
    time.sleep(7)
    file_name_without_extension = os.path.splitext(file_name)[0]
    source_path = os.path.join(target_folder, file_name)
    zip_path = os.path.join(target_folder, file_name_without_extension + ".zip")
    time.sleep(3)
    try:
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            zipf.write(source_path, arcname=file_name)
        logging.info("압축 파일이 성공적으로 생성되었습니다.")
        time.sleep(3)
        os.remove(source_path)
        time.sleep(3)
        
    except Exception as e:
        logging.info(f"{e}, 압축 파일 생성 중 오류 발생.")

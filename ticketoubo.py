import time
import datetime
from datetime import datetime
import schedule
import sched
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchWindowException
import chromedriver_binary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#プログラム起動
def process():
    # ブラウザ開始
    driver = webdriver.Chrome("{Place of ChromeDriver}")
    driver.get('https://shop.columbia.jp/shop/g/gS2763/')

    WebDriverWait(driver, 1000000).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn_cart_l_')))
    driver.find_element_by_class_name('btn_cart_l_').click()
    WebDriverWait(driver, 1000000).until(EC.presence_of_element_located((By.CLASS_NAME, 'order_btn_')))
    driver.find_element_by_class_name('order_btn_').click()
    WebDriverWait(driver, 1000000).until(EC.presence_of_element_located((By.CLASS_NAME, 'login_uid_mail_')))
    driver.find_element_by_class_name("login_uid_mail_").send_keys("{YOUR_USERNAME}")
    WebDriverWait(driver, 1000000).until(EC.presence_of_element_located((By.CLASS_NAME, 'login_pwd_')))
    driver.find_element_by_class_name("login_pwd_").send_keys("{YOUR_PASSWORD}")
    WebDriverWait(driver, 1000000).until(EC.presence_of_element_located((By.CLASS_NAME, 'inputimage_')))
    driver.find_element_by_class_name('inputimage_').click()
    #WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'method_box_content_')))
    driver.find_element_by_id('method_r7').click()
    time.sleep(5)
    WebDriverWait(driver, 1000000).until(EC.presence_of_element_located((By.CLASS_NAME, 'button_')))
    driver.find_element_by_name('submit').click()
    WebDriverWait(driver, 1000000).until(EC.presence_of_element_located((By.CLASS_NAME, 'submit_')))
    driver.find_element_by_class_name('submit_').click()
    #WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, 'inputimage_')))
    #driver.find_element_by_class_name('submit_').click()

scheduler = sched.scheduler(time.time, time.sleep)

#スクレイピング開始時間
run_at = datetime.strptime('{実行する時間}', '%Y-%m-%d %H:%M:%S')
run_at = int(time.mktime(run_at.utctimetuple()))

#イベントをスケジュール
scheduler.enterabs(run_at, 1, process)
scheduler.run()


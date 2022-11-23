import math
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element(By.ID,'price'))
    button = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID,'price'),'$100'))
    browser.find_element(By.CLASS_NAME,"btn.btn-primary").click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element(By.ID,'solve'))
    num = browser.find_element(By.ID,'input_value').text
    browser.find_element(By.ID,"answer").send_keys(calc(num))
    browser.find_element(By.ID,'solve').click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
# from PIL import Image
# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = 'c://Program Files (x86)/Tesseract-OCR/tesseract.exe'
# text = pytesseract.image_to_string(Image.open('./Picture/test.jpg'))
# print(text)
import os, re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, NoSuchFrameException, TimeoutException
import time, re


def windows_compatible_string(original_string):
    forbidden_chars = r'[<>:\"\/\\|?*]'
    windows_compatible_string = re.sub(forbidden_chars, '_', original_string)
    return windows_compatible_string


# 设置 ChromeDriver 的路径
webdriver_service = Service('.//Picture/chromedriver.exe')
# 设置 Chrome 浏览器的选项
chrome_options = Options()
chrome_options.add_argument('--headless')  # 无头模式，不显示浏览器窗口
# 创建 ChromeDriver 实例
driver = webdriver.Chrome(service=webdriver_service,options=chrome_options)
driver.set_window_size(1200, 960)

for i in range(5000, 13000):

    url = 'https://www.addgene.org/browse/sequence_vdb/' + str(i)
    # driver.set_page_load_timeout(10)
    # try:
    #     driver.get(url)
    # except TimeoutException:
    #     driver.refresh()
    driver.get(url)
    time.sleep(1.5)
    try:
        sequence_title = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[2]/h1').text
        time.sleep(0.2)
        driver.switch_to.frame('giraffe-analyze-frame')
        time.sleep(0.2)
        # driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/ul/li[2]/a').click()
        # time.sleep(0.1)
        # driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/p[2]/a[2]').click()
        # time.sleep(0.1)
        sequence_data = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[2]/textarea').get_attribute('value')
        # print(sequence_title)
        # print(sequence_data)
        file_name = re.search(r":\s*(.*)", sequence_title).group(1)
        file_path = ".//sequence_file_5000-13000/" + windows_compatible_string(file_name) + "-" + (str(i))+ ".txt"
        with open(file_path, "w",encoding='utf-8') as file:
            # file.write(sequence_title + "\n")
            file.write(sequence_data)
        print("找到基因序列信息: " + str(i) + "  " + sequence_title)
        # driver.save_screenshot(".//sequence_file_2/" + str(i) + ".png")
    except NoSuchElementException as e:
        print("未找到基因序列信息: " + str(i))
        time.sleep(0.3)
        driver.save_screenshot(".//sequence_file_5000-13000/" + str(i) + ".png")
    except NoSuchFrameException as e:
        print("未找到基因序列信息: " + str(i))
        time.sleep(0.3)
        driver.save_screenshot(".//sequence_file_5000-13000/" + str(i) + ".png")
    finally:
        # driver.save_screenshot(".//sequence_file_2/" + str(i) + ".png")
        # driver.quit()
        continue
driver.quit()






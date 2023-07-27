from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, NoSuchFrameException, TimeoutException
from datetime import datetime
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
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
driver.set_window_size(1200, 960)
current_Time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for i in range(5000, 9000):

    url = 'https://www.addgene.org/browse/sequence_vdb/' + str(i)
    # driver.set_page_load_timeout(10)
    # try:
    #     driver.get(url)
    # except TimeoutException:
    #     driver.refresh()
    driver.get(url)
    files_path = ".//testfile_5000,9000/"
    # time.sleep(1.5)
    try:
        # time.sleep(0.5)
        se_title = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div[2]/h1')))
        sequence_title = se_title.text
        # sequence_title = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[2]/h1').text
        # time.sleep(0.2)
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, 'giraffe-analyze-frame')))
        driver.switch_to.frame('giraffe-analyze-frame')
        # time.sleep(0.2)
        # driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/ul/li[2]/a').click()
        # time.sleep(0.1)
        # driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/p[2]/a[2]').click()
        # time.sleep(0.1)
        # sequence_data = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[2]/textarea').get_attribute('value')
        se_data = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[2]/textarea')))
        sequence_data = se_data.get_attribute('value')
        # print(sequence_title)
        # print(sequence_data)
        file_name = re.search(r":\s*(.*)", sequence_title).group(1)
        file_path = files_path + windows_compatible_string(file_name) + "-" + (str(i)) + ".txt"
        with open(file_path, "w", encoding='utf-8') as file:
            # file.write(sequence_title + "\n")
            file.write(sequence_data)
        print(datetime.now().strftime("%m-%d %H:%M:%S") + ": " + "找到基因序列信息: " + str(i) + "  " + sequence_title)
        # driver.save_screenshot(".//sequence_file_2/" + str(i) + ".png")
    except Exception as e:
        print(datetime.now().strftime("%m-%d %H:%M:%S") + ": " + "未找到基因序列信息: " + str(i))
        time.sleep(1)
        driver.save_screenshot(files_path + str(i) + ".png")
    except TimeoutException as e:
        print(datetime.now().strftime("%m-%d %H:%M:%S") + ": " + "未找到基因序列信息: " + str(i))
        time.sleep(1)
        driver.save_screenshot(files_path + str(i) + ".png")
    finally:
        # driver.save_screenshot(".//sequence_file_2/" + str(i) + ".png")
        # driver.quit()
        continue
driver.quit()

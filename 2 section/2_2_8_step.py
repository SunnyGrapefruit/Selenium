from selenium import webdriver
import time
import os

options = webdriver.ChromeOptions()
chrome_driver_binary = 'C:\chromedriver\chromedriver.exe'

time.sleep(5)
link = "http://suninjuly.github.io/file_input.html"


try:

    browser = webdriver.Chrome(chrome_driver_binary)
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))

    browser.find_element_by_name("firstname").send_keys("Иван")
    browser.find_element_by_name("lastname").send_keys("Петров")
    browser.find_element_by_name("email").send_keys("fgfhgf@gh.hj")

    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    browser.find_element_by_id('file').send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(5)
    browser.quit()
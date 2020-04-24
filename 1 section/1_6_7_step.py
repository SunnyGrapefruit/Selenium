from selenium import webdriver
import time

options = webdriver.ChromeOptions()
chrome_driver_binary = 'C:\chromedriver\chromedriver.exe'

# driver = webdriver.Chrome(chrome_driver_binary)
time.sleep(5)
link = "http://suninjuly.github.io/huge_form.html"

try:

    browser = webdriver.Chrome(chrome_driver_binary)

    browser.get(link)
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

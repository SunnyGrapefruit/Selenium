from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

options = webdriver.ChromeOptions()
chrome_driver_binary = 'C:\chromedriver\chromedriver.exe'

time.sleep(5)
link = "http://suninjuly.github.io/selects1.html"


try:

    browser = webdriver.Chrome(chrome_driver_binary)
    browser.get(link)

    x_element = browser.find_element_by_id("num1").text
    y_element = browser.find_element_by_id("num2").text

    z = int(x_element)+ int(y_element)

    browser.find_element_by_tag_name("select").click()

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(z))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
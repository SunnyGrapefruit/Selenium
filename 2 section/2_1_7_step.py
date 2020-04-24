from selenium import webdriver
import time
import math

options = webdriver.ChromeOptions()
chrome_driver_binary = 'C:\chromedriver\chromedriver.exe'

time.sleep(5)
link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome(chrome_driver_binary)
    browser.get(link)

    x_element = browser.find_element_by_id("treasure").get_attribute("valuex")
    y = calc(x_element)

    browser.find_element_by_id("answer").send_keys(y)

    browser.find_element_by_css_selector("#robotCheckbox").click()
    browser.find_element_by_css_selector("#robotsRule").click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
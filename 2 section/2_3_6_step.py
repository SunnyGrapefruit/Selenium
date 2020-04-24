from selenium import webdriver
import time
import math

options = webdriver.ChromeOptions()
chrome_driver_binary = 'C:\chromedriver\chromedriver.exe'

time.sleep(5)
link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome(chrome_driver_binary)
    browser.get(link)

    browser.find_element_by_css_selector("button.btn").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
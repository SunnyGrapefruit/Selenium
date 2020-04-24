from selenium import webdriver
import time
import math

options = webdriver.ChromeOptions()
chrome_driver_binary = 'C:\chromedriver\chromedriver.exe'

time.sleep(5)
link = "http://SunInJuly.github.io/execute_script.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome(chrome_driver_binary)
    browser.get(link)

    x_element = browser.find_element_by_id("input_value").text
    y = calc(x_element)

    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_css_selector("#robotCheckbox").click()
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element_by_css_selector("#robotsRule").click()

    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("window.scrollBy(0, 100);")
    # browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", button)
    button.click()


finally:
    time.sleep(5)
    browser.quit()
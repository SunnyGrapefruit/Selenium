from selenium import webdriver
import time

options = webdriver.ChromeOptions()
chrome_driver_binary = 'C:\chromedriver\chromedriver.exe'

# driver = webdriver.Chrome(chrome_driver_binary)
time.sleep(5)
link = "http://suninjuly.github.io/registration2.html"

try:

    browser = webdriver.Chrome(chrome_driver_binary)
    browser.get(link)

    input1 = browser.find_element_by_css_selector(".first_block .form-control.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(".first_block .form-control.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector(".first_block .form-control.third")
    input3.send_keys("Smolensk")
    # input4 = browser.find_element_by_css_selector(".second_block .form-control.first")
    # input4.send_keys("Russia")
    # input5 = browser.find_element_by_css_selector(".second_block .form-control.second")
    # input5.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()
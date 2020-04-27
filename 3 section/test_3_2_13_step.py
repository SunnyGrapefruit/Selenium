from selenium import webdriver
import time
import unittest

options = webdriver.ChromeOptions()
chrome_driver_binary = 'C:\chromedriver\chromedriver.exe'

time.sleep(5)

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        browser = webdriver.Chrome(chrome_driver_binary)
        browser.get(link1)
        input1 = browser.find_element_by_css_selector(".first_block .form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block .form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".first_block .form-control.third")
        input3.send_keys("Smolensk")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        time.sleep(10)
        browser.quit()

    def test_abs2(self):
        browser = webdriver.Chrome(chrome_driver_binary)
        browser.get(link2)
        input1 = browser.find_element_by_css_selector(".first_block .form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block .form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".first_block .form-control.third")
        input3.send_keys("Smolensk")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        time.sleep(10)
        browser.quit()


if __name__ == "__main__":
    unittest.main()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pytest

options = webdriver.ChromeOptions()
chrome_driver_binary = 'C:\chromedriver\chromedriver.exe'

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(chrome_driver_binary)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('links', ["236895/step/1", "236896/step/1", "236897/step/1", "236898/step/1", "236899/step/1", "236903/step/1", "236904/step/1", "236905/step/1"])
class TestAbs(object):
    def test_time_input(self, browser, links):

        link = f"https://stepik.org/lesson/{links}/"
        browser.get(link)

        textArea = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
        )

        answer = math.log(int(time.time()))
        a = str(answer)
        textArea.send_keys(a)
        button = browser.find_element_by_class_name("submit-submission")
        button.click()

        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
        )

        correctText = browser.find_element_by_class_name("smart-hints__feedback").text

        assert correctText == "Correct!"

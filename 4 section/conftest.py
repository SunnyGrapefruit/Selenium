import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language browser: ru or other")


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    # browser_name = request.config.getoption("browser_name")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    browser = webdriver.Chrome(options=options)

    # if browser_name == "chrome":
    #     print("\nstart chrome browser for test..")
    #     options = Options()
    #     options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    #     browser = webdriver.Chrome(options=options, executable_path='C:\chromedriver\chromedriver.exe')
    #
    # elif browser_name == "firefox":
    #     print("\nstart firefox browser for test..")
    #     fp = webdriver.FirefoxProfile()
    #     fp.set_preference("intl.accept_languages", browser_language)
    #     browser = webdriver.Firefox(firefox_profile=fp)
    # else:
    #     raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()
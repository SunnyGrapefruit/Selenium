import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# def pytest_addoption(parser):
#     parser.addoption('--language', action='store', default=None,
#                      help="Choose language: ru, en, fr or es")


# @pytest.fixture(scope="function")
# def browser(request):
#
#     user_language = request.config.getoption("language")
#     options = Options()
#     options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
#
#     if user_language == "ru":
#         print("\nstart browser for ru-test..")
#         browser = webdriver.Chrome(options=options, executable_path='C:\chromedriver\chromedriver.exe')
#     elif user_language == "en":
#         print("\nstart browser for en-test..")
#         browser = webdriver.Chrome(options=options, executable_path='C:\chromedriver\chromedriver.exe')
#     else:
#         raise pytest.UsageError("--language should be ru or en")
#
#     yield browser
#     print("\nquit browser..")
#     browser.quit()


@pytest.fixture(scope="function")
def browser(request):

    browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
    yield browser
    print("\nquit browser..")
    browser.quit()
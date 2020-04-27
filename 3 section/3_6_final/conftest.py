import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en, fr or es")


@pytest.fixture(scope="function")
def browser(request):

    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    if user_language == "ru":
        print("\nstart browser for ru-test..")
        browser = webdriver.Chrome(options=options)
    elif user_language == "en":
        print("\nstart browser for en-test..")
        browser = webdriver.Chrome(options=options)

    elif user_language == "es":
        print("\nstart browser for es-test..")
        browser = webdriver.Chrome(options=options)

    elif user_language == "fr":
        print("\nstart browser for fr-test..")
        browser = webdriver.Chrome(options=options)

    else:
        raise pytest.UsageError("--language should be ru, en, fr or es")

    yield browser
    print("\nquit browser..")
    browser.quit()
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru, en, ...ect.")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print(f"\nstart {browser_name} browser in {user_language}-language  for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = FirefoxOptions()
        fp.set_preference("intl.accept_languages", user_language)
        print(f"\nstart {browser_name} browser in {user_language}-language for test..")
        browser = webdriver.Firefox(options=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print(f"\nquit {browser_name} browser in {user_language}-language..")
    browser.quit()

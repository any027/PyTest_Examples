import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    #Need to put Chromedriver on system path?
    browser = webdriver.Chrome()
    #This wait will help us for race conditions.
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


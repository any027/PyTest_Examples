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

@pytest.fixture
def cbt_config(scope ="session"):

    #Read our config file
    with open('cbt_config.json') as config_file:
        config = json.load(config_file)

    #verify our config, we want to make sure that our json file was parsed properly and that they look good.
    assert 'authentication' in config
    assert 'username' in config['authentication']
    assert 'key' in config['authentication']
    assert 'webdriver' in config
    assert 'name' in config['webdriver']
    assert 'browserName' in config['webdriver']
    assert 'platform' in config['webdriver']

    return config
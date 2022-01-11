from time import sleep

import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def driver():
    # SETUP - steps to do before <scope>'
    print('\n############ I am a SETUP ###########')
    print('initializing the browser....')
    opts = Options()
    opts.add_argument('--disable-notification--')
    # options.add_argument ('-headless') running the Chrome on the background
    # 1. open the browser
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    sleep(5)
    print('closing the browser...')
    driver.quit()
    print('Test cases ar enow complete')





from selenium import webdriver
from time import sleep
import time
from select import select
from unittest import result
import pytest
from time import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
# VARIABLES:
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    """base blass for all other pages, includes common selenium operations"""

    def __init__(self, driver):
        self.driver = driver
        self.wdwait = WebDriveWait(self.driver)

    def click_element_by_locator(self, locator, method='xpath', wait_time=10):
        try:
            element = object # very general data type
            if method == 'xpath':
                element = wdwait.until(EC.presence_of_element_located((By.XPATH, locator)))
            elif method == 'id':
                element = wdwait.until(EC.presence_of_element_located((By.ID, locator)))
            elif method == 'css':
                element = wdwait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
            element.click()
        except (NoSuchElementException, TimeoutException) as err:
            print('Error on click element by xpath, check xpath.', locator)
            print(err)




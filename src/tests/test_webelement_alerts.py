import time
from select import select
from unittest import result
import pytest
from time import *
from selenium import webdriver
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# VARIABLES:
from selenium.webdriver.support.select import Select
HOST = 'https://courses.letskodeit.com/practice'
name_input_xpath = "//input[@name='enter-name']"
name = 'Joe Doe'
filepath = '../../screenshots/'

# STEPS:
# 1. open the browser
from selenium.webdriver.remote import webelement


# 2. open the automationpractice.com
# driver.get('https://www.thelevelupsolutions.com/')
# driver.get('https://www.google.com')
# driver.get('https://courses.letskodeit.com/practice')
# print('Opening the page...')
# driver.get(HOST)

@pytest.mark.alert1
def test_js_alert_single_button(driver):
      print('Opening the page...')
      driver.get(HOST)
      # enter name
      print('testing the alert button...')
      name_input = driver.find_element(By.XPATH, name_input_xpath)
      name_input.send_keys(name)
      # click on alert
      driver.find_element(By.ID, 'alertbtn').click()
      # switch to alert
      alert = driver.switch_to.alert
      # get the text
      print('Alert text:', alert.text)
      # click OK on alert
      sleep(5)
      alert.accept()
      print('####### accepted the alert #######')
      sleep(5)

def test_alert_multiple_button(driver):
      print('Opening the page...')
      driver.get(HOST)
      # enter name
      print('')
      name_input = driver.find_element(By.XPATH, name_input_xpath)
      name_input.send_keys(name)
      # click on Confirm
      driver.find_element(By.ID, 'confirmbtn').click()
      # switch to alert
      alert2 = driver.switch_to.alert
      sleep(5)
      # get the text
      print('Alert text:', alert2.text)
      # click Cancel
      alert2.dismiss()
      print('####### cancel the alert #######')


import time
from unittest import result

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# filepath = 'C:\dev\SeleniumProject\screenshots/'
filepath = '../../screenshots/'
# 1. open the browser
from selenium.webdriver.remote import webelement

driver = webdriver.Chrome()
driver.implicitly_wait(20)  # synchronizing the browser
# synchronizing the browser
# driver.maximize_window()
driver.minimize_window()
# 2. open the automationpractice.com
driver.get('http://automationpractice.com/index.php')
search_box = driver.find_element(By.XPATH, "//input[@id='search_query_top']")
search_box.send_keys('dress' + Keys.ENTER)

url = driver.current_url
print('current url: ', url)
browser_name = driver.name
win_name = driver.current_window_handle
title = driver.title
win_names = driver.window_handles

print(win_name)
print(browser_name)
print(title)
print(win_names)
driver.save_screenshot(filepath + 'screenshot1.png')

print('############### web driver methods #############')
driver.back()
time.sleep(1)
print('current url: ', driver.current_url)
driver.save_screenshot(filepath + 'screenshot2.png')

driver.forward()
print('current url: ', driver.current_url)
time.sleep(2)
driver.refresh()
time.sleep(1)
driver.save_screenshot(filepath + 'screenshot3.png')

print('#################switch to window_name##############')
products = driver.find_elements(By.XPATH, "//div[@id='center_column']//a[@class='product-name']")
products[0].click()
time.sleep(5)
driver.save_screenshot(filepath + 'screenshot4.png')


fb_btn_xpath = "//button[@class='btn btn-default btn-facebook']"
driver.find_element(By.XPATH, fb_btn_xpath).click()
win_names = driver.window_handles
print(win_names)
print(driver.title)
time.sleep(2)

driver.switch_to.window(win_names[-1])
driver.save_screenshot(filepath + 'screenshotFB.png')

driver.find_element(By.ID, 'email').send_keys('myemail@gmail.com')
driver.find_element(By.NAME, 'pass').send_keys('myNewPassword333')
time.sleep(5)
driver.save_screenshot(filepath + 'screenshot5.png')
driver.close()
driver.quit()
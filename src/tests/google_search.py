from unittest import result

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1. open the browser
from selenium.webdriver.remote import webelement

driver = webdriver.Chrome()
driver.implicitly_wait(20)  # s
# synchronizing the browser
# driver.maximize_window()

# 2. open the google.com
# driver.get('https://www.thelevelupsolutions.com/')
driver.get('https://www.google.com')
# 3.search for 'selenium'
# driver.find_element_by_id() fastest way of finding element from html document
# search_box = driver.find_element_by_name('q')
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('selenium')  # entering the text in the input (text) form
search_box.send_keys(Keys.ENTER)
# driver.find_element_by_xpath() # technic, build
# driver.find_element_by_css_selector() # technics, build
# driver.find_element_by_link_text()
# driver.find_element_by_class_name() # class name might be
# driver.find_element_by_partial_link_text()
# driver.find_element_by_tag_name()
# # 4. capture the result text
result_msg = driver.find_element(By.ID, 'result-stats').text
# result_msg = driver.find_element_by_id('result-stats').text - obsolete model for find_element

print('I got the result here: ', result_msg)

# 5. close the browser
driver.quit()
# driver.close()
# driver.quit()
# webdriver
# webelement

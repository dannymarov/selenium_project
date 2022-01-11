import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1. open the browser
from selenium.webdriver.remote import webelement

driver = webdriver.Chrome()
driver.implicitly_wait(20)  # s
# synchronizing the browser
driver.maximize_window()

# 2. open the automationpractice.com demo website
# driver.get('https://www.thelevelupsolutions.com/')
driver.get('http://automationpractice.com/index.php')
search_box = driver.find_element(By.XPATH, "//input[@id='search_query_top']")
search_box.send_keys('dress' + Keys.ENTER)
# the same way can be written like
# search_box.send_keys('dress')
# search_box.send_keys(Keys.ENTER)

# XPATH SELECTOR:
# //ul[@id='homefeatured']//a[@class='product-name' and @title='Blouse']
# //ul[@id='homefeatured']
# //a[@title='Women'] - search using attributes in the xpath
# //a[text()='Women'] - search using text of the element in your xpath
# //b[text()='Cart']
# //ul[@class="sf-menu clearfix menu-content sf-js-enabled sf-arrows"]/li[2]

# CSS SELECTOR:
# ul#id=homefeatured a.product-name[title='Blouse']
# ul#homefeatured
# a:contains()='Women' - search using attributes in the xpath
# a[text()='Women'] - search using text of the element in your xpath
# //b[text()='Cart']
# //ul[@class="sf-menu clearfix menu-content sf-js-enabled sf-arrows"]/li[2]
time.sleep(2)
result = driver.find_element(By.CSS_SELECTOR, 'span.heading-counter').text

items = []
products = driver.find_elements(By.XPATH, "//div[@id='center_column']//a[@class='product-name']")
for product in products:
    print(product.text)
    items.append(product.text.strip())
print('The list of items:', items)

print('############## Completed ################')
print('The result of the search:', result)
# driver.quit()
 
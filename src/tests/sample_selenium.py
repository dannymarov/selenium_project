from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()
driver.get('https://www.thelevelupsolutions.com/')

driver.quit()
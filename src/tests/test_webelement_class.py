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

email = 'mycool@emial.com'
# custfirst_name = 'Joe'
# custlast_name = 'Doe'
# password = 'Forgetmenot'
# state = 'New Jersey'
filepath = '../../screenshots/'

# STEPS:
# 1. open the browser

def click_element_by_locator(driver, locator, method='xpath', wait_time=10):
    try:
        wdwait = WebDriverWait(driver, wait_time)
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

def test_go_to_authentication_page(driver):
    # 2. open the automationpractice.com
    driver.get('http://automationpractice.com/index.php')
    # click on sign in
    sign_in_link = "//a[contains(text(),'sign in')]"
    # option 1 click using regular element method
    driver.find_element(By.XPATH, sign_in_link).click()
    # option 2 use function created above with explicit wait
    click_element_by_locator(sign_in_link)
    # click_element_by_xpath(sign_in_link, 20) if user wants to provide value of time
    # to wait instead of using default value of 10, the provided value would overwrite the default value
    sleep(3)

def test_create_account(driver, email):
    """
    Creating the account with email and static data for the sign up info.
    This step is dependent on test_go_to_authentication_page()
    :param email: email with @ symbol and dot to be included
    """

    # Variables:
    custfirst_name = 'Joe'
    custlast_name = 'Doe'
    password = 'Forgetmenot'
    state = 'New Jersey'

    # enter email address to Create an Account field, mycool@email.com, click on create account
    driver.find_element(By.ID, "email_create").send_keys(email)
    driver.find_element(By.ID, 'SubmitCreate').click()
    sleep(3)

    # radio button: click on Mr
    mr_gender = driver.find_element(By.ID, 'id_gender1')
    mrs_gender = driver.find_element(By.ID, 'id_gender2')
    mrs_gender.click()
    click_element_by_locator('id_gender2', method='id')

    # mr_gender.click()

    # enter first name
    cfirst_name = driver.find_element(By.NAME, 'customer_firstname')
    cfirst_name.send_keys(custfirst_name)
    # enter last name
    clast_name = driver.find_element(By.NAME, 'customer_lastname')
    clast_name.send_keys(custlast_name)

    # enter password
    driver.find_element(By.ID, 'passwd').send_keys(password)



    # check sign up for our newsletter
    newsletter = driver.find_element(By.ID, 'newsletter')
    newsletter.click()
    sleep(5)
    driver.save_screenshot(filepath + 'signup1.png')

    # part of the homework
    special = driver.find_element(By.NAME, 'optin')
    special.click()
    # clear it and enter different name
    cfirst_name.clear()
    cfirst_name.send_keys('Jonathan')

    # verify email, get text, make sure is what we entered
    # verify Mr is selected
    # mr_gender.is_selected()
    print('Is gender type selected Mr: ', mr_gender.is_selected())
    print('Is gender type Mrs selected: ', mrs_gender.is_selected())
    if mrs_gender.is_selected():
        mr_gender.click()
    print('Is gender type selected Mr: ', mr_gender.is_selected())
    print('Is gender type Mrs selected: ', mrs_gender.is_selected())

    # verify sign up is checked
    print('Is sign up checkbox checked: ', newsletter.is_selected())

    # verify one of the error messages appearing when required field is not entered
    address_msg_xpath = "//input[@id='address1']/../span"
    address_msg_elem = driver.find_element(By.XPATH, address_msg_xpath)
    address_msg = ''
    if address_msg_elem.is_displayed():
        address_msg = driver.find_element(By.XPATH, address_msg_xpath).text
    else:
        print('Address message is not displayed.')
    # address_msg = driver.find_element(By.XPATH, address_msg).text
    print('This is a message type: ', address_msg)
    driver.save_screenshot(filepath + 'signup2.png')
    # driver.quit()
    # the rest for H/W
    # click on register
    # select state

    driver.execute_script('window.scrollBy(0,990)')
    state_ddown = Select(driver.find_element(By.ID, 'id_state'))
    state_ddown.select_by_value('30')
    print('Current selection:', state_ddown.all_selected_options[0].text)
    sleep(3)
    # state_ddown.options - return all available options
    # state_ddown.all_selected_options - return all selected options
    state_ddown.select_by_visible_text('New Jersey')
    print('Current selection:', state_ddown.all_selected_options[0].text)
    sleep(3)
    state_ddown.select_by_index(31) #in case value and indexes are not match
    print('Current selection:', state_ddown.all_selected_options[0].text)

def test_explicit_wait(driver):
    # open the website
    host = 'https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver'
    driver.get(host)
    print('############## Testing Populating the text ############')
    click_element_by_locator('populate-text', 'id')
    wdwait = WebDriverWait(driver, 15)
    wdwait.until(EC.text_to_be_present_in_element((By.ID, 'h2'),'Selenium'))
    element = wdwait.until(EC.presence_of_element_located((By.ID, 'h2')))
    print('text in the element:', element.text)

    print('############### Testing Visibile Text ################')
    click_element_by_locator('display-other-button', 'id')
    button_text = wdwait.until(EC.visibility_of_element_located((By.ID, 'hidden'))).text
    print('Text inside button:', button_text)

def test_drag_drop(driver):
    print('############## Testing drag and drop ##############')
    driver.get('https://jqueryui.com/droppable/')
    wdwait = WebDriverWait(driver, 20)
    driver.switch_to.frame(0)
    source_element = wdwait.until(EC.presence_of_element_located((By.ID, 'draggable')))
    target_element = wdwait.until(EC.presence_of_element_located((By.ID, 'droppable')))
    print(f"Original text in the box:'{target_element.text}'")

    actions = ActionChains(driver)
    actions.drag_and_drop(source_element, target_element).perform()
    print(f"Text in the box after drag and drop:'{target_element.text}'")

def test_mouse_hover(driver):
    wdwait = WebDriverWait(driver, 30)

    driver.get('http://automationpractice.com/index.php')
    driver.execute_script('window.scrollBy(0,750)')
    # product1 = driver.find_element(By.XPATH, "//ul[@id='homefeatured']/li[1]")

    product1 = wdwait.until(EC.presence_of_element_located((By.XPATH, "//ul[@id='homefeatured']/li[1]")))
    actions = ActionChains(driver)
    actions.move_to_element(product1).perform()
    # actions.context_click()
    driver.find_element(By.LINK_TEXT, 'Add to cart').click()


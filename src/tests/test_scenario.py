# from src.webelement_alerts import *
# from src.webelement_class import *

# email = 'mycool@emial.com'
# driver = webdriver.Chrome()
# driver.implicitly_wait(20)  # synchronizing the browser
# driver.maximize_window()

# test_create_account()
# test_go_to_authentication_page()

# test_js_alert_single_button()
# test_alert_multiple_button()

# test_js_alert_single_button(driver)
# test_alert_multiple_button(driver)
# test_drag_drop()
# test_mouse_hover()
# sleep(5)
# driver.quit()
# test_explicit_wait()
import pytest

@pytest.mark.myFirstCase
@pytest.mark.sample1
@pytest.mark.regression
def test_sample_pytst():
    assert 25 / 5 == 5
    print('/n Test1:yeah this is the first pytest')

@pytest.mark.mySecondCase
@pytest.mark.regression
def test_sample_pytst2():
    print('/n Test2:yeah this is the first pytest')
    assert 25 / 5 == 65

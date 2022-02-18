# link = "http://selenium1py.pythonanywhere.com/"
#
#
# def test_guest_should_see_login_link(browser):
#     browser.get(link)
#     browser.find_element_by_css_selector("#login_link")
import time
link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    time.sleep(10)
    browser.find_element_by_css_selector("#login_link")


import time

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


def test_button_add_to_cart_exist(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    time.sleep(5)
    button_element = browser.find_element_by_css_selector('[class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert button_element is not None, 'Кнопка не найдена'


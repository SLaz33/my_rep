import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


list_links = ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1', 'https://stepik.org/lesson/236897/step/1',
              'https://stepik.org/lesson/236898/step/1', 'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
              'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1']


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('links', list_links)
def test_func(browser, links):
    link = links
    browser.get(link)
    browser.implicitly_wait(5)
    input1 = browser.find_element_by_css_selector('[placeholder="Напишите ваш ответ здесь..."]')
    answer = str(math.log(int(time.time())))
    input1.send_keys(answer)
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    # button = browser.find_element_by_class_name('submit-submission')
    button.click()
    message_element = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
    message = message_element.text
    assert message == "Correct!", message







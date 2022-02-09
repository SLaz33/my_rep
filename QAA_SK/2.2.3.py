from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select



try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    num_1 = int(browser.find_element_by_id('num1').text)
    num_2 = int(browser.find_element_by_id('num2').text)
    x = num_1 + num_2

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(x))
    time.sleep(2)
    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
  time.sleep(10)
  browser.quit()
from selenium import webdriver
import time
import os



try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_css_selector('[placeholder="Enter first name"]')
    input1.send_keys("Ivan")
    input1 = browser.find_element_by_css_selector('[placeholder="Enter last name"]')
    input1.send_keys("Ivanov")
    input1 = browser.find_element_by_css_selector('[placeholder="Enter email"]')
    input1.send_keys("123@mail.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file = browser.find_element_by_id('file')
    file.send_keys(file_path)
    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
  time.sleep(10)
  browser.quit()
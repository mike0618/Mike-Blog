from selenium import webdriver
from my_conf import chromedriver_path
from time import time

driver = webdriver.Chrome(chromedriver_path)
driver.get('http://orteil.dashnet.org/experiments/cookie/')
cookie = driver.find_element_by_id('cookie')


def clicker():
    check_timer = time() + 5
    while time() < check_timer:
        cookie.click()
    check()


def check():
    items = driver.find_elements_by_css_selector('#store div')
    items.reverse()
    for item in items:
        if 'a' not in item.get_attribute('class'):
            item.click()
            break
    if time() < timeout:
        clicker()


timeout = time() + 60 * 5
clicker()

print(driver.find_element_by_id('cps').text)
driver.close()

from selenium import webdriver
from my_conf import chromedriver_path, LOGIN, PASS, LINK
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException

# --- INITIALIZATION
driver = webdriver.Chrome(chromedriver_path)
driver.get(LINK)
sleep(1)
cookie_btn = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button')
cookie_btn.click()
sleep(1)

# --- LOGIN
log_in_btn = driver.find_element_by_css_selector('div .button')
log_in_btn.click()
sleep(10)
# fb_btn = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
# fb_btn.click()
google_btn = driver.find_element_by_xpath('//*[@aria-label="Log in with Google"]')
sleep(3)
google_btn.click()
sleep(3)

# --- FILLING OUT LOGIN FORM
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

login_field = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]'
                                           '/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
login_field.send_keys(LOGIN)
sleep(0.5)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/'
                             'div/div/button').click()
sleep(2)
pass_field = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form'
                                          '/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
pass_field.send_keys(PASS)
sleep(0.5)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]'
                             '/div/div/button').click()
sleep(10)

# --- INSIDE PREPARATION
driver.switch_to.window(base_window)
print(driver.title)
sleep(10)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]').click()
sleep(0.5)
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]').click()
sleep(8)

# --- SWIPING
driver.find_element_by_xpath(
    '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button').click()
n = 1
print('swiped', n)
while True:
    sleep(3)
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]'
                                     '/div/div[4]/button').click()
        n += 1
        print('swiped', n)
    except (ElementClickInterceptedException, NoSuchElementException):
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[2]').click()
# driver.close()

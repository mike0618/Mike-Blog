from bs4 import BeautifulSoup
import requests
from my_conf import ZILLOW_URL, BROWSER_HEADERS, GOOGLE_FORM
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service

# Beautiful Soup
zillow_page = requests.get(ZILLOW_URL, headers=BROWSER_HEADERS).text
soup = BeautifulSoup(zillow_page, 'html.parser')
divs = soup.find_all('div', class_='StyledPropertyCardDataWrapper')
properties = [
    {'address': div.address.getText().strip(), 'price': div.span.getText().replace('+', '').split('/')[0].split()[0],
     'link': div.a.get('href')} for div in divs]

# Selenium
service = Service(log_output='NUL', log_path='NUL')
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)
driver.get(GOOGLE_FORM)
for p in properties:
    addr = wait.until(ec.element_to_be_clickable(
        (By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    price = wait.until(ec.element_to_be_clickable(
        (By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    link = wait.until(ec.element_to_be_clickable(
        (By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    addr.click()
    addr.send_keys(p['address'])
    price.click()
    price.send_keys(p['price'])
    link.click()
    link.send_keys(p['link'])
    wait.until(ec.element_to_be_clickable(
        (By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div'))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'))).click()
# driver.close()

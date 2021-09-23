from bs4 import BeautifulSoup
import requests
from my_conf import ZILLOW_URL, BROWSER_HEADERS, chromedriver_path, GOOGLE_FORM
from selenium import webdriver
from time import sleep

zillow_page = requests.get(ZILLOW_URL, headers=BROWSER_HEADERS).text
soup = BeautifulSoup(zillow_page, 'lxml')
articles = soup.find_all('article')

links = []
prices = []
addresses = []

for article in articles:
    link = article.a
    if link:
        href = link.get('href')
        if href.startswith('/b/'):
            href = 'https://www.zillow.com' + href
        links.append(href)
        prices.append(article.find('div', class_='list-card-price').getText()[:6])
        addresses.append(article.address.getText())

driver = webdriver.Chrome(chromedriver_path)

for i in range(len(links)):
    driver.get(GOOGLE_FORM)
    sleep(2)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/'
                                 'div[1]/input').send_keys(addresses[i])
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/'
                                 'div[1]/input').send_keys(prices[i])
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/'
                                 'div[1]/input').send_keys(links[i])
    sleep(1)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div').click()
    sleep(1)

driver.close()

from selenium import webdriver
from my_conf import chromedriver_path
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(chromedriver_path)
driver.get('https://en.wikipedia.org/wiki/Main_Page')
total_articles = driver.find_element_by_css_selector('#articlecount a')
print(total_articles.text)
# total_articles.click()

all_portals = driver.find_element_by_link_text('All portals')
# all_portals.click()

search_bar = driver.find_element_by_id('searchInput')
search_bar.send_keys('Python')
search_bar.send_keys(Keys.ENTER)

driver.get('http://secure-retreat-92358.herokuapp.com/')
fname = driver.find_element_by_name('fName')
lname = driver.find_element_by_name('lName')
email = driver.find_element_by_name('email')
btn = driver.find_element_by_css_selector('form button')
fname.send_keys('My Name')
lname.send_keys('My Last Name')
email.send_keys('my_email@gmail.com')
btn.click()
# driver.close()

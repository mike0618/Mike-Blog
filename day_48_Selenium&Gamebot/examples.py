from selenium import webdriver
from my_conf import chromedriver_path

driver = webdriver.Chrome(executable_path=chromedriver_path)
# driver.get('https://www.amazon.com/ASUS-i7-10750H-ScreenPad-Celestial-UX581LV-XS74T/dp/B08D941WH6/'
#            'ref=sr_1_1?dchild=1&keywords=ASUS%2BZenBook%2BPro%2BDuo%2BUX581&qid=1626358964&sr=8-1&th=1')
# price = driver.find_element_by_id('priceblock_ourprice')
# print(price.text)

driver.get('https://www.python.org')
search_bar = driver.find_element_by_name('q')
print(search_bar.get_attribute('placeholder'))

logo = driver.find_element_by_class_name('python-logo')
print(logo.size)

documentation_link = driver.find_element_by_css_selector('.documentation-widget a')
print(documentation_link.text)

bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

upcoming_events = {}
for i in range(5):
    datetime = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i+1}]/time')
    date = datetime.get_attribute('datetime').split('T')[0]
    name = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i+1}]/a').text
    upcoming_events[i] = {date: name}
print(upcoming_events)

upcoming_events2 = {}
# datetimes = driver.find_elements_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time')
# datetimes = driver.find_elements_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')
datetimes = driver.find_elements_by_css_selector('.event-widget time')
names = driver.find_elements_by_css_selector('.event-widget li a')
for i in range(5):
    upcoming_events2[i] = {'date': datetimes[i].get_attribute('datetime').split('T')[0],
                           'name': names[i].text}
print(upcoming_events2)

driver.close()
# driver.quit()

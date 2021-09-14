from selenium import webdriver
from my_conf import chromedriver_path, LOGIN, PASS, SIMILAR_ACCOUNT
from time import sleep
from random import randint

INSTA_LOGIN_LINK = 'https://www.instagram.com/'

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(chromedriver_path)

    def login(self):
        self.driver.get(INSTA_LOGIN_LINK)
        sleep(2)
        login_entry = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/'
                                                        'div/div[1]/div/label/input')
        login_entry.send_keys(LOGIN)
        pass_entry = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/'
                                                       'div/div[2]/div/label/input')
        pass_entry.send_keys(PASS)
        sleep(1)
        login_btn = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/'
                                                      'div/div[3]/button')
        login_btn.click()
        sleep(3)
        notnow_btn = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
        notnow_btn.click()
        sleep(2)
        notnow_btn2 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
        notnow_btn2.click()
        sleep(2)

    def find_followers(self):
        self.driver.get(INSTA_LOGIN_LINK + SIMILAR_ACCOUNT)
        sleep(2)
        number_followers = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/'
                                                             'li[2]/a/span').get_attribute('title').replace(',', '')
        print(number_followers)
        followers_lnk = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/'
                                                          'header/section/ul/li[2]/a')
        followers_lnk.click()
        sleep(3)
        popup = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
        # for i in range(10):
        for i in range(int(number_followers) // 12):
            sleep(randint(1000, 1600) / 1000)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup)

    def follow(self):
        sleep(5)
        followers = self.driver.find_elements_by_css_selector('li button')
        for follower in followers:
            if follower.text == 'Follow':
                sleep(randint(1000, 1600) / 1000)
                follower.click()


follow_bot = InstaFollower()
follow_bot.login()
follow_bot.find_followers()
follow_bot.follow()

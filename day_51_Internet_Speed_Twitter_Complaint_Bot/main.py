from selenium import webdriver
from my_conf import chromedriver_path, LOGIN, PASS, TWITTER_LOGIN_LINK, SPEEDTEST_LINK, PROMISED_DOWN, PROMISED_UP
from time import sleep

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(chromedriver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_LINK)
        sleep(10)
        go_btn = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_btn.click()
        sleep(60)
        self.down = float(self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                            'div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/'
                                                            'div[2]/span').text)
        self.up = float(self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                          'div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/'
                                                          'div[2]/span').text)
        # self.driver.quit()
        print(f'down: {self.down}\nup: {self.up}')

    def tweet_at_provider(self):
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            msg = f'Hey, Internet Provider, why is my internet speed\n{self.down}down/{self.up}up when I pay for ' \
                  f'{PROMISED_DOWN}down/{PROMISED_UP}up?'

            # --- LOGIN
            self.driver.get(TWITTER_LOGIN_LINK)
            sleep(5)
            login_field = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/'
                                                            'div/div[1]/label/div/div[2]/div/input')
            login_field.send_keys(LOGIN)
            sleep(1)
            # next_btn = self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/'
            #                                              'div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div')
            # next_btn.click()
            # sleep(3)
            pass_field = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/'
                                                           'div/div[2]/label/div/div[2]/div/input')
            pass_field.send_keys(PASS)
            sleep(1)
            login_btn = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/'
                                                          'div/div[3]/div')
            login_btn.click()
            sleep(20)

            # --- TWEET

            focus = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/'
                                                      'div[2]')
            focus.click()
            sleep(1)
            msg_field = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/'
                                                          'div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/'
                                                          'div/div/div/div/div/div/div/label/div[1]/div/div/div/div/'
                                                          'div/div/div/div/div/span')
            msg_field.send_keys(msg)
            sleep(1)
            tweet_btn = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/'
                                                          'div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/'
                                                          'div[2]/div[3]')
            tweet_btn.click()

            self.driver.close()


complaint_bot = InternetSpeedTwitterBot()
complaint_bot.get_internet_speed()
complaint_bot.tweet_at_provider()

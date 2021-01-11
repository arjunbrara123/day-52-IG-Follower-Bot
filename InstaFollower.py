from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os import environ
from time import sleep

CHROME_DRIVER_PATH = "chromedriver.exe"
SIMILAR_ACCT = "rolandfrasier"
IG_USERNAME = environ['IG_USERNAME']
IG_PASSWORD = environ['IG_PASSWORD']


class InstaFollower:
    pass

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        accept_cookies = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]')
        accept_cookies.click()
        sleep(2)
        input_username = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        input_username.send_keys(IG_USERNAME)
        input_password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        input_password.click()
        input_password.send_keys(IG_PASSWORD)
        btn_login = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        btn_login.click()
        sleep(5)
        btn_not_now_1 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        btn_not_now_1.click()
        sleep(5)
        btn_not_now_2 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        btn_not_now_2.click()
        sleep(2)
        input_search = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        input_search.send_keys(SIMILAR_ACCT)
        sleep(1)
        input_search.send_keys(Keys.ENTER)
        input_search.send_keys(Keys.ENTER)
        sleep(3)
        followers_tag = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        followers_tag.click()

    def find_followers(self):
        pass

    def follow(self):
        pass

    def close(self):
        self.driver.quit()

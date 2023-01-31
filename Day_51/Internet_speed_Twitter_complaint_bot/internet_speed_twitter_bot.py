from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

class InternetSpeedTwitterBot:
    
    def __init__(self, driver_path):
        self.down = 0
        self.up = 0
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)

        try:
            consent_button = self.driver.find_element_by_id("_evidon-banner-acceptbutton")
            consent_button.click()
        except NoSuchElementException:
            pass

        time.sleep(5)
        go_button = self.driver.find_element_by_css_selector(".speedtest-container .start-button .js-start-test .start-text")
        go_button.click()
        time.sleep(60)
        self.down = float(self.driver.find_element_by_css_selector(".result-container-speed .result-container-data .result-item .result-data .download-speed").text)
        self.up = float(self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)

    def tweet_at_provider(self, twitter_mail, twitter_password):
        self.driver.get("https://twitter.com/")
        time.sleep(5)

        login_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        login_button.click()
        time.sleep(3)

        email = self.driver.find_element_by_tag_name("input")
        email.send_keys(twitter_mail)

        next_button = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_button.click()
        time.sleep(3)

        password = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(twitter_password)

        login_button = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        login_button.click()
        time.sleep(3)

        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(f"Just testing an automated Python script. My current download speed is {self.down}Mbps and my current upload speed is {self.up}Mbps. @udemy")

        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_button.click()
        time.sleep(3)

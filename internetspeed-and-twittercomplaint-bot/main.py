from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

from time import sleep

PROMISED_DOWN = 100
PROMISED_UP = 15
x_password = "your_password"
x_email= "your_email@gmail.com"
class InternetSpeedXBot:
    print("yes")
    def __init__(self):
        print("yes")
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0
        self.wait = WebDriverWait(self.driver, 20)
    def get_internet_speed(self):
        print("yes")
        self.driver.get("https://www.speedtest.net")
        print("getting internet speed")
        # speedtest = self.driver.window_handles[0]
        sleep(3)
        try:
            self.driver.find_element(By.XPATH, "//*[@id='onetrust-accept-btn-handler']").click()
        except NoSuchElementException:
            print("Already accepted or not found")
        sleep(3)
        go_button = self.driver.find_element(By.XPATH, "//*[@id='container']/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a")
        go_button.click()
        sleep(60)
        self.down = float(self.driver.find_element(By.XPATH, "//*[@id='container']/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text)
        self.up = float(self.driver.find_element(By.XPATH, "//*[@id='container']/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text)
        print(f"down: {self.down}")
        print(f"up: {self.up}")
    def tweet_at_provider(self):
        print("tweeting")
        self.driver.get("https://x.com/i/flow/login")
        sleep(4)
        email = self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='text']")))
        email.clear()
        email.send_keys(x_email, Keys.ENTER)
        password = self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
        password.send_keys(x_password, Keys.ENTER)
        sleep(5)
        print("Logged in successfully")
        print("Tweeting at provider")
        tweet_compose = self.driver.find_element(By.XPATH, value="// *[ @ id = 'react-root'] / div / div / div[2] / header / div / div / div / div[1] / div[3] / a")
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        sleep(3)
        tweet_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()
        sleep(2)
        self.driver.quit()
internet_speed_bot = InternetSpeedXBot()
internet_speed_bot.get_internet_speed()
internet_speed_bot.tweet_at_provider()

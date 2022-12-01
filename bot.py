from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import welcomeScreen


class Bot:

    @staticmethod
    def start():
        browser = webdriver.Edge("msedgedriver.exe")
        elements = browser.get("https://web.whatsapp.com/")
        sleep(50)


        browser.quit()

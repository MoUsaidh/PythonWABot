from threading import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from time import sleep
import welcomeScreen

class Bot():
    @staticmethod
    def Start():
        browser = webdriver.Edge("msedgedriver.exe")
        browser.get("https://web.whatsapp.com/")

        welcomeScreen.Welcome()

        browser.quit()

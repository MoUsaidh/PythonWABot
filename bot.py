# from selenium.webdriver.edge.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import welcomeScreen
import datetime

browser = webdriver.Edge("msedgedriver.exe")

today = datetime.datetime.today()
tomorrow = today + datetime.timedelta(days=1)


class Bot:

    @staticmethod
    def Start():
        browser.get("https://web.whatsapp.com/")
        welcomeScreen.Welcome()

        browser.quit()

    @staticmethod
    def wishNow():
        with open("birthdays.json") as j:
            json_data = json.load(j)

        todayBirthday = []
        for i, items in enumerate(json_data):
            if items["birth_date"] == today.strftime("%d") and items["birth_month"] == today.strftime("%m"):
                todayBirthday.append(json_data[i])

        for i, items in enumerate(todayBirthday):
            search_box = browser.find_element("xpath", "//*[@id='side']/div[1]/div/div/div[2]/div/div[2]")
            search_box.send_keys("")
            search_box.send_keys(items["ph"])
            search_box.send_keys(Keys.ENTER)
            msg_box = browser.find_element("xpath", "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
            msg_box.send_keys("happy birthday")
            msg_box.send_keys(Keys.ENTER)

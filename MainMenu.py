import json
import tkinter
from tkinter import ttk
import datetime
import list
import bot


class MainMenu:
    def __init__(self):
        self.menu()

    @staticmethod
    def menu():

        with open("birthdays.json") as j:
            json_data = json.load(j)

        today = datetime.datetime.today()
        tomorrow = today + datetime.timedelta(days=1)

        todayBirthday = []
        for i, items in enumerate(json_data):
            if items["birth_date"] == today.strftime("%d") and items["birth_month"] == today.strftime("%m"):
                todayBirthday.append(json_data[i])

        tomorrowBirthday = []
        for i, items in enumerate(json_data):
            if items["birth_date"] == tomorrow.strftime("%d") and items["birth_month"] == tomorrow.strftime("%m"):
                tomorrowBirthday.append(json_data[i])

        # window
        menu = tkinter.Tk()
        menu.title("WABOT")
        menu.resizable(False, False)

        # elements
        # title label
        label1 = tkinter.Label(master=menu, text="WABOT", width=8, padx=10, pady=10, font=('Consolas', 14))
        label1.grid(row=0, column=1)
        # buttons
        button_send = tkinter.Button(master=menu, text="SEND NOW", width=8, padx=10, pady=10, command=bot.Bot.wishNow)
        button_send.grid(row=1, column=0)

        button_sendlater = tkinter.Button(master=menu, text="SEND LATER", width=8, padx=10, pady=10)
        button_sendlater.grid(row=1, column=1)

        button_list = tkinter.Button(master=menu, text="LIST", width=5, padx=10, pady=10, command=list.List)
        button_list.grid(row=1, column=2)

        # frame
        frame1 = tkinter.LabelFrame(master=menu, text="Upcoming Events", padx=4, pady=4, font=('Consolas', 14))
        frame1.grid(row=3, column=0, columnspan=3)

        # table
        treev = ttk.Treeview(master=frame1, selectmode='browse')
        treev.grid(row=0, column=0, rowspan=3, columnspan=3)

        treev["columns"] = ("name", "ph", "birth_month", "birth_date")

        # Defining heading
        treev['show'] = 'headings'

        # Assigning the width and anchor to  the
        # respective columns
        treev.column("name", width=100, anchor='c')
        treev.column("ph", width=80, anchor='s')
        treev.column("birth_month", width=60, anchor='s')
        treev.column("birth_date", width=60, anchor='s')

        # Assigning the heading names to the
        # respective columns
        treev.heading("#0", text="ID")
        treev.heading("name", text="Name")
        treev.heading("ph", text="Phone")
        treev.heading("birth_month", text="Birth Day")
        treev.heading("birth_date", text="Birth Date")

        upcomingEvent = todayBirthday+tomorrowBirthday

        for i, item in enumerate(upcomingEvent):
            treev.insert("", "end", i, text=i)
            treev.set(i, column="name", value=item["name"])
            treev.set(i, column="ph", value=item["ph"])
            treev.set(i, column="birth_month", value=item["birth_month"])
            treev.set(i, column="birth_date", value=item["birth_date"])

        menu.mainloop()

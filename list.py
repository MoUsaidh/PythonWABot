import tkinter
from tkinter import ttk
import json


class List:
    def __init__(self):
        self.menu()

    @staticmethod
    def menu():
        # window
        menu = tkinter.Tk()
        menu.title("WABOT")
        menu.resizable(False, False)

        # elements
        # title label

        # buttons
        button_send = tkinter.Button(master=menu, text="Add", width=8, padx=10, pady=10)
        button_send.grid(row=1, column=0)

        button_sendlater = tkinter.Button(master=menu, text="Delete", width=8, padx=10, pady=10)
        button_sendlater.grid(row=1, column=1)

        button_list = tkinter.Button(master=menu, text="Update", width=5, padx=10, pady=10)
        button_list.grid(row=1, column=2)

        # frame
        frame1 = tkinter.LabelFrame(master=menu, padx=4, pady=4, font=('Consolas', 14))
        frame1.grid(row=3, column=0, columnspan=3)

        # table

        with open("birthdays.json") as f:
            json_data = json.load(f)



        treev = ttk.Treeview(master=frame1, selectmode='browse')

        treev["columns"] = ("name", "ph", "birth_month", "birth_date")

        # Defining heading
        treev['show'] = 'headings'

        # Assigning the width and anchor to  the
        # respective columns
        treev.column("name", width=180, anchor='c')
        treev.column("ph", width=100, anchor='s')
        treev.column("birth_month", width=100, anchor='s')
        treev.column("birth_date", width=100, anchor='s')

        # Assigning the heading names to the
        # respective columns
        treev.heading("#0", text="ID")
        treev.heading("name", text="Name")
        treev.heading("ph", text="Phone")
        treev.heading("birth_month", text="month")
        treev.heading("birth_date", text="day")

        for i, item in enumerate(json_data):
            treev.insert("", "end", i, text=i)
            treev.set(i, column= "name", value=item["name"])
            treev.set(i, column= "ph", value=item["ph"])
            treev.set(i, column= "birth_month", value=item["birth_month"])
            treev.set(i, column= "birth_date", value=item["birth_date"])

        treev.grid(row=0, column=0, rowspan=3, columnspan=3)


        menu.mainloop()

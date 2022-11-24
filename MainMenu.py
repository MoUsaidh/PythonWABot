import tkinter
from tkinter import ttk

class MainMenu:
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
        label1 = tkinter.Label(master=menu, text="WABOT", width=8, padx=10, pady=10, font=('Consolas',14))
        label1.grid(row=0, column=1)
        # buttons
        button_send = tkinter.Button(master=menu, text="SEND NOW", width=8, padx=10, pady=10)
        button_send.grid(row=1, column=0)

        button_sendlater = tkinter.Button(master=menu, text="SEND LATER", width=8, padx=10, pady=10)
        button_sendlater.grid(row=1, column=1)

        button_list = tkinter.Button(master=menu, text="LIST", width=5, padx=10, pady=10)
        button_list.grid(row=1, column=2)

        # frame
        frame1 = tkinter.LabelFrame(master=menu, text="Upcoming Events",padx=4, pady=4, font=('Consolas',14))
        frame1.grid(row=3, column=0,columnspan=3)

        # table
        treev=ttk.Treeview(master=frame1,selectmode='browse')
        treev.grid(row=0, column=0, rowspan=3,columnspan=3)

        treev["columns"] = ("1", "2")

        # Defining heading
        treev['show'] = 'headings'

        # Assigning the width and anchor to  the
        # respective columns
        treev.column("1", width=180, anchor='c')
        treev.column("2", width=100, anchor='s')

        # Assigning the heading names to the
        # respective columns
        treev.heading("1", text="Name")
        treev.heading("2", text="Birth Date")


        menu.mainloop()

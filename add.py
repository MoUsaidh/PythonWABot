import tkinter
from tkinter import ttk


class Add:
    def __init__(self):
        self.menu()

    @staticmethod
    def menu():
        # window
        menu = tkinter.Tk()
        menu.title("WABOT")
        menu.resizable(False, False)


        # labels
        label2 = tkinter.Label(master=menu, text="NAME", width=8)
        label2.grid(row=1, column=0, padx=10, pady=10)

        label3 = tkinter.Label(master=menu, text="PHONE NO", width=8)
        label3.grid(row=2, column=0, padx=10, pady=10)

        label4 = tkinter.Label(master=menu, text="DATE", width=8)
        label4.grid(row=3, column=0, padx=10, pady=10)

        label5 = tkinter.Label(master=menu, text="MONTH", width=8 )
        label5.grid(row=3, column=2, padx=10, pady=10)

        label6 = tkinter.Label(master=menu, text="MESSAGE", width=8)
        label6.grid(row=4, column=0, padx=10, pady=10)

        # entry
        name_var = tkinter.StringVar
        phoneno_var=tkinter.StringVar
        date_var=tkinter.IntVar
        month_var = tkinter.IntVar
        msg_var=tkinter.StringVar


        name_entry = tkinter.Entry(master=menu, width=20, textvariable=name_var)
        name_entry.grid(row=1, column=1)

        phoneno_entry = tkinter.Entry(master=menu, width=20, textvariable=phoneno_var)
        phoneno_entry.grid(row=2, column=1)

        date_entry=tkinter.Entry(master=menu, width=5,textvariable=date_var)
        date_entry.grid(row=3, column=1,)

        month_entry = tkinter.Entry(master=menu, width=5, textvariable=month_var)
        month_entry.grid(row=3, column=3,padx=10)

        msg_entry= tkinter.Entry(master=menu, width=20, textvariable=msg_var)
        msg_entry.grid(row=4, column=1)

        button_send = tkinter.Button(master=menu, text="Submit", width=8 )
        button_send.grid(row=5, column=1,padx=10, pady=10)



        menu.mainloop()

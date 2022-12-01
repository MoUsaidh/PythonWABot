import tkinter
import MainMenu

class Welcome:
    def __init__(self):
        self.menu()

    @staticmethod
    def menu():
        # window
        menu = tkinter.Tk()
        menu.title("WABOT")
        menu.resizable(False, False)

        #labels
        label1 = tkinter.Label(master=menu, text="WABOT", width=30, padx=10, pady=10, font=('Consolas', 14))
        label1.grid(row=0, column=0)

        label2 = tkinter.Label(master=menu, text="after scanning the qr code", width=30, padx=10, pady=10, font=('Consolas', 14))
        label2.grid(row=1, column=0)

        label3 = tkinter.Label(master=menu, text="please click the 'start' button", width=30, padx=10, pady=10, font=('Consolas', 14))
        label3.grid(row=2, column=0)

        label4 = tkinter.Label(master=menu, text="   ", width=10, padx=10, pady=10,font=('Consolas', 14))
        label4.grid(row=4, column=0)

        #button
        button1=tkinter.Button(master=menu, text="Start", width=8, padx=10, pady=10, command=MainMenu.MainMenu)
        button1.grid(row=3, column=0)


        menu.mainloop()


Welcome()

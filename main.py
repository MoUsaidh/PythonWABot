import multiprocessing as mp
import MainMenu
import bot

if __name__ == '__main__':
    p1 = mp.Process(target=bot.Bot.start())
    p2 = mp.Process(target=MainMenu.MainMenu())

    p1.start()
    p2.start()

import time
from tkinter import *
from tkinter.ttk import *

window = Tk()

window.title("message spammer")


def clicked():
    message = "grc"
    keyboard = Controller()

    time.sleep(5)

    for num in range(100):
        for letter in message:
            keyboard.press(letter)
            keyboard.release(letter)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(1)


btn = Button(window, text="Start", command=clicked)

btn.grid(column=0, row=0)

window.geometry("350x350")
window.mainloop()

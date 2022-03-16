import tkinter
from tkinter import *
from model.display import display
from model.button import button

window = tkinter.Tk()

display(window)

start_btn = PhotoImage(file='Button.png')
button(window, start_btn)

window.mainloop()

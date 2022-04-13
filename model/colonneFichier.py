from cProfile import label
import tkinter
from tkinter import *
import functools
from turtle import color

class colonneFichier:

    def __init__(self, window, data):
        
        for file in data:
            buttonFichier = Button(
                window,
                text=file,
                foreground='black',
                activeforeground='white',
                font=("Times New Roman", 10, 'bold'),
                borderwidth=0,
                background='white',
                activebackground='white',
                command= functools.partial(self.displayAttributes, file, data[file])
            )
            buttonFichier.pack(expand=YES)

    def displayAttributes(self, file, data):
        windowAttributes = tkinter.Tk()
        windowAttributes.title(file)
        windowAttributes.config(background='#282828')
        windowAttributes.geometry("250x400")

        text = ""

        for fileTested in data:
            text += fileTested + "\n"
            for attributesFileTested in data[fileTested]:
                text += attributesFileTested + " : " + data[fileTested][attributesFileTested] + "\n"
            text += "\n"
            
        label=Label(windowAttributes, text=text, background='#282828', foreground='white')
        label.pack()
        windowAttributes.mainloop()


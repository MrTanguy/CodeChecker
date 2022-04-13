from tkinter import *
from tkinter import filedialog

class but():

    def __init__(self, window):
        img = PhotoImage(file="Button.png")
        buttonStart = Button(
            window,
            image=img,
            text="START",
            foreground='white',
            activeforeground='white',
            font=("Times New Roman", 40, 'bold'),
            borderwidth=0,
            background='#282828',
            activebackground='#282828',
            compound="center",
            command=self.chooseDirectory()
        )
        buttonStart.pack(expand=YES)

    def chooseDirectory(self):
        dirname = filedialog.askdirectory(title='Select a directory')
        print(dirname)
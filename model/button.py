from tkinter import *
from tkinter import filedialog

class button():

    def __init__(self, window, Image):
        buttonStart = Button(
            window,
            image=Image,
            text="START",
            foreground='white',
            activeforeground='white',
            font=("Times New Roman", 40, 'bold'),
            borderwidth=0,
            background='#282828',
            activebackground='#282828',
            compound="center",
            command=self.chooseDirectory
        )
        buttonStart.pack(expand=YES)

    def chooseDirectory(self):
        dirname = filedialog.askdirectory(title='Select a directory')
        print(dirname)
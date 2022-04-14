
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk 
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import json
from main import execute

LARGE_FONT= ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        self.state('zoomed')
        tk.Tk.wm_title(self, "CodeChecker")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.frames = {}
        self.pstart = StartPage(container, self)
        self.pgraph = PageGraph(container, self)

        for F in (StartPage, PageGraph):

            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        self.first = True
        X = tk.Frame.__init__(self,parent, bg="#282828")
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        self.JsonObject = dict()
        canvas = Canvas(self, width="1000",height="1000", bd = 0)
        canvas.configure(bg = "#282828")
        def chooseDirectory() :
            dirname = filedialog.askdirectory(title='Select a directory')
            if(dirname != "") :
                buttonStart.pack_forget()
                execute(dirname)
                with open("data.json") as jsonFile:
                    jsonObject = json.load(jsonFile)
                    jsonFile.close()
                    self.JsonObject = jsonObject
                    
                    self.fig, self.ax = plt.subplots(figsize=(3, 2))
                    self.fig.patch.set_facecolor('#282828')
                    self.plot_Graph()
                
                    
                        
        start_img = PhotoImage(file= 'Button.png')
        buttonStart = Button(
            self,
            image=start_img,
            text="START",
            foreground='white',
            activeforeground='white',
            font=("Times New Roman", 40, 'bold'),
            borderwidth=0,
            background='#282828',
            activebackground='#282828',
            compound="center",
            command=chooseDirectory
        )
        buttonStart.pack()
        buttonStart.start_img = start_img
        
        button = ttk.Button(self, text="Change Directory",
                            command=chooseDirectory)
        button.pack()

    def plot_Graph(self):
        color = "b"
        self.canvas = FigureCanvasTkAgg(self.fig, self)  
        if(self.first):
            JsonObject = self.JsonObject
            # JSON PART
            Increment = 0
            for files  in self.JsonObject: 
                for testing_files in self.JsonObject[files] :
                    if(float(self.JsonObject[files][testing_files]["Score"]) >= 0.6) :
                        color="r"
                    else:
                        color="g" 
                    an1 = self.ax.annotate(testing_files, xy=(Increment, 0.5), xycoords="data",
                        va="center", ha="center",
                        bbox=dict(boxstyle="round", fc="w"))
                    an2 = self.ax.annotate(files, xy=(0.5, 0.8), xycoords=an1,
                        xytext=(0.5, 0.8), textcoords=(an1, "axes fraction"),
                        va="bottom", ha="center",
                        bbox=dict(boxstyle="round", fc="w"),
                        arrowprops=dict(color=color))
                    an3 = self.ax.annotate(round(float(self.JsonObject[files][testing_files]["Score"]),2), xy=(Increment, 0.65), xycoords="data",
                        va="center", ha="center",
                        bbox=dict(boxstyle="round", fc="w"))
                    Increment+=0.1
                Increment+=0.2
    
            
            
            
            
            
            self.toolbar = NavigationToolbar2Tk(self.canvas, self)
            
           
            self.fig.subplots_adjust(top=0.83)        
            
            plt.axis('off')
            
            self.canvas.draw()
            self.toolbar.update()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            self.first = False
        else :
            self.fig.clear()
            self.canvas.draw()
     
        
        
            
        
class PageGraph(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        self.controller = controller
        


app = SeaofBTCapp()
app.mainloop()
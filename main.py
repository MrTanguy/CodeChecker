# import Python
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from sty import fg

# import fichier
from Functions.env_retriever import retrieve
from Functions.data_clearing import run
from Functions.json_maker import prepareJson
from Functions.json_maker import make

# import tkinter
import tkinter
from tkinter import *
from model.display import display
from model.colonneFichier import colonneFichier
import json

# Initialisation de nos variables
def execute(Path) :
    Sample_Content, Sample_Files =  retrieve(Path)
    All_Content, All_Content_Name = run(Sample_Content, Sample_Files)
    PreJson = {}

    for i in range(len(Sample_Files)):
        PreJson[Sample_Files[i]] = {}
        for j in range(len(Sample_Files)):
            if (i != j):
                PreJson[Sample_Files[i]][Sample_Files[j]] = {}

<<<<<<< HEAD
for i in range(len(Sample_Files)):
    PreJson[Sample_Files[i]] = {}
    for j in range(len(Sample_Files)):
        if (i != j):
            PreJson[Sample_Files[i]][Sample_Files[j]] = {}
            
make(PreJson = prepareJson(PreJson, All_Content, Sample_Files, Sample_Content))
=======
    make(PreJson = prepareJson(PreJson, All_Content, Sample_Files, Sample_Content))
>>>>>>> UI

data = json.load(open('data.json'))

window = tkinter.Tk()

display(window)
colonneFichier(window, data)


window.mainloop()








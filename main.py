# import Python
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from sty import fg

# import fichier
from Functions.env_retriever import retrieve
from Functions.data_clearing import run
from Functions.json_maker import prepareJson
from Functions.json_maker import make

# Initialisation de nos variables

Sample_Content, Sample_Files =  retrieve()
All_Content, All_Content_Name = run(Sample_Content, Sample_Files)
PreJson = {}

for i in range(len(Sample_Files)):
    PreJson[Sample_Files[i]] = {}
    for j in range(len(Sample_Files)):
        if (i != j):
            PreJson[Sample_Files[i]][Sample_Files[j]] = {}

make(PreJson = prepareJson(PreJson, All_Content, Sample_Files, Sample_Content))




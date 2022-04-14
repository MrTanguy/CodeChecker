# Mise en place de l'environnement de travail 
# - Récupération de l'extension souhaitée 
# - Tri des fichiers à analyser

import sys
import os
from dotenv import load_dotenv

def retrieve(Path) :
    s=""
    sample_files = []
    load_dotenv()
    Space_Cleared_Exts = os.environ["EXTENSIONS"].replace(" ", "")

    for ext in os.environ["EXTENSIONS"] :
        if(ext==",") :
            ext="["
            for doc in os.listdir(Path) :
                if doc.endswith(str(s)) :
                    sample_files.append(''.join(doc))
            s = ""
        if(ext!="[" and ext!="]") :
            s+=ext
    for doc in os.listdir(Path) :
        if doc.endswith(str(s.replace(" ",""))) :
            sample_files.append(''.join(doc))

    # sample_contents contient tous les codes de tous les fichiers .py
    sample_contents = [open(Path+"/"+File).read() for File in sample_files]


    if (len(sample_contents) <= 1):
        sys.exit("Vous devez mettre un dossier avec un minimum 2 fichiers Python")
    else :
        return sample_contents, sample_files

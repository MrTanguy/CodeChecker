from Functions.data_vectorize import ExecutePlagiarismChecker
import json


def prepareJson(PreJson, All_Content, Sample_Files, Sample_Content) :
    for index in range(len(All_Content)) : 
        nbEmpty = len(All_Content[index])
        isEmpty = False
        for indexIndex in range(len(All_Content[index])):
            if All_Content[index][indexIndex] == []:
                nbEmpty -= 1
            if nbEmpty == 0 :
                isEmpty = True
                indexFail = index  
        if isEmpty == False:
            for score in ExecutePlagiarismChecker(All_Content[index], Sample_Files) :
                result = (','.join(map(str,(score)))).split(',')
                if index == 0 :
                    if result[2] == "0.0":
                        result[2] = "None"
                    PreJson[result[0]][result[1]]["Commentary"] = result[2]
                    PreJson[result[1]][result[0]]["Commentary"] = result[2]
                elif index == 1 : 
                    if result[2] == "0.0":
                        result[2] = "None"
                    PreJson[result[0]][result[1]]["Loop"] = result[2]
                    PreJson[result[1]][result[0]]["Loop"] = result[2]
                elif index == 2 : 
                    if result[2] == "0.0":
                        result[2] = "None"
                    PreJson[result[0]][result[1]]["Var"] = result[2]
                    PreJson[result[1]][result[0]]["Var"] = result[2]
                elif index == 3 : 
                    if result[2] == "0.0":
                        result[2] = "None"
                    PreJson[result[0]][result[1]]["Function"] = result[2]
                    PreJson[result[1]][result[0]]["Function"] = result[2]
                else :
                    if result[2] == "0.0":
                        result[2] = "None"
                    PreJson[result[0]][result[1]]["Classes"] = result[2]
                    PreJson[result[1]][result[0]]["Classes"] = result[2]
        else:
            for nomFichier in range(len(Sample_Files)):
                for nomFichier2 in range(len(Sample_Files)):
                    if indexFail == 0:
                        if (nomFichier != nomFichier2):
                            PreJson[Sample_Files[nomFichier]][Sample_Files[nomFichier2]]["Commentary"] = "None"
                    if indexFail == 1:
                        if (nomFichier != nomFichier2):
                            PreJson[Sample_Files[nomFichier]][Sample_Files[nomFichier2]]["Loop"] = "None"
                    if indexFail == 2:
                        if (nomFichier != nomFichier2):
                            PreJson[Sample_Files[nomFichier]][Sample_Files[nomFichier2]]["Var"] = "None"
                    if indexFail == 3:
                        if (nomFichier != nomFichier2):
                            PreJson[Sample_Files[nomFichier]][Sample_Files[nomFichier2]]["Function"] = "None"
                    if indexFail == 4:
                        if (nomFichier != nomFichier2):
                            PreJson[Sample_Files[nomFichier]][Sample_Files[nomFichier2]]["Classes"] = "None"
    
                    
    for index in range(len(Sample_Content)):
        for index2 in range(len(Sample_Content)):
                if (index  != index2):
                    testPlagiat = ExecutePlagiarismChecker([Sample_Content[index], Sample_Content[index2]], Sample_Files)
                    mapTestPlagiat = (','.join(map(str,(testPlagiat)))).split(',')
                    score = mapTestPlagiat[2]
                    score = score.replace(')', "")
                    PreJson[Sample_Files[index]][Sample_Files[index2]]["Score"] = score
                    PreJson[Sample_Files[index2]][Sample_Files[index]]["Score"] = score
                    
    return PreJson

def make(PreJson) :
    jsonString = json.dumps(PreJson)
    jsonFile = open("data.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
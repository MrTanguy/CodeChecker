from Functions.data_vectorize import ExecutePlagiarismChecker
import json


def prepareJson(PreJson, All_Content, Sample_Files, Sample_Content) :
    for index in range(len(All_Content)) : 
        for score in ExecutePlagiarismChecker(All_Content[index], Sample_Files) :
            result = (','.join(map(str,(score)))).split(',')
            if index == 0 :
                PreJson[result[0]][result[1]]["Commentary"] = result[2]
                PreJson[result[1]][result[0]]["Commentary"] = result[2]
            elif index == 1 : 
                PreJson[result[0]][result[1]]["Loop"] = result[2]
                PreJson[result[1]][result[0]]["Loop"] = result[2]
            else : 
                PreJson[result[0]][result[1]]["Var"] = result[2]
                PreJson[result[1]][result[0]]["Var"] = result[2]
                
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
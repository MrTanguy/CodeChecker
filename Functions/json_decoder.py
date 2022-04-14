import json

def decodeFormat(language) :
    # Opening the json file of languages format
    json_file = open('./languages_format.json')

    # Return the data of the json object
    json_data = json.load(json_file)

    format_Dict = {}    
    for i in json_data :
        if(i.upper() == language) :
            for x in json_data[i] :
                format_Sub_Array = []
                temp_text = ""
                for char in range(len(json_data[i][x])) :
                    if(json_data[i][x][char]!="|") :
                        temp_text = temp_text + json_data[i][x][char]
                        if(char+1 == len(json_data[i][x])) :
                            format_Sub_Array.append(temp_text)
                    else :
                        format_Sub_Array.append(temp_text)
                        temp_text = ""
                format_Dict[x]=(format_Sub_Array)
    return format_Dict



from Functions.json_decoder import decodeFormat
import inspect

Commentary_Content = []
Var_Content = []
Equal_Content = []
Loop_Content = []
Functions_Content = []

Sample_Content_Double = []
Sample_Content_Without_CommsLoops = []
Sample_Content_Without_CommsLoopsVar = []
Sample_Content_Without_CommsLoopsVarFunc = []

All_Content = []
All_Content_Name = []


def run(sample_c, sample_f): 
    for index in range(len(sample_f)) :
        increment_text = False
        temp_text = ""
        for j in range(len(sample_f[index])) :
            if(increment_text) :
                temp_text += (sample_f[index][j]).upper()
            if(sample_f[index][j] == ".") :
                increment_text = True
        format_dict = decodeFormat(temp_text)
        PurgeCommentary(format_dict['com'],format_dict['extended_com'],index , sample_c)
        PurgeLoops(format_dict['loop'],index)
        PurgeVariables(format_dict['var'],index)
        PurgeFunctions(format_dict['function'], index)
        CheckStruct(format_dict, index , sample_c, sample_f)
        
    print(Loop_Content)
        
    All_Content.append(Commentary_Content)
    All_Content.append(Var_Content)
    All_Content.append(Loop_Content)
    All_Content.append(Functions_Content)

    All_Content_Name.append("Commentary")
    All_Content_Name.append("Loop")
    All_Content_Name.append("Var")     
    return All_Content, All_Content_Name
    

def PurgeCommentary(com_format,ext_com_format, syntax, sample_contents) :
    Sample_ContentsBis = sample_contents[syntax].splitlines(True)
    Sample_Content_SubFile = []
    Commentary_SubFile = []
    Long_Comment = False
    Append_Lines = False    
    Stop_Ext_Com = "None"
    for lines in Sample_ContentsBis :
        for syntax in com_format :
            for ext in ext_com_format :
                if(Stop_Ext_Com in lines):
                    Long_Comment = False
                    Append_Lines = True
                if(Long_Comment) :
                    Append_Lines = True
                if(syntax in lines) :
                    Append_Lines = True
                if(ext in lines):
                    Append_Lines = True
                    Long_Comment = True
                    if(ext=="/*") :
                        Stop_Ext_Com = "*/"
        if(Append_Lines == False and Stop_Ext_Com not in lines and Long_Comment == False):
            Sample_Content_SubFile.append(lines)
        if(Append_Lines and Long_Comment == False) :
            Commentary_SubFile.append(lines)
            Append_Lines = False
        elif(Append_Lines and Long_Comment) :
            Commentary_SubFile.append(lines)
    Sample_Content_Double.append(Sample_Content_SubFile)
    Commentary_Content.append(Commentary_SubFile)
    
    
def PurgeLoops(format, index) :
    Sample_Content_SubFile = []
    Loop_SubFile = []
    IsLoop = False
    Append_Lines = False
    Stop_Loop_Text = "None"
    for lines in Sample_Content_Double[index] :
        for syntax in format :
            if(Stop_Loop_Text in lines):
                Append_Lines = True
                IsLoop = False
            if(IsLoop) :
                Append_Lines = True
            if(syntax in lines) :
                Append_Lines = True
                IsLoop = True
                if(syntax=="{") :
                    Stop_Loop_Text = "}"
        if(Append_Lines == False and Stop_Loop_Text not in lines and IsLoop == False):
            Sample_Content_SubFile.append(lines) 
        if(Append_Lines and IsLoop == False) : 
            Loop_SubFile.append(lines)
            Append_Lines = False
        elif(Append_Lines and IsLoop) :
            Loop_SubFile.append(lines)
    Sample_Content_Without_CommsLoops.append(Sample_Content_SubFile)
    Loop_Content.append(Loop_SubFile)
    
    
def PurgeVariables(format, index) :
    Sample_Content_SubFile = []
    Var_SubFile = []
    Append_Lines = False
    for lines in Sample_Content_Without_CommsLoops[index] :
        for syntax in format : 
            if(syntax in lines) :
                Append_Lines = True
        if(Append_Lines) :
            Var_SubFile.append(lines)
            Append_Lines = False
        else :
                Sample_Content_SubFile.append(lines)
    Sample_Content_Without_CommsLoopsVar.append(Sample_Content_SubFile)
    Var_Content.append(Var_SubFile)    
    
    
Code_Struct = {}
def CheckStruct(format_dict, syntax, sample_contents, sample_files) :
    Var_Index = []
    Loop_Index = []
    Com_Index = []
    append_Lines_Var = False
    append_Lines_Loop = False
    append_Lines_Com = False
    long_Com = False
    stop_LC = "None"
    Sample_ContentsBis = sample_contents[syntax].splitlines(True)
    for index in range(len(Sample_ContentsBis)) :
        for exc in format_dict['var'] :
            if(exc in Sample_ContentsBis[index]) :
                append_Lines_Var = True
        for exc in format_dict['loop'] :
            if(exc in Sample_ContentsBis[index]) :
                append_Lines_Loop = True
                
        for exc in format_dict['com'] :
            if(exc in Sample_ContentsBis[index]) :
                append_Lines_Com = True
                
        if(Sample_ContentsBis[index] == stop_LC) :
            long_Com = False
            append_Lines_Com = True
            
        if(long_Com == True):
            append_Lines_Com = True
            
        for exc in format_dict['extended_com'] :
            if(exc in Sample_ContentsBis[index]) :
                append_Lines_Com = True
                long_Com = True
                if(exc=="/*"):
                    stop_LC = "*/"
                    
        if(append_Lines_Var) :
            Var_Index.append(str(index))
            append_Lines_Var = False 
        if(append_Lines_Loop) :
            Loop_Index.append(str(index))
            append_Lines_Loop = False
        if(append_Lines_Com and long_Com == False) : 
            Com_Index.append(str(index))
            append_Lines_Com = False
        elif(append_Lines_Com and long_Com ==True) : 
            Com_Index.append(str(index))
            append_Lines_Com = False
            
    Code_Struct[sample_files[syntax]] = {"VAR": Var_Index, "LOOP" : Loop_Index, "COM": Com_Index}
    
    
    
def PurgeFunctions(format, index) :
    Sample_Content_SubFile = []
    Functions_SubFile = []
    Append_Lines = False
    InFunc = False
    for lines in Sample_Content_Without_CommsLoopsVar[index] :
        if( lines.startswith(" ") and InFunc ) :
            Append_Lines = True
        elif( not lines.startswith(" ") and InFunc ) :
            InFunc = False
            Append_Lines = False
        for syntax in format : 
            if(syntax in lines) :
                InFunc = True
                Append_Lines = True
        if(Append_Lines) :
            Functions_SubFile.append(lines)
            Append_Lines = False
        else :
                Sample_Content_SubFile.append(lines)
    Sample_Content_Without_CommsLoopsVarFunc.append(Sample_Content_SubFile)
    Functions_Content.append(Functions_SubFile)

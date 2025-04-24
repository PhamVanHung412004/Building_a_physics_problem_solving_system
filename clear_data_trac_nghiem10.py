from read_file import Read_File_Json
from save_file_json import Save_File_Json
from package import (
    Path,
    json
)

from solution_string import solution

from gen import Answer_Question_From_Documents

def char_test(char : str):
    return 65 <= ord(char) and ord(char) <= 65 + 32

def check_char(vector_answer : list[str]) -> bool:
    cnt = 0
    for i in range(len(vector_answer[1 : ])):
        char = vector_answer[i][0]
        if (char_test(char)):
            cnt += 1
            
    return True if (cnt >= 2 and cnt <= 4) else False

def check_char_index(vector_answer : list[str], char : str) -> str:
    index = -1
    for i in range(len(vector_answer)):
        if (char_test(vector_answer[i][0])):
            if (vector_answer[i][0] == char):
                index = i
                break
    return vector_answer[index]

def get_char(text : str) -> str:
    
    for i in range(len(text) - 1, -1, -1):
        if (char_test(text[i])):
            return i
        

def index_char_true(vector : list) -> str:
    index = -1    
    for i in range(len(vector)):
        if ("đúng" in vector[i][1 : ] or "Đúng" in vector[i][1 : ]):
                index = i
                break       
    return vector[index]

def main():
    path_json = Path(__file__).parent / "500_trac_nghiem_10.json"
    path_json_save = Path(__file__).parent / "data_clean_fine_turning.json"
    
    datas = Read_File_Json(path_json).Read()  
    data_all = []
    cnt = 0
    for data in datas:
        datas_new = {}
        question = data["cau_hoi"]
        question = question.split("\n")
        text = "\n".join(question[1 : ])
        
        index = -1
        for i in range(len(question[0])):
            if (question[0][i] == '.' or question[0][i] == ':'):
                index = i
                break
            
        question[0] = question[0][index + 2: ]
        datas_new["cau_hoi"] = question[0]
        datas_new["cac_dap_an"] = text
        
        answers = data["dap_an"]

        vector_answers = []
        for ans in answers:
            text_new = solution(ans)
            if (text_new != "1"):
                vector_answers.append(text_new)
            else:
                print("error")
        datas_new["giai_thich"] = vector_answers
        
        Save_File_Json(str(path_json_save),datas_new).save()            
        cnt += 1
        # data_all.append(datas_new)
    print(cnt)
main()
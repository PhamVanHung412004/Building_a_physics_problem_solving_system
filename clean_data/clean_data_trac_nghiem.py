from add_path import add
add()
from read_file import Read_File_Json
from save_file_json import Save_File_Json
from package import (
    Path,
    json,
    Dict,
    re
)
from solution_string import (
    solution,
    clean_mathml
)

def char_test(char : str):
    '''
    char : kí tự muốn kiểm tra
    '''
    return 65 <= ord(char) and ord(char) <= 65 + 32

def check_char(vector_answer : list[str]) -> bool:
    '''
    vector_answer : chứa danh sách các câu trả lời
    '''
    cnt = 0
    for i in range(len(vector_answer[1 : ])):
        char = vector_answer[i][0]
        if (char_test(char)):
            cnt += 1
            
    return True if (cnt >= 2 and cnt <= 4) else False

def check_char_index(vector_answer : list[str], char : str) -> str:
    '''
    vector_answer : chứa danh sách các câu trả lời
    char : kí tự đáp án đúng của câu đấy
    '''
    index = -1
    for i in range(len(vector_answer)):
        if (char_test(vector_answer[i][0])):
            if (vector_answer[i][0] == char):
                index = i
                break
    return vector_answer[index]

def get_char(text : str) -> str:    
    '''
    text : từng đoạn văn bản trong danh sách các câu trả lời
    '''
    for i in range(len(text) - 1, -1, -1):
        if (char_test(text[i])):
            return i
        

def index_char_true(vector : list) -> str:
    '''
    vector : chứa các danh sach câu trả lời
    '''
    index = -1    
    for i in range(len(vector)):
        if ("đúng" in vector[i][1 : ] or "Đúng" in vector[i][1 : ]):
                index = i
                break       
    return vector[index]


def convert_dict(options_raw : Dict[str , str]) -> Dict[str , str]:
    options = {}
    for line in options_raw:
        match = re.match(r"([A-D])\.\s*(.*)", line)
        if match:
            options[match.group(1)] = match.group(2).strip()

    return options

# kiểm tra xem kí tự in hoa tìm được có hợp lệ hay không
def range_char(char : str) -> bool:
    table_char = ['A', 'B', 'C', 'D']    
    return char in table_char

def check_value(string : str) -> tuple:
    index = -1
    oke = False
    for i in range(len(string)):
        if (char_test(string[i])):
            index = i 
            oke = True
            break                             
    return (oke,index)

def check(options : Dict[str , str]) -> Dict[str , str]:
    dict_new = {}
    for key, value in options.items():
        oke, index = check_value(value)
        if (oke and range_char(value[index])):
            title1 = value[ : index]
            dict_new[key] = title1
            dict_new[value[index]] = value[index + 1 : ]            
        else:
            dict_new[key] = value
    
    value_dict_tmp = dict(sorted(dict_new.items()))
    return value_dict_tmp


def dict_to_text(data : Dict[str, str]) -> list[str]:
    return [key + "." + value for key, value in data.items()]

def main():
    cleaned_data = []
    cnt = 0
    for i in range(10,13):
        path_json = Path(__file__).parent / "500_cau_hoi_trac_nghiem" / "500_trac_nghiem_{}.json".format(i)
        datas = Read_File_Json(path_json).Read()  
        data_all = []
        print("file json lop: {}".format(i))
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
            data_all.append(datas_new)
            # print(?"cau thu: {}".format(cnt))
            # cnt += 1

        for item in data_all:
            question = item["cau_hoi"].strip()

            # Xử lý đáp án: gom các dòng multiline theo đáp án
            options_raw = item["cac_dap_an"].split('\n')
            options = {}
            current_key = None
            current_text = []

            for line in options_raw:
                match = re.match(r"^([A-D])\.\s*$", line.strip())  # Chỉ chứa "A.", "B.",...
                if match:
                    # Lưu đáp án trước đó nếu có
                    if current_key is not None:
                        options[current_key] = " ".join(current_text).strip()
                    # Bắt đầu đáp án mới
                    current_key = match.group(1)
                    current_text = []
                elif current_key:
                    current_text.append(line.strip())

            # Đừng quên lưu đáp án cuối cùng
            if current_key is not None:
                options[current_key] = " ".join(current_text).strip()
            
            
            # Gộp giải thích lại
            explanation = "\n".join([line.strip() for line in item["giai_thich"]])
            
            if (len(options) == 0):
                options = convert_dict(options_raw)
            else:
                options = check(options)
            
            result = "\n".join(dict_to_text(options))
                
            check_oke = False
            for i in range(len(question)):
                if (question[i] == '?'):
                    check_oke = True 
                    break    
            if (not check_oke):
                question += '?'

            cleaned_data.append({
                "title" : "trac nghiem",
                "cau_hoi": question,
                "cac_lua_chon": result,
                "giai_thich": explanation
            })
            # print("Cau thu: {}".format())
            cnt += 1

    path_json_save = Path(__file__).parent / "data_fine_turning" /  "data_fine_turning.json"
    Save_File_Json(str(path_json_save),cleaned_data).save()            
    print("luu thanh cong voi tong so cau la: {}".format(cnt))
main()


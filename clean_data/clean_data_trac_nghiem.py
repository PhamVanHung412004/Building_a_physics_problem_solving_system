from add_path import add
add()

from read_file import Read_File_Json
from save_file_json import Save_File_Json

from package import (
    Path,
    re,
    BeautifulSoup
)

from solution_string import (
    solution,
    clean_choice,
    convert_dict,
    check,
    dict_to_text,
    string_seach_character,
    clean_text_with_mathml,
    check_charactor,

)

def remove_string(string_after : str, string_before : str) -> str:
    '''
    string_after : xau khi tu sau khi lam sach la cong thuc toan
    string_before : xau khi tu truoc khi chua lam sach

    '''
    print(string_after)
    # ki tu dau tien sau khi lam sach
    char_begin = string_after[0]
    index = -1
    for i in range(len(string_before)):
        if (string_before[i] == char_begin):
            index = i
            break
    return string_before[: index]


def convert_charactor(string : str) -> str:
    if (check_char(string[0]) and string[1] == ')'):
        return chr(ord(string) - 32) + "." + string[2: ]
def main():    

    cleaned_data = []
    cnt = 0
    for i in range(10,13):
        path_json = Path(__file__).parent / "500_cau_hoi_trac_nghiem" / "500_trac_nghiem_{}.json".format(i)
        datas = Read_File_Json(path_json).Read()  
        print("file json lop: {}".format(i))
        cnt = 0
        for data in datas:
            print("Cau so:",cnt)
            datas_new = {}
            question = data["cau_hoi"]
            index = -1
            for i in range(len(question)):
                if (question[i] == ':'):
                    index = i
            if (index != -1):
                question = question[index + 1: ]

            question = question.split("\n")

            # khi ma so luong danh sach cau hoi sau 
            # khi chia bang 1 thi tuc la khong co lua chon
            # ta quy do la thuoc title bai tap
            if (len(question) == 1):                
                datas_new["title"] = "bai tap"
                datas_new["cau_hoi"] = question[0] 
                texts = data["dap_an"]   
                text_news = [clean_text_with_mathml(text[solution(text)[0] : solution(text)[1] + 1]) if (solution(text) != (-1,-1)) else text for text in texts]                                          
                datas_new["giai_thich"] = "\n".join(text_news)   
            # khi ma so luong danh sach tu 2 do len 
            # tuc la co 1 cau va co dap an lua chon
            # ta quy ve do la cau hoi trac nghiem
            else:
                datas_new["title"] = "trac nghiem"
                datas_new["cau_hoi"] = question[0]
                selection_choice = question[1 : ]    
                
                for i in range(len(selection_choice)):
                    if (check_charactor(selection_choice[i]) != '-1'):
                        selection_choice[i] = check_charactor(selection_choice[i])


                options = clean_choice(selection_choice)

                if (len(options) == 0):
                    options = convert_dict(selection_choice)
                else:
                    options = check(options)

                dict_to_list = dict_to_text(options)
                datas_new["cac_lua_chon"] = dict_to_list

                list_answers = data["dap_an"]                
                vector_text = []
                for i in range(len(list_answers)):
                    left, right = solution(list_answers[i])
                    if (left != -1 and right != -1):
                        char_begin = list_answers[0]
                        char_end = list_answers[-1]
                        if (list_answers[i] == list_answers[i][left : right + 1]):
                            vector_text.append(list_answers[i])
                        else:
                            string_end = clean_text_with_mathml(list_answers[i][left : right + 1])
                            string_begin = string_seach_character(string_end[0],list_answers[i][ : left])
                            vector_text.append(string_begin + string_end)
                    else:    
                        vector_text.append(list_answers[i])
                text_beautiful = "\n".join(vector_text)
                datas_new["giai_thich"] = text_beautiful
                cnt += 1
            cleaned_data.append(datas_new)

    path_save_data = Path(__file__).parent / "data_fine_turning" / "data_trac_nghiem.json"            
    Save_File_Json(str(path_save_data),cleaned_data).save()
    print("save file sussufully")
main()

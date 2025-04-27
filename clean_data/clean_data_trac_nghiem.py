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
    clean_mathml,
    clean_choice,
    convert_dict,
    check,
    dict_to_text,
    fix_spacing_and_comma,
    string_seach_character
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
def main():    

    cleaned_data = []
    cnt = 0
    for i in range(11,13):
        path_json = Path(__file__).parent / "500_cau_hoi_trac_nghiem" / "500_trac_nghiem_{}.json".format(i)
        datas = Read_File_Json(path_json).Read()  
        print("file json lop: {}".format(i))
        for data in datas:
            datas_new = {}
            question = data["cau_hoi"]
            question = question.split("\n")

            index = -1
            for i in range(len(question[0])):
                if (question[0][i] == '.' or question[0][i] == ':'):
                    index = i
                    break

            question[0] = question[0][index + 2: ]

            # kiem tra xem co dau ? o cuoi cau hay khong neu khong co thi them dau hoi vao ?

            '''
            khi ma so luong danh sach cau hoi sau 
            khi chia bang 1 thi tuc la khong co lua chon
            ta quy do la thuoc title bai tap
            '''
            if (len(question) == 1):                
                datas_new["title"] = "bai tap"
                datas_new["cau_hoi"] = question[0]    
                text_news = [clean_mathml(text[solution(text)[0] : solution(text)[1] + 1]) if (solution(text) != (-1,-1)) else text for text in texts]                                          
                datas_new["giai_thich"] = "\n".join(text_news)   

            # '''
            # khi ma so luong danh sach tu 2 do len 
            # tuc la co 1 cau va co dap an lua chon
            # ta quy ve do la cau hoi trac nghiem
            # '''
            else:                            
                datas_new["title"] = "trac nghiem"
                datas_new["cau_hoi"] = question[0]
                selection_choice = question[1 : ]    
                options = clean_choice(selection_choice)

                if (len(options) == 0):
                    options = convert_dict(selection_choice)
                else:
                    options = check(options)

                dict_to_list = dict_to_text(options)

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
                            print("left:",left , "right:", right)
                            string_end = clean_mathml(list_answers[i][left : right + 1])
                            # print("string clean:",fix_spacing_and_comma(string_end))

                            string_begin = string_seach_character(string_end,list_answers[i][left : right + 1])
                            print("string begin:",string_begin)
                            # print(string_begin + string_end)
                            # string_beautiful = char_math_begin + char_math_last
                        # vector_text.append(string_beautiful)
                    else:    
                        print("string before:",list_answers[i])
                #         vector_text.append(list_answers[i])
                # text_beautiful = "\n".join(vector_text)

            #     datas_new["cac_lua_chon"] = dict_to_list
            #     datas_new["giai_thich"] = text_beautiful
            # cleaned_data.append(datas_new)
    
        # check_oke = False
        # for i in range(len(question[0])):
        #     if (question[0][i] == '?'):
        #         check_oke = True 
        #         break    
        # if (not check_oke):
        #     question[0] += '?'

        # cleaned_data.append({
        #     "title" : "trac nghiem",
        #     "cau_hoi": question,
        #     "cac_lua_chon": result,
        #     "giai_thich": explanation
        # })
        # print("Cau thu: {}".format())
            # cnt += 1
        print(cleaned_data)
main()

# -*- coding: utf-8 -*-
from add_path import add
add()
import re
from package import Path,json

from read_file import Read_File_Json
from solution_string import (
    convert_doube_string_from_string,
    clean_choice,
    check_value
)
def clean_question(text):
    text = text.replace("\n","")
    index = re.search(":",text).start()
    # t = ""
    # for i in range(index+2,int((len(text)-index)/2)):
    #     t = t + text[i]
    # text = text[index+2:]
    # t = text.split()
    # ds = []
    # for i in
    return text[index+2:int((len(text)-index)/2)]


def clean_answer(text):
    # text = text.replace("\n","")
    vector_array = text.split()
    check = set()
    vecto_new = []

    for vecto in vector_array:
        if len(vecto)>=0:
            if vecto not in check:
                vecto_new.append(vecto)
                check.add(vecto)
    string =""
    last = []
    for vecto in vecto_new:
        if str(vecto) not in string:
            string +=str(vecto)
            last.append(vecto)
   
    text_beautiful = " ".join(last)
    return text_beautiful
    
        


    # return text_last
    # set_check = set()

    # vector_text_new = []

    # for i in vector_array:
    #     if (i not in set_check):
    #         vector_text_new.append(i)
    #         set_check.add(i)

    # text_beautiful = " ".join(vector_text_new)
    # return text_beautiful
def main():
    path = Path(__file__).parent / "data_practice" / "bai_tap_10.json"
    data_json = Read_File_Json(str(path)).Read()
    data_new_tmp = {}
    for data in data_json:
        text = data["loi_giai"]
        # text_convert = text.split()
        # text_new_tmp = " ".join(text_convert)
        # data_new_test = text_new_tmp.split("Lời giải: Lời giải:")

        text_test = check_value(text)
        print(text_test)
        # # print("-" * 40)
        # for i in range(len(data_new_test)):
        #     if (data_new_test[i] != ' '):
        #         text_test = convert_doube_string_from_string(data_new_test[i])
                # print(text_test)
        # print("-" * 40)

main()
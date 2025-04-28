# -*- coding: utf-8 -*-
from add_path import add
add()
import re
from package import Path,json

from read_file import Read_File_Json
from solution_string import (
    solution_double_string,
    convert_conthuc,
    smart_clean
)


# def clean_question(text):
#     text = text.replace("\n","")
#     index = re.search(":",text).start()
#     # t = ""
#     # for i in range(index+2,int((len(text)-index)/2)):
#     #     t = t + text[i]
#     # text = text[index+2:]
#     # t = text.split()
#     # ds = []
#     # for i in
#     return text[index+2:int((len(text)-index)/2)]


# def clean_answer(text):
#     # text = text.replace("\n","")
#     vector_array = text.split()
#     check = set()
#     vecto_new = []

#     for vecto in vector_array:
#         if len(vecto)>=0:
#             if vecto not in check:
#                 vecto_new.append(vecto)
#                 check.add(vecto)
#     string =""
#     last = []
#     for vecto in vecto_new:
#         if str(vecto) not in string:
#             string +=str(vecto)
#             last.append(vecto)
   
#     text_beautiful = " ".join(last)
#     return text_beautiful
    
        


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
    cnt = 0
    for data in data_json:
        # if (cnt == 1): break
        text = data["loi_giai"]
        # text = " Lời giải: Lời giải: Số liệu tham khảo Bảng 3.1 n\ns (m)\n∆s (m)\nt (s)\n∆t (m)\n1\n0,649\n0,0024\n3,49\n0,024\n2\n0,651\n0,0004\n3,51\n0,004\n3\n0,654\n0,0026\n3,54\n0,026\n4\n0,653\n0,0016\n3,53\n0,016\n5\n0,650\n0,0014\n3,50\n0,014\nTrung bình\n¯\ns\n= 0,6514\n¯¯¯¯¯\nΔ\ns\n= 0,00168\n¯\nt\n= 3,514\n¯¯¯¯¯\nΔ\nt\n= 0,0168 n\ns (m)\n∆s (m)\nt (s)\n∆t (m)\n1\n0,649\n0,0024\n3,49\n0,024\n2\n0,651\n0,0004\n3,51\n0,004\n3\n0,654\n0,0026\n3,54\n0,026\n4\n0,653\n0,0016\n3,53\n0,016\n5\n0,650\n0,0014\n3,50\n0,014\nTrung bình\n¯\ns\n= 0,6514\n¯¯¯¯¯\nΔ\ns\n= 0,00168\n¯\nt\n= 3,514\n¯¯¯¯¯\nΔ\nt\n= 0,0168 n\ns (m)\n∆s (m)\nt (s)\n∆t (m)\n1\n0,649\n0,0024\n3,49\n0,024\n2\n0,651\n0,0004\n3,51\n0,004\n3\n0,654\n0,0026\n3,54\n0,026\n4\n0,653\n0,0016\n3,53\n0,016\n5\n0,650\n0,0014\n3,50\n0,014\nTrung bình\n¯\ns\n= 0,6514\n¯¯¯¯¯\nΔ\ns\n= 0,00168\n¯\nt\n= 3,514\n¯¯¯¯¯\nΔ\nt\n= 0,0168 n\ns (m)\n∆s (m)\nt (s)\n∆t (m) n n s (m) s (m) ∆s (m) ∆s (m) t (s) t (s) ∆t (m) ∆t (m) 1\n0,649\n0,0024\n3,49\n0,024 1 1 0,649 0,649 0,0024 0,0024 3,49 3,49 0,024 0,024 2\n0,651\n0,0004\n3,51\n0,004 2 2 0,651 0,651 0,0004 0,0004 3,51 3,51 0,004 0,004 3\n0,654\n0,0026\n3,54\n0,026 3 3 0,654 0,654 0,0026 0,0026 3,54 3,54 0,026 0,026 4\n0,653\n0,0016\n3,53\n0,016 4 4 0,653 0,653 0,0016 0,0016 3,53 3,53 0,016 0,016 5\n0,650\n0,0014\n3,50\n0,014 5 5 0,650 0,650 0,0014 0,0014 3,50 3,50 0,014 0,014 Trung bình\n¯\ns\n= 0,6514\n¯¯¯¯¯\nΔ\ns\n= 0,00168\n¯\nt\n= 3,514\n¯¯¯¯¯\nΔ\nt\n= 0,0168 Trung bình Trung bình ¯\ns\n= 0,6514 ¯\ns\n= 0,6514 ¯\ns ¯\ns ¯\ns ¯\ns ¯\ns ¯ ¯ ¯ s s s ¯¯¯¯¯\nΔ\ns\n= 0,00168 ¯¯¯¯¯\nΔ\ns\n= 0,00168 ¯¯¯¯¯\nΔ\ns ¯¯¯¯¯\nΔ\ns ¯¯¯¯¯\nΔ\ns ¯¯¯¯¯\nΔ\ns ¯¯¯¯¯\nΔ\ns ¯¯¯¯¯ ¯¯¯¯¯ ¯¯¯¯¯ ¯ ¯¯¯ ¯ Δ\ns Δ\ns Δ Δ s s ¯\nt\n= 3,514 ¯\nt\n= 3,514 ¯\nt ¯\nt ¯\nt ¯\nt ¯\nt ¯ ¯ ¯ t t t ¯¯¯¯¯\nΔ\nt\n= 0,0168 ¯¯¯¯¯\nΔ\nt\n= 0,0168 ¯¯¯¯¯\nΔ\nt ¯¯¯¯¯\nΔ\nt ¯¯¯¯¯\nΔ\nt ¯¯¯¯¯\nΔ\nt ¯¯¯¯¯\nΔ\nt ¯¯¯¯¯ ¯¯¯¯¯ ¯¯¯¯¯ ¯ ¯¯¯ ¯ Δ\nt Δ\nt Δ Δ t t a) Nguyên nhân gây ra sự sai khác giữa các lần đo là do: - Sai số hệ thống do dụng cụ đo. - Điều kiện làm thí nghiệm chưa được chuẩn. - Thao tác khi đo chưa chính xác. b) Phép đo s Phép đo s - Giá trị trung bình của quãng đường: - Sai số ngẫu nhiên tuyệt đối của từng lần đo: - Sai số ngẫu nhiên tuyệt đối trung bình của 5 lần đo: - Sai số tuyệt đối của phép đo quãng đường là: ∆s =\n¯¯¯¯¯\nΔ\ns\n+\nΔ\ns\nd\nc\n= 0,00168 +\n0\n,\n001\n2\n= 0,00218 (m) ¯¯¯¯¯\nΔ\ns\n+\nΔ\ns\nd\nc ¯¯¯¯¯\nΔ\ns\n+\nΔ\ns\nd\nc ¯¯¯¯¯\nΔ\ns\n+\nΔ\ns\nd\nc ¯¯¯¯¯\nΔ\ns ¯¯¯¯¯\nΔ\ns ¯¯¯¯¯ ¯¯¯¯¯ ¯¯¯¯¯ ¯ ¯¯¯ ¯ Δ\ns Δ\ns Δ Δ s s + + Δ Δ s\nd\nc s s s d\nc d\nc d d c c 0\n,\n001\n2 0\n,\n001\n2 0\n,\n001\n2 0\n,\n001\n2 0\n,\n001\n2 0\n,\n001 0\n,\n001 0 0 , , 001 001 2 2 2 Phép đo t Phép đo t - Giá trị trung bình của thời gian chuyển động - Sai số ngẫu nhiên tuyệt đối của từng lần đo: - Sai số ngẫu nhiên tuyệt đối trung bình của 5 lần đo: - Sai số tuyệt đối của phép đo thời gian là: ∆t =\n¯¯¯¯¯\nΔ\nt\n+\nΔ\nt\nd\nc\n= 0,0168 +\n0\n,\n01\n2\n= 0,0218 (m) ¯¯¯¯¯\nΔ\nt\n+\nΔ\nt\nd\nc ¯¯¯¯¯\nΔ\nt\n+\nΔ\nt\nd\nc ¯¯¯¯¯\nΔ\nt\n+\nΔ\nt\nd\nc ¯¯¯¯¯\nΔ\nt ¯¯¯¯¯\nΔ\nt ¯¯¯¯¯ ¯¯¯¯¯ ¯¯¯¯¯ ¯ ¯¯¯ ¯ Δ\nt Δ\nt Δ Δ t t + + Δ Δ t\nd\nc t t t d\nc d\nc d d c c 0\n,\n01\n2 0\n,\n01\n2 0\n,\n01\n2 0\n,\n01\n2 0\n,\n01\n2 0\n,\n01 0\n,\n01 0 0 , , 01 01 2 2 2 c) Viết kết quả đo - Phép đo s: s =\n¯\ns\n± ∆s = 0,6514 ± 0,00218 (m) ¯\ns ¯\ns ¯\ns ¯\ns ¯\ns ¯ ¯ ¯ s s s - Phép đo t: t =\n¯\nt\n± ∆t = 3,514 ± 0,0218 (m) ¯\nt ¯\nt ¯\nt ¯\nt ¯\nt ¯ ¯ ¯ t t t"        
        vector_text = text.split()
        text_new = " ".join(vector_text)
        
        text_new = text_new.replace(":",".")
        vector_data = text_new.split(".")
        print(vector_data) 
        # text_index = solution_double_string(text_new)
        # print(text_index)
        # print(text_index)
        # # print("-" * 40)
        # for i in range(len(data_new_test)):
        #     if (data_new_test[i] != ' '):
        #         text_test = convert_doube_string_from_string(data_new_test[i])
                # print(text_test)
        # print("-" * 40)

main()
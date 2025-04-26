from add_path import add 
add()

from package import (
    Path
)
from read_file import (
    Read_File_Json
)

def convert_dapan(text : str) -> str:
    begin = -1
    for i in range(len(text)):
        if (text[i] == ':' and text[i - 8: i] == "Lời giải"):
            begin = i      

    text = text.replace(text[: begin + 1], "")
    return text

def convert_cauhoi(text : str) -> str:
    oke = False
    index = None
    for i in range(len(text)):
        if (text[i] == '?' or text[i] == '.'):
            oke = True            
            index = i
    if (index != None):
        text = text.replace(text[index + 1: ],"")
    begin = -1
    for i in range(len(text)):
        if (text[i] == ':' and (text[i - 2: i] == "10" or text[i - 2:  i] == "11" or text[i - 2:  i] == "12")):
            begin = i
    text = text.replace(text[: begin + 1] , "")
        
    return text
def main():
    path = Path(__file__).parent / "data_practice" / "bai_tap_10.json"

    datas = Read_File_Json(str(path)).Read()
    
    datas_all = []    
    for item in datas:
        datas_dict = {}    
        datas_dict["title"] = "bai tap"
        for key, value in item.items():
            if (key == "cau_hoi"):
                datas_dict["cau_hoi"] = convert_cauhoi(value)                    
            
            else:
                datas_dict["dap_an"] = convert_dapan(value)
                    
        datas_all.append(datas_dict)
    print(datas_all[0])

main()




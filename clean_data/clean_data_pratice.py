from add_path import add 
add()

from package import (
    Path
)
from read_file import (
    Read_File_Json
)
def convert_text(text : str):
    index = text.index(":")
    return text[index + 1 : ]

def main():
    path = Path(__file__).parent / "data_practice" / "bai_tap_10.json"

    datas = Read_File_Json(str(path)).Read()
    
    data_dict = [ {"title" : "ly thuyet", "cau_hoi" : convert_text(value)} for item in datas for key, value in item.items()]
    for item in datas:
        datas_dict = {}        
        for key, value in item.items():
            datas_dict["title"] = "ly thuyet"
            datas_dict["cau_hoi"] = convert_text(value)
            datas_dict["dap_an"] = convert_text(value)
    print(datas_dict[0])
main()




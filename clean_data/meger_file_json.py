
from add_path import add
add()
from package import (
    Path,
    os
)
from read_file import Read_File_Json
from save_file_json import Save_File_Json
def main():
    path = "data_fine_turning"
    list_name_file = os.listdir(path)
    datas = []
    cnt = 0
    for name in list_name_file:
        path_new = path + "/" + name
        data = Read_File_Json(path_new).Read()
        print("name file",name)
        for i in data:
            cnt += 1
            datas.append(i)
    path_save = "data_fine_turning/datas.json"
    Save_File_Json(path_save,datas).save()
    
main()
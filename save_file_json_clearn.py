from read_file import Read_File_Json
from package import (
    Path,
    Dict
)
from save_file_json import Save_File_Json
from read_file import Read_File_Json
def solution(dict_new : Dict[str, str]) -> Dict[str, str]:
    datas_question_answers = dict_new["content"]
    data_new = {}

    for key, value in datas_question_answers.items():
        key += "?"
        data_new[key] = value
    return data_new

def convert(value_dict : Dict[str, str]) -> Dict[str, str]:
    pass

def main():
    file_path_read_file_json = Path(__file__).parent / "input.json" 
    file_path_save_file_json_tmp = Path(__file__).parent / "output_tmp.json" 
    data = Read_File_Json(str(file_path_read_file_json)).Read()

    data_new = [solution(dict_value) for dict_value in data]
    vector_data = [ convert(i) for i in data_new]
    Save_File_Json(str(file_path_save_file_json_tmp), data_new).save()
main()


from package import (
    Dict,
    os,
    Path,
    json
)

from read_file import Read_File_Json
from save_file_json import Save_File_Json


def solution(dict_new : Dict[str, str]) -> Dict[str, str]:    
    datas_question_answers = dict_new["content"]
    data_new = {}

    for key, value in datas_question_answers.items():
        key += "?"
        data_new[key] = value
    return data_new

def main():
    file_path_read_file_json = Path(__file__).parent / "data_theory"
    file_path_save_file_json = Path(__file__).parent / "data_fine_turning" / "data_theory.json"
    vector_list_dir = os.listdir(file_path_read_file_json)    
    data = [solution(text) for path in vector_list_dir for text in Read_File_Json(file_path_read_file_json / path).Read()]
    datas = { key : value for vector_question in data for key, value in vector_question.items()}
    Save_File_Json(str(file_path_save_file_json),datas).save()

main()


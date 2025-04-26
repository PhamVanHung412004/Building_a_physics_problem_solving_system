from add_path import add
add()
from package import (
    Dict,
    os,
    Path,
    json,
    re
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
# Hàm làm sạch từng đoạn văn bản

def clean_text(text):
    # Ghép công thức Q = mcΔT
    text = text.replace('\n', ' ')
    text = re.sub(r'\bQ m c Δ T\b', 'Q = mcΔT', text)
    text = re.sub(r'\bc = Q m Δ T\b', 'c = Q / (mΔT)', text)
    text = re.sub(r'\bλ = Q m\b', 'λ = Q / m', text)
    text = re.sub(r'\bL = Q m\b', 'L = Q / m', text)
    # Xoá khoảng trắng thừa
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def main():
    file_path_read_file_json = Path(__file__).parent / "data_theory"
    file_path_save_file_json = Path(__file__).parent / "data_fine_turning" / "data_theory.json"
    vector_list_dir = os.listdir(file_path_read_file_json)    
    data = [solution(text) for path in vector_list_dir for text in Read_File_Json(file_path_read_file_json / path).Read()]
    datas = { key : value for vector_question in data for key, value in vector_question.items()}
    
    cleaned_data = {k: clean_text(v) for k, v in datas.items()}
    
    data_best = []
    for key, value in cleaned_data.items():
        dict_value = {}
        dict_value["title"] = "ly thuyet"
        dict_value["cau_hoi"] = key
        dict_value["dap_an"] = value
        data_best.append(dict_value)
    
    Save_File_Json(str(file_path_save_file_json),data_best).save()
    # with open("data_theory_cleaned.json", "w", encoding="utf-8") as f:
    #     json.dump(cleaned_data, f, ensure_ascii=False, indent=4)
main()


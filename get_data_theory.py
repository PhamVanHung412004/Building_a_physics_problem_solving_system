# from add_path import add
# add()
import json
import numpy as np
from sentence_transformers import SentenceTransformer
# from read_file import Read_File_Json
# from Embedding_data import Get_Embedding
# from package import (
#     Path,
#     faiss
# )


def main():
    datas = [
    {
        "title": "ly thuyet",
        "cau_hoi": "anh anh ơi anh à",
        "giai_thich": "không có"
    },
    {
        "title": "bai tap",
        "cau_hoi": "2+2 bằng mấy?",
        "giai_thich": "bằng 4"
    }
]
    datas_theory = [data["cau_hoi"]
    # {data["cau_hoi"]: data["giai_thich"]}
    for data in datas
    if data["title"] == "ly thuyet"
]
    # thay bằng model khác all-MiniLM-L6-v2
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(datas_theory, convert_to_numpy=True)  
   
    embeddings_array = embeddings.tolist()
    
    with open("datas_theory.json", "w", encoding="utf-8") as f:
        json.dump(embeddings_array, f, ensure_ascii=False, indent=2)

    # luu vao file datas_theory.json
    
    # embedding -> dua vao vector Data
main()
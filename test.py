from pathlib import Path
from sentence_transformers import SentenceTransformer
from Embedding_data import Get_Embedding
from lasbels_points import Convert_Labels_Points
from save_file_json import Save_File_Json

from read_file import (
    Read_File_CSV,
    Read_File_WORD,
    Read_File_PDF,
)

from package import (
    Dict,
    NDArray,    
)


def check_path(path : str) -> 

    index = path.index('.')    
    if (path[index + 1: ] == "json"): return Read_File_Json(path).Read()
    elif (path[index + 1: ] == "docx"): return Read_File_WORD(path).Read()
    elif (path[index + 1: ] == "pdf"): return Read_File_PDF(path).Read()
    else:
        print("aaaaaaaaaa")
def main():
    path_json = Path(__file__).parent / "cau_hoi_vat_ly.json"
    path_word = Path(__file__).parent / "dataset"/ "BUỔI 13 - SÓNG CƠ.docx"
    path_pdf = Path(__file__).parent / "dataset"/ "ÔN TẬP GIỮA KÌ 2.pdf"
    path_csv = Path(__file__).parent / "a.csv"
    
main()
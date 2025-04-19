from pathlib import Path
from read_file import Read_File_WORD
from sentence_transformers import SentenceTransformer
from Embedding_data import Get_Embedding

from labels_points import Convert_Labels_Points

def main():
    path = Path(__file__).parent / "dataset/BUỔI 7 - LUYỆN TẬP DAO ĐỘNG ĐIỀU HOÀ.docx"
    print(Read_File_WORD(path).Read())
main()
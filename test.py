from pathlib import Path
from read_file import Read_File_WORD
def main():
    path = Path(__file__).parent/"dataset/BUỔI 7 - LUYỆN TẬP DAO ĐỘNG ĐIỀU HOÀ.docx"
    data = Read_File_WORD(path).Read()
    print(data)
main()
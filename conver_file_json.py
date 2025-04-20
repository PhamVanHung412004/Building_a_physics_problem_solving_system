from package import (
    json,
    Path
)

from save_file_json import Save_File_Json
from read_file import Read_File_Json


def main():
    path_dir = Path(__file__).parent / "output.json"
    path_dir_save = Path(__file__).parent / "output_new.json"
    data = Read_File_Json(str(path_dir)).Read()
    Save_File_Json(str(path_dir_save),data).save()
main()
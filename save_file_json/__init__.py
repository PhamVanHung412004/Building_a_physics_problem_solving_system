from labels_points import np
from typing import Dict
from read_file import Get_Path
import json

def convert_ndarray(obj):
    '''
    obj : Đối tượng bạn muốn chuyển dữ liệu
    '''
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, dict):
        return {k: convert_ndarray(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_ndarray(item) for item in obj]
    else:
        return obj

class Save_File_Json(Get_Path):
    def __init__(self,path : str, data : Dict[str , str]) -> None:
        super().__init__(path)
        '''
        path: Đường dẫn đầu vào
        data : Câu hỏi kèm theo câu trả lời lưu dưới dạng là một map key và value
        '''
        self.__data = data

    def save_file(self) -> None:
        with open(self.path , "w") as file:
            json.dump(convert_ndarray(self.__data), file, indent=4)




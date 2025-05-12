import sys
import os

# thêm path thủ công 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from package import (
    pandas as pd,
    Dict,
    json
)
class Get_Path:
    def __init__(self,path : str)->None:
        '''
        path: Đường dẫn đầu vào
        '''
        self.path = path

class Read_File_CSV(Get_Path):
    def __init__(self, path : str) -> None:
        super().__init__(path)
        '''
        Kế thừa đường dẫn từ class Get_Path
        '''
    
    def Read(self)-> pd:
        return pd.read_csv(self.path)
    
class Read_File_Json(Get_Path):
    def __init__(self, path : str) -> None:
        super().__init__(path)
    
    def Read(self):
        with open(self.path, 'r', encoding="utf-8") as file:
            data = json.load(file)
            return data
#  -> list[Dict[str, str | Dict[str, str]]]
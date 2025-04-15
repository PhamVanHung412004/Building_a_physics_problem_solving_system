import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from package import (
    numpy as np,
    NDArray,
    Dict,
    Save_File_Json,
    Get_Path
)

class Convert_Labels_Points(Get_Path):
    def __init__(self, path : str, data : NDArray[np.float32] , labels : NDArray[np.int32], n_clusters : int) -> None:
        '''
        path : đường dẫn đến thư mục cần lưu
        data : Là một vector chứa dữ liệu ban đầu chưa có nhãn
        labels : Nhãn của các điểm dữ liệu trong data
        n_clusters : số lượng cụm trung tâm
        '''
        super().__init__(path)
        self.__labels : NDArray[np.int32] = labels
        self.__data : NDArray[np.float32] = data
        self.__n_clusters = n_clusters
    
    def conver_array_to_dict(self) -> Dict[int , NDArray[np.float32]]:
        data_dict = {i : [] for i in range(self.__n_clusters)}

        for i in range(len(self.__labels)):
            data_dict[self.__labels[i]].append(self.__data[i])
        return data_dict
    
    def save_file_json(self) -> None:
        data_dict = self.conver_array_to_dict()
        Save_File_Json(self.path, data_dict).save_file()
    
    

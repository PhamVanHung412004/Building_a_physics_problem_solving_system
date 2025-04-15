import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from package import (
    numpy as np,
    NDArray,
    KMeans
)

class Build_KMeans:
    def __init__(self, n_clusters : int, data : NDArray[np.float32]) -> None:
        '''
        n_clusters : Số cụm muốn phân loại
        data : Là một vector chứa dữ liệu ban đầu chưa có nhãn
        '''
        self.__n_clusters : int = n_clusters        
        self.__data : NDArray[np.float32] = data

    def init_model(self):
        model = KMeans(n_clusters=self.__n_clusters, random_state=42)
        return model

    def run(self):
        return self.init_model().fit(self.__data)
    
    def get_labels(self) -> NDArray[np.int32]:
        return self.run().predict(self.__data)
    
    def get_center_points(self) -> NDArray[np.int32]:
        return self.run().cluster_centers_


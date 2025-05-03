from add_path import add
add()
from package import (
    numpy as np,
    NDArray,
    faiss
)
from Embedding_data import Get_Embedding

class VectorDB:
    def __init__(self, datas : list[str] | NDArray[float32]) -> None:
        '''
        datas : danh sach data da embedding
        '''
        self.__datas : list[str] | NDArray[str_] = datas

    def Init_VectorDB(self) -> NDArray[float32]:

        datats_embeddings = [data for data in self.__datas]
        index = faiss.IndexFlatL2(self.__datas)
        
        dimen = 384


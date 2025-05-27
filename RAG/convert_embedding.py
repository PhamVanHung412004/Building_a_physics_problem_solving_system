from .add_path import add
add()

from package import (
    ast,
    pandas as pd,
    numpy as np,
    NDArray
)

class Embedding_To_Numpy:   
    def __init__(self, array_embedding : pd.core.series.Series = None) -> None:
        '''
        array_embedding : vector embedding sau khi chunking cua tung doan
        '''
        self.__array_embedding : pd.core.series.Series = array_embedding

    def get_data(self):
        embedding : NDArray[np.int32] = self.__array_embedding.apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
        return embedding
    
    def convert_to_numpy(self) -> NDArray[np.int32]:
        return np.array(self.get_data().tolist())
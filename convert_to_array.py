from package import (
    pandas as pd,
    numpy as np,
    ast
)
class Embedding_To_Numpy:   
    def __init__(self, array_embedding : pd.core.series.Series = None) -> None:
        '''
        array_embedding : vector embedding sau khi chunking cua tung doan
        '''
        self.__array_embedding : pd.core.series.Series = array_embedding

    def get_data(self):
        embedding = self.__array_embedding.apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
        return embedding
    
    def convert_to_numpy(self) -> np.array:
        return np.array(self.get_data().tolist())
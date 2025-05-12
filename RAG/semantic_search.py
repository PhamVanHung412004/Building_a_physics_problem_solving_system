from .add_path import add
add()

from package import (
    numpy as np,
    Path,
    faiss,
    SentenceTransformer,
)
from .Input import Init_Input



class Sematic_search(Init_Input):
    def __init__(self,model : SentenceTransformer, vector_database : faiss, use_query : str, top_k : int) -> None:
        super().__init__(use_query,top_k)
        self.__model : SentenceTransformer = model
        self.__vector_database : faiss = vector_database

    def run(self) -> list[int]:
        index : SentenceTransformer = self.__vector_database
        query_embedding : NDArray[np.float32]  = self.__model.encode([self.use_query])[0]

        query_embedding : NDArray[np.float32] = np.array(query_embedding, dtype="float32").reshape(1, -1)
        D, I = index.search(query_embedding,self.top_k)
        return I
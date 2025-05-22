from langchain_community.vectorstores import FAISS
from read_file import Read_File_CSV
from package import (
    Path,
    List,
    Dict,
    pandas as pd
)

from langchain_huggingface import HuggingFaceEmbeddings
from convert_to_array import Embedding_To_Numpy

def main():
    path = Path(__file__).parent / "embedding_practive.csv"
    data : pd = Read_File_CSV(path).Read()
    
    model_embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    data_embedings : NDArray[np.float32] = Embedding_To_Numpy(data["Embedding"]).convert_to_numpy()

    data_base = FAISS.from_texts(data["Cau_hoi"], embedding=model_embeddings) 
    data_base.save_local("faiss_index")
    print(data_base)
    # print(data_base)

main()

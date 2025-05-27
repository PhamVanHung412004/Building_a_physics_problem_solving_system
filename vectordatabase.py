from langchain_community.vectorstores import FAISS
from read_file import Read_File_CSV
from package import (
    Path,
    List,
    Dict,
    pandas
)

from langchain.embeddings import HuggingFaceEmbeddings
from convert_to_array import Embedding_To_Numpy

def main():

    # Read file csv
    path_dataset : str = str(Path(__file__).parent / "deploy" / "dataset.csv")
    data : panads = Read_File_CSV(path_dataset).Read()

    # Convert to vector
    model_embeddings : HuggingFaceEmbeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    data_embedings : NDArray[np.float32] = Embedding_To_Numpy(data["Embedding"]).convert_to_numpy()

    # save to vectordatabase
    path_save_vector_database : str = str(Path(__file__).parent / "deploy/vectorDB")
    data_base : FAISS = FAISS.from_texts(data["Cau_hoi"], embedding=model_embeddings) 
    data_base.save_local(path_save_vector_database)

main()

from pathlib import Path
from read_file import Read_File_PDF
from sentence_transformers import SentenceTransformer
from Embedding_data import Get_Embedding
def main():
    path = Path(__file__).parent/"dataset/ÔN TẬP GIỮA KÌ 2.pdf"
    data = Read_File_PDF(path).Read()
    model = SentenceTransformer('BAAI/bge-small-en-v1.5')
    embedding = Get_Embedding(model,data).use_model()
    


main()
import os
from sentence_transformers import SentenceTransformer
from read_file import Read_File_PDF
from Embedding_data import Get_Embedding

def main():
  
    path = os.path.abspath("dataset/ÔN TẬP GIỮA KÌ 2.pdf")
    texts = Read_File_PDF(path).Read()
    model = SentenceTransformer('all-MiniLM-L6-v2')
    text_vector = Get_Embedding(model,texts).use_model()
    print(text_vector)
main()

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from package import Path

model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

load_vector_data_base = FAISS.load_local("faiss_index", model, allow_dangerous_deserialization=True)


user_query = "Buoc song la gi?"

retrival = load_vector_data_base.similarity_search(user_query,4)

print(retrival)

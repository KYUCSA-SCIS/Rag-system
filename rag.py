import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

bou_legal_text = """
with open("bou_fcp_2011.txt", "w") as f:
    f.write(bou_legal_text)

loader = TextLoader("bou_fcp_2011.txt")
documets = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunksize=500, chunkoverlap=50)
chunks = text_splitter.split_documents(documents)

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


persist_directory = "./chroma_bou_db"
vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory=persist_directory
)

def query_policy_rag(risk_type: str, query_text: str)

db = Chroma(persist_directory=persist_directory, embedding_function=embedding_model)

results = db.similarity_search(query_text, k=2)

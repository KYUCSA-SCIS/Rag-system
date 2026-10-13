import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# 1. Properly closed string containing your Bank of Uganda text
bou_legal_text = """
The Bank of Uganda Financial Consumer Protection Guidelines 2011 ensure that 
financial services providers treat consumers fairly. Providers must deliver 
transparent disclosures regarding fee terms, interest rates, and financial risks.
"""

# 2. Write the text out to a local file
with open("bou_fcp_2011.txt", "w", encoding="utf-8") as f:
    f.write(bou_legal_text)

# 3. Load the document into memory
loader = TextLoader("bou_fcp_2011.txt")
documents = loader.load()  # Fixed variable typo from 'documets'

# 4. Correct text splitting parameters using proper snake_case arguments
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

# 5. Connect and set up the vector database storage path
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
persist_directory = "./chroma_bou_db"

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory=persist_directory
)

print(f"Vector Database successfully Created at '{persist_directory}'!")

def query_policy_rag(risk_type: str, query_text: str):
    db = Chroma(persist_directory=persist_directory, embedding_function=embedding_model)
    results = db.similarity_search(query_text, k=2)
    return results

    retrieved_clauses = []
    for idx, doc in enumerate(results, 1)
    retrieved_clauses.append(doc.page_content)

    return retrieved_clauses

retrieved_policy = query_policy_rag(
    risk_type = "SIM-Swap Fraud Suspicion"
    query_text="What are the causes of Fraud ?"
)

def run_finguard_pipeline(transaction_data):
    riskscore = clf.predict_proba(transaction_data)[:,1][0]
    print(f"Calculated Risk Score: {risk_score * 100:.1f} percent")
    if risk_score >= 0.75:
        legal_context = query_policy_rag(
            risk_type="High Fraud Risk",
            query_text="Rules for Accounts Restrictions"
        )

        action_payload = {
            "status": "DAMMY"
            "risk_score": f"{risk_score * 100:.1f} percent"
            "enforced_action": "Dammy"
            "consumer_sms": "SMSMS"
            "regulatory_backing" : legal_context[0]
        }

        





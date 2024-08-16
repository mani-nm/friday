# import nltk
# nltk.download('punkt_tab')
# nltk.download('averaged_perceptron_tagger_eng')
import torch
import streamlit as st
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain_ollama import ChatOllama

torch.cuda.empty_cache()
def generate_response(question, model, embeddings, db):
    chain = RetrievalQA.from_chain_type(
        llm,
        retriever=db.as_retriever(),
    )
    result = chain.invoke({"query": question})
    return result


embeddings = HuggingFaceEmbeddings()
persist_dir = "chromadb"
db = Chroma(embedding_function=embeddings, persist_directory=persist_dir)

llm = ChatOllama(model="llama3.1", temperature=0.5)
# question = "how to improve upon the proposed methods in the thesis?"
# res = generate_response(question, llm, embeddings, db)
# print(res["result"])

# Page title
st.set_page_config(page_title="Friday AI")
st.title(":green[Hi👋🏼 I am :blue[*Friday*] your personal AI]🤖\nLocal and Secure 🙂")

query_text = st.text_input(
    "How can I help you?", placeholder="your question here"
)
result = []
with st.form("myform", clear_on_submit=True):
    submitted = st.form_submit_button("Submit") #, disabled=not query_text)
    if submitted:
        with st.spinner("Analysing..."):
            response = generate_response(query_text, llm, embeddings, db)
            result.append(response)

if len(result):
    st.info(response['result'])


torch.cuda.empty_cache()


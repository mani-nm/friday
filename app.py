# import nltk
# nltk.download('punkt_tab')
# nltk.download('averaged_perceptron_tagger_eng')
import torch
import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain_ollama import ChatOllama
import ollama

ollama.pull('llama3.1')

def generate_response(question, model, embeddings, db):
    """
    Generate a response to the given question using the specified model and database.

    Args:
        question (str): The user's query.
        model: The language model used for generation.
        embeddings: The embedding function used for retrieval.
        db: The persistent database used for storing embeddings.

    Returns:
        str: The generated response.
    """
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


# import nltk
# nltk.download('punkt_tab')
# nltk.download('averaged_perceptron_tagger_eng')
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain_ollama import ChatOllama

pdf = "data/CS298_Nag_Mani_Report.pdf"
loader = UnstructuredPDFLoader(pdf)

docs = loader.load()

text_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=2000,
    chunk_overlap=200
)
texts = text_splitter.split_documents(docs)
embeddings = HuggingFaceEmbeddings()
db = Chroma.from_documents(texts, embeddings)
llm=ChatOllama(model='llama3.1', temperature=0)
chain=RetrievalQA.from_chain_type(
    llm,
    retriever=db.as_retriever(),
)

question = "What is this document all about?"
result =chain({"query":question})
print(result['result'])
# print(texts[0])
# print(texts[1])
# print(type(docs))


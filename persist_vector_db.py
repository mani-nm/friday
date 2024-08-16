from langchain.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
# from langchain.chains import VectorDBQA
from langchain_community.document_loaders import UnstructuredPDFLoader

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
persist_directory = 'chromadb'
db = Chroma.from_documents(documents=texts, embedding=embeddings, persist_directory=persist_directory)
db.persist()
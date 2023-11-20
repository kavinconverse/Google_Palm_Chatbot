import google.generativeai as palm
import streamlit as st
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import GooglePalm
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory

def get_pdf_read(pdf_files):
    raw_text = ''
    for pdf in pdf_files:
        reader = PdfReader(pdf)
        for page in reader.pages:
            raw_text += page.extract_text()
    return raw_text

def get_text_split(raw_text):
    text_splitter = RecursiveCharacterTextSplitter(separators=['\n\n','\n',','],
                                                   chunk_size=1000,
                                                   chunk_overlap=50)
    text_chunks = text_splitter.split_text(raw_text)
    return text_chunks

def get_embeddings():
    embeddings = SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-v2')
    return embeddings

def push_to_vector_store(text_chunks,embeddings):
    vectorstore = FAISS.from_texts(text_chunks,embeddings)
    vectorstore.save_local('vectorst')
    return vectorstore

def get_conv_chain(vectorstore):
    llm = GooglePalm()
    memory = ConversationBufferMemory(memory_key='chat_history',return_messages=True)
    conversation_chain = RetrievalQA.from_llm(llm, retriever = vectorstore.as_retriever(),memory=memory)
    return conversation_chain

def get_response(query):
    response = st.session_state.conversation({'query':query})
    return response




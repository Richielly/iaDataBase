# from PyPDF2 import PdfReader
# from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
#
# from langchain.chains.question_answering import load_qa_chain
# from langchain.llms import OpenAI
#
# import os
# with open(r'C:\Users\Equiplano\Desktop\API.txt', 'r') as file:
#     # Ler uma linha do arquivo
#     api_key = file.readline()
# os.environ["OPENAI_API_KEY"] = api_key
#
# reader = PdfReader(r'C:\Users\Equiplano\Downloads\Unicesumar - Ensino a DistânciaPlano de negocio.pdf')
#
# raw_text = ''
#
# for i, page in enumerate(reader.pages):
#     text = page.extract_text()
#     if text:
#         raw_text+=text
#
# text_splitter = CharacterTextSplitter(
#     separator="\n",
#     chunk_size=1000,
#     chunk_overlap=200,
#     length_function=len,
# )
# texts = text_splitter.split_text(raw_text)
#
# # print(texts[0])
# def talk(question):
#     embeddings = OpenAIEmbeddings()
#
#     docsearch = FAISS.from_texts(texts, embeddings)
#
#     chain = load_qa_chain(OpenAI(), chain_type="stuff")
#
#     # question = 'Sobre o que fala este documento'
#     docs = docsearch.similarity_search(question)
#     resposta = chain.run(input_documents=docs, question=question)
#
#     return resposta
#
# while True:
#     question = input('O que você quer saber?')
#     if question:
#         print(talk(question))
#     question = ""

import streamlit as st
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os

# Definir a chave da API como variável de ambiente
with open(r'C:\Users\Equiplano\Desktop\API.txt', 'r') as file:
    api_key = file.readline()
os.environ["OPENAI_API_KEY"] = api_key

def load_pdf(file):
    reader = PdfReader(file)
    raw_text = ''

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            raw_text += text

    return raw_text

def talk(question, texts):
    embeddings = OpenAIEmbeddings()
    docsearch = FAISS.from_texts(texts, embeddings)
    chain = load_qa_chain(OpenAI(), chain_type="stuff")
    docs = docsearch.similarity_search(question)
    resposta = chain.run(input_documents=docs, question=question)

    return resposta

st.title('PDF Question Answering')
uploaded_file = st.file_uploader("Escolha um PDF", type="pdf")

if uploaded_file:
    raw_text = load_pdf(uploaded_file)
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    texts = text_splitter.split_text(raw_text)

    question = st.text_input('O que você quer saber?')

    if question:
        response = talk(question, texts)
        st.write(response)

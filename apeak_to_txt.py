# pip install wikipedia
from langchain import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS

import os
with open(r'C:\Users\Equiplano\Desktop\API.txt', 'r') as file:
    # Ler uma linha do arquivo
    api_key = file.readline()
os.environ["OPENAI_API_KEY"] = api_key

loader = TextLoader(r'C:\Users\Equiplano\Downloads\log.txt')
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(docs, embeddings)

chain = load_qa_chain(OpenAI(), chain_type="stuff")

query = "quantas linhas tem o arquivo?"
docs = db.similarity_search(query)

resposta = chain.run(input_documents=docs, question=query)


print(resposta)
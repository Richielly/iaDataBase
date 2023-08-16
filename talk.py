import streamlit as st
from streamlit_chat import message
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
import tempfile
import os

user_api_key = st.sidebar.text_input(
    label="#### Sua OpenAi API Key 👇",
    placeholder="Cole sua chave aqui, sk-",
    type="password")

# Definir a chave da API como variável de ambiente
with open(r'C:\Users\Equiplano\Desktop\API.txt', 'r') as file:
    api_key = file.readline()
user_api_key = api_key
os.environ["OPENAI_API_KEY"] = user_api_key

uploaded_file = st.sidebar.file_uploader("Importar arquivo", type=["csv", "pdf"])

def load_pdf(file):
    reader = PdfReader(file)
    raw_text = ''

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            raw_text += text

    return raw_text

def talk_pdf(question, texts):
    embeddings = OpenAIEmbeddings()
    docsearch = FAISS.from_texts(texts, embeddings)
    chain = load_qa_chain(OpenAI(), chain_type="stuff")
    docs = docsearch.similarity_search(question)
    resposta = chain.run(input_documents=docs, question=question)

    return resposta

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    if uploaded_file.type == 'application/pdf':
        raw_text = load_pdf(uploaded_file)
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        texts = text_splitter.split_text(raw_text)

    elif uploaded_file.type == 'text/csv':
        loader = CSVLoader(file_path=tmp_file_path, encoding="utf-8")
        data = loader.load()

        embeddings = OpenAIEmbeddings()
        vectors = FAISS.from_documents(data, embeddings)

        chain = ConversationalRetrievalChain.from_llm(
            llm=ChatOpenAI(temperature=0.0, model_name='gpt-3.5-turbo', openai_api_key=user_api_key),
            retriever=vectors.as_retriever())

    def conversational_chat(query):

        result = chain({"question": query, "chat_history": st.session_state['history']})
        st.session_state['history'].append((query, result["answer"]))
        return result["answer"]


    if 'history' not in st.session_state:
        st.session_state['history'] = []

    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Pergunte-me qualquer coisa sobre o arquivo " + uploaded_file.name + "."]

    if 'past' not in st.session_state:
        st.session_state['past'] = [" 👋 Seja bem vindo(a)! carreguei o arquivo e agora já sei um pouco sobre ele... 🤗"]

    # container for the chat history
    response_container = st.container()
    # container for the user's text input
    container = st.container()

    with container:
        with st.form(key='my_form', clear_on_submit=True):
            user_input = st.text_input("Query:", placeholder="Pergunte-me qualquer coisa sobre o arquivo aqui.", key='input')
            submit_button = st.form_submit_button(label='Send')

        if submit_button and user_input:
            if uploaded_file.type == 'text/csv':
                output = conversational_chat(user_input)
            elif uploaded_file.type == 'application/pdf':
                output = talk_pdf(user_input, texts)
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)

    if st.session_state['generated']:
        with response_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="big-smile")
                message(st.session_state["generated"][i], key=str(i), avatar_style="adventurer")
# from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
# import os
#
# with open(r'C:\Users\Equiplano\Desktop\API.txt', 'r') as file:
#     # Ler uma linha do arquivo
#     api_key = file.readline()
#
# # Setup database
# db = SQLDatabase.from_uri("postgresql://postgres:es74079@localhost:5432/postgres")
#
# llm = OpenAI(temperature=0, openai_api_key=api_key, model_name='gpt-3.5-turbo')
#
# db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)
#
# # Create query instruction
# QUERY = """
# Given an input question, first create a syntactically correct postgresql query to run, then look at the results of the query and return the answer.
# Use the following format:
#
# Question: "Question here"
# SQLQuery: "SQL Query to run"
# SQLResult: "Result of the SQLQuery"
# Answer: "Final answer here"
#
# {question}
# """
#
# # Setup the database chain
# db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)
#
# def get_prompt():
#     print("Type 'exit' to quit")
#
#     while True:
#         prompt = input("Enter a prompt: ")
#
#         if prompt.lower() == 'exit':
#             print('Exiting...')
#             break
#         else:
#             try:
#                 question = QUERY.format(question=prompt)
#                 print(db_chain.run(question))
#             except Exception as e:
#                 print(e)
#
#
# get_prompt()

import streamlit as st
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain

# Ler a chave da API a partir de um arquivo
with open(r'C:\Users\Equiplano\Desktop\API.txt', 'r') as file:
    api_key = file.readline().strip()

# Configuração do banco de dados
db = SQLDatabase.from_uri("postgresql://postgres:es74079@localhost:5432/postgres")

# print(db.get_table_info(['arr_nfs1']))

llm = OpenAI(temperature=0, openai_api_key=api_key, model_name='gpt-3.5-turbo')

# Instrução de consulta
QUERY = """
Dada uma pergunta de entrada, primeiro crie uma consulta postgresql sintaticamente correta para executar, depois observe os resultados da consulta e retorne a resposta.
Use o seguinte formato:
Answer: "Resposta final aqui"
{question}
"""
# Question: "pergunta aqui"
# SQLQuery: "Consulta SQL para executar"
# SQLResult: "Resultado da SQLQuery"

# Configuração da database chain
db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)

# Interface Streamlit
st.title('Bate Papo com Data Base')

prompt = st.text_input("Digite uma pergunta ou dê uma instrução:")

print(prompt)

if prompt:
    try:
        question = QUERY.format(question=prompt)
        response = db_chain.run(question)
        st.write(response)
    except Exception as e:
        st.write(f"Erro: {e}")


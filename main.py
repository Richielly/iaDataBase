# from langchain.llms import OpenAI
# from langchain import PromptTemplate, LLMChain
#
# with open(r'C:\Users\Equiplano\Desktop\API.txt', 'r') as file:
#     # Ler uma linha do arquivo
#     api_key = file.readline()
#
# # llm = OpenAI(model_name="text-davinci-003", openai_api_key=api_key)
# # question = "Que dia é hoje?"
# # print(question, llm(question))
#
# llm = OpenAI(model_name="text-davinci-003", openai_api_key=api_key)
# template = "Qual os top {num} sites gratuitos para aprender programação {linguagem}?"
# prompt = PromptTemplate(template=template,input_variables=['num','linguagem'])
# chain = LLMChain(llm=llm,prompt=prompt)
# input = {'num':4,'linguagem':'Python'}
# # print(chain.run(input))




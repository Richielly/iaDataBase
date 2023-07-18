from langchain import OpenAI, SQLDatabase, SQLDatabaseChain


with open(r'C:\Users\Equiplano\Desktop\API.txt', 'r') as file:
    # Ler uma linha do arquivo
    api_key = file.readline()
# Set up the connection string for your PostgreSQL database
#conn_str = "postgresql+psycopg2://Nota_Terra_Rica:es74079@localhost:5432/Nota_Terra_Rica"
conn_str = "postgresql://postgres:es74079@localhost:5432/postgres"
# Create an instance of the SQLDatabase using the connection string
db = SQLDatabase.from_uri(conn_str)

# Create an instance of the SQLDatabaseChain with the desired language model and the SQLDatabase
db_chain = SQLDatabaseChain.from_llm(OpenAI(temperature=0, openai_api_key=api_key), db, verbose=True)

# Ask a question about your database
question = "crie uma tabela chamada tabela_1"

# Use the SQLDatabaseChain to get the answer
answer = db_chain(question)

print(answer)
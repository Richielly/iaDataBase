import psycopg2

# Estabelece uma conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(
    host= 'localhost' ,
    port= 5432 ,
    user= 'Nota_Terra_Rica' ,
    password= 'es74079',
    database='Nota_Terra_Rica'
)

# Cria um objeto cursor para executar comandos SQL
cursor = conn.cursor()
cursor.execute('select *  from arr_emp')
result = cursor.fetchall()
print(result)
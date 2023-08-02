import os
import requests
import pandas as pd

# Ler o arquivo CSV
dados = pd.read_csv(r'D:\Conversao\Sysmar\Terra_Rica\Arquivos\notasTerraRica_pdf_completo_35344.csv')

# Solicitar ao usuário a linha inicial
try:
    linha_inicial = int(input("A partir de qual linha você deseja iniciar o processo? (0 para a primeira linha): "))
    if linha_inicial >= len(dados) or linha_inicial < 0:
        print("Linha inválida. Iniciando a partir da primeira linha.")
        linha_inicial = 0
except ValueError:
    print("Entrada inválida. Iniciando a partir da primeira linha.")
    linha_inicial = 0

# Criar a pasta principal para armazenar as notas
pasta_principal = input("Digite o nome da pasta principal: ")
os.makedirs(pasta_principal, exist_ok=True)

# Iterar sobre os dados e baixar as notas, começando da linha especificada pelo usuário -1 se não tiver cabeçalho e -2 se tiver cabeçalho
for index, linha in dados.iloc[linha_inicial-2:].iterrows():
    documento = linha['documento']
    nota = linha['nota']
    url = linha['url']

    # Criar a pasta para o documento
    pasta_documento = os.path.join(pasta_principal, str(documento))
    os.makedirs(pasta_documento, exist_ok=True)

    # Baixar a nota e salvar com o nome da coluna 'nota'
    nome_arquivo = os.path.join(pasta_documento, str(nota) + '.pdf')
    response = requests.get(url)
    with open(nome_arquivo, 'wb') as file:
        file.write(response.content)
    print(f"Nota {str(nota)} empresa {str(documento)} baixada com sucesso!")

print(f"Notas baixadas com sucesso!")
# Nota 1 empresa 82388737000198 baixada com sucesso!
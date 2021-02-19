# Desafio Wiser
    # Acessar os dados Json no meu drive pessoal
    # Tratar os dados
    # Salvar as primeiras 300 linhas em um novo .csv

# Instala biblioteca necessária para acesso ao Google Drive
#!pip install PyDrive

# Importando bibliotecas
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import json
import pandas as pd
import seaborn as srn
import statistics as sts

# Acessando o Google Drive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

# Id da pasta onde encontram-se os arquivos json no drive
folder_id = "1ZKooNrG63XOe0uDGX8f6-b9YxzUjVY9u"

# Lista os arquivos dentro da pasta e realiza o download
file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(folder_id)}).GetList()
arrayNome = []
for file in file_list:
    file.GetContentFile(file['title'])
    arrayNome.append(file['title'])


# Para cada arquivo listado armazena os dados no formato DataFrame
f = open(arrayNome[0])
data = json.load(f)
base1 = pd.DataFrame.from_dict(data["_default"], orient='index')
len(base1.index)

f = open(arrayNome[1])
data = json.load(f)
base2 = pd.DataFrame.from_dict(data["_default"], orient='index')
len(base2.index)

f = open(arrayNome[2])
data = json.load(f)
base3 = pd.DataFrame.from_dict(data["_default"], orient='index')
len(base3.index)

# Compila todos os dados em um único DataFrame
tmp = [base1, base2, base3]
base = pd.concat(tmp)
len(base)

# Checa o número de linhas e colunas
base.shape

# Salva as primeiras 300 linhas do DataFrame em um .csv
print(base.head(300).to_csv("desafioWiser.csv", sep = ';', encoding='utf-8-sig'))




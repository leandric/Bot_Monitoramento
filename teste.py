import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import json

#arquivo de Configuração:
config = open('config/config.json','r').read()
config = json.loads(config)

#BANCO:
adress = config['BANCO']['ADRESS']
port = config['BANCO']['PORT']
user = config['BANCO']['USER']
pwd = config['BANCO']['PASS']

base_query = open('config/console.sql','r').read()


conexao = mysql.connector.connect(host=adress, user=user, passwd=pwd, db='BANCO')


query = ''

df = pd.read_sql_query(base_query, conexao, index_col=None)

plt.bar(df.SITE, df.LOGIN, color='green')

#legendas
plt.title('LOGINS')
plt.xlabel('Sites')
plt.ylabel('Logados')


plt.ylim(250, 450)
plt.show()

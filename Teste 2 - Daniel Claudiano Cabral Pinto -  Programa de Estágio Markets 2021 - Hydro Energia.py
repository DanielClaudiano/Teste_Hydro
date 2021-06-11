## Importando Pandas
import pandas as pd
## Obtendo Dados através da API do Banco Central
url = 'https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoAnuais?$top=10&$orderby=Data%20desc&$format=text/csv&$select=Data,DataReferencia,Mediana'
#Obtendo Dataframe
df = pd.read_csv(url)
#Salvando em csv
df.to_csv('Bacen_api.csv', index=False)
#Abrindo arquivo salvo em csv
teste2 = pd.read_csv('Bacen_api.csv')
print(teste2) 
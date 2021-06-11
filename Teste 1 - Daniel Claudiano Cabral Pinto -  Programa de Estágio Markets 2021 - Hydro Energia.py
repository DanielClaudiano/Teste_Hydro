#importando pacote 
import pandas as pd
#Criando dataframe a partir do arquivo importado
df = pd.read_csv(r'C:\Users\Daniel\Downloads\Prices_Hydro_20190721.csv')
#Obtendo as características dos dados
print(df.info())
#Verificando a presença de valores nulos
print('Verificando a presença de valores nulos',df.isnull().sum())
#Verificando a presença de valores duplicados
print('Verificando a presença de valores nulos',sum(df.duplicated()))
#Extraindo a amostra de interesse
subset0 = df.query('PMO_Stage == "Month"')
subset1 = subset0[subset0['Scenarios_id'].str.contains('GFS-ETA')]
#Verificando a presença de valores nulos na amostra selecionada
print(subset1.isnull().sum())
######Dataframe baseada no exemplo dado
#Obtendo as médias por segmento
df_results = subset1.groupby(['Target_label','System'],as_index =False)['value'].mean()
#Obtendo as medianas por segmento
df_results2 = subset1.groupby(['Target_label','System'],as_index =False)['value'].median()
#Unindo os dois dataframes anteriores
df_final = pd.merge(df_results, df_results2, left_on=['Target_label','System'], right_on=['Target_label','System'],suffixes=('_L','_R'))
#Atribuindo novos nomes as colunas
new_labels= ['Target label','System','Average','Median']
df_final.columns = new_labels
#Ordenando o dataframe
import numpy as np
df_final["Month"] = np.repeat([8,12,7,11,10,9],4)
df_final["Region"] = np.array(list(np.arange(0,4))*6)
df_final.sort_values(["Region","Month"], ascending=[True,True],inplace=True)
df_final.drop(["Region","Month"], axis=1, inplace=True)
#df_final.sort_values(["Month","System"], ascending=[True,True],inplace=True)
#df_final.drop('Month', axis=1, inplace=True)
df_final.set_index('Target label',inplace=True)
df_final = df_final.transpose()
print(df_final)
## Outra forma Alternativa
A_df_final = df_final.transpose()
A_df_final
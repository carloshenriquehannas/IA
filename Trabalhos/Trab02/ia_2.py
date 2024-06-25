# -*- coding: utf-8 -*-
"""IA_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ryvNgFbZlXWjRijbqRS1PrUbmQzTxAN4
"""

#Importa o arquivo CSV com dados para o dataframe (df)
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/carloshenriquehannas/IA/main/Trabalhos/Trab02/train.csv')

#Exibe a dimensao do dataframe
df.shape

#Exibe a estruturacao dos dados dos 5 primeiros registros
df.head()

#Alteracao dos nomes das colunas do dataframe
df = df.rename(columns={'MonsoonIntensity': 'IntensidadeDaMoncao', 'TopographyDrainage': 'TopografiaDeDrenagem', 'RiverManagement': 'GestaoDeRio', 'Deforestation': 'Desmatamento', 'Urbanization': 'Urbanizacao', 'ClimateChange': 'AlteracoesClimaticas', 'DamsQuality': 'QualidadeDeBarragens', 'Siltation': 'Assoreamento', 'AgriculturalPractices': 'PraticasAgricolas', 'Encroachments': 'Invasoes', 'IneffectiveDisasterPreparedness': 'PreparacaoIneficazParaDesastres', 'DrainageSystems': 'SistemasDeDrenagem', 'CoastalVulnerability': 'VulnerabilidadeCosteira', 'Landslides': 'DeslizamentosDeTerra', 'Watersheds': 'BaciasHidrograficas', 'DeterioratingInfrastructure': 'DeterioracaoDaInfraestrutura', 'PopulationScore': 'PontuacaoPopulacional', 'WetlandLoss': 'PerdaDeZonasUmidas', 'InadequatePlanning': 'PlanejamentoInadequado', 'PoliticalFactors': 'FatoresPoliticos', 'FloodProbability': 'ProbabilidadeInundacao'})
df.columns

#Gera analises estatiticas, como contagem, media, desvia padrao, minimo, quartis (25%, 50% e 75%) e maximo, do dataframe
df.describe()

df = df.drop(columns = ['id'])                                                  #Remocao da coluna "id" do dataframe
correlation_matrix = df.corr()                                                  #Calculo da matriz de correlacao entre colunas do dataframe

#Filtro para verificar correlacoes entre dados maiores que threshold
threshold = 0.1                                                                 #Limite de threshold (constante arbitraria)
high_correlations = correlation_matrix[(abs(correlation_matrix) > threshold)]   #Filtro de altas correlacoes (maiores que threshold)

high_correlations                                                               #Matriz com os dados de altas correlacoes

import matplotlib.pyplot as plt
import seaborn as sns

#Plot da matriz de altas correlacoes, com uma formato de mapas de calor
plt.figure(figsize=(21, 8))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', annot_kws={"size": 10})
plt.title('Heatmap da Matriz de Correlação')
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


sample_size = 10000                                                             #Define o tamanho da amostra para modelagem dos dados

df_simple = df.sample(n=sample_size, random_state=42)                           #Selecao de uma amostra aleatoria

#Separacao de variaveis
X = df_simple.drop(columns = ['ProbabilidadeInundacao'])                        #X: feature do dataframe
y = df_simple.ProbabilidadeInundacao                                            #y: target do dataframe

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)        #Treino e teste de dados (80% para treino e 20% para teste)

#Treino do modelo de regressao com 100 (n_estimators) arvores de decisao
rf_model = RandomForestRegressor(n_estimators=100)                              #Inicializa o modelo
rf_model.fit(X_train, y_train)                                                  #Treino do modelo

y_pred = rf_model.predict(X_test)                                               #Previsao de y no conjunto de testes X

#Calculo e impressao do erro quadratico medio, entre teste e previsao
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

#Selecao das melhores features
for k in range(1, X.shape[1] + 1):

  #Selecao das melhores caracteristicas
  selecionar_kmelhores = SelectKBest(chi2, k = k)                               #Inicializa SelectKBest
  X_new = selecionar_kmelhores.fit_transform(X_train, y_train.astype('int'))

  #Obtencao das melhores caracteristicas
  mask = selecionar_kmelhores.get_support()
  selected_features = df.columns[:-1][mask]
  #print("Características selecionadas:", selected_features)

  #Criacao de um novo dataframe
  df_v2 = df[selected_features]
  df_v2 = pd.concat([df_v2, df.ProbabilidadeInundacao], axis=1)

  df_v2_simple = df_v2.sample(n=sample_size, random_state=42)                   #Selecao de uma amostra aleatoria

  #Separacao de variaveis
  X = df_v2_simple.drop(columns = ['ProbabilidadeInundacao'])                   #X: feature
  y = df_v2_simple.ProbabilidadeInundacao                                       #y: target

  #Treino e teste de dados (80% para treino e 20% para teste)
  X_train_v2, X_test_v2, y_train_v2, y_test_v2 = train_test_split(X, y, test_size=0.2)

  #Treino do modelo de regressao com 100 (n_estimators) arvores de decisao
  rf_model = RandomForestRegressor(n_estimators=100)                            #Inicializa o modelo
  rf_model.fit(X_train_v2, y_train_v2)                                          #Treino do modelo
  y_pred_v2 = rf_model.predict(X_test_v2)                                       #Previsao de dados

  #Calculo e impressao do erro quadratico medio, para cada valor de K
  mse_rf = mean_squared_error(y_test_v2, y_pred_v2)
  print(f"K = {k} --> Mean Squared Error: {mse}")

from sklearn.linear_model import LinearRegression

#Treinamento por regressao linear
lr_model = LinearRegression()                                                   #Inicializa modelo de regressao linear
lr_model.fit(X_train, y_train)                                                  #Treinamento dos dados por regressao linear

y_pred = lr_model.predict(X_test)                                               #Previsao de y no conjunto de testes X, por regressao linear

#Calculo e impressao do erro quadratico medio, entre teste e previsao para regressao linear
mse_lr = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

from sklearn.neighbors import KNeighborsRegressor

#Treinamento por KNN
knn_model = KNeighborsRegressor()                                               #Inicializa o modelo de KNN
knn_model.fit(X_train, y_train)                                                 #Treinamento dos dados por KNN

y_pred = knn_model.predict(X_test)                                              #Previsao de y no conjunto de testes X, por KNN

#Calculo e impressao do erro quadratico medio, entre teste e previsao para KNN
mse_knn = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

from sklearn.linear_model import Ridge

#Treinamento pelo modelo ridge
ridge_model = Ridge()                                                           #Inicializa o modelo ridge
ridge_model.fit(X_train, y_train)                                               #Treinamento de dados pelo modelo ridge

y_pred = ridge_model.predict(X_test)                                            #Previsao de y no conjunto de testes X, no modelo ridge

#Calculo e impressao do erro quadratico medio, entre teste e previsao para modelo ridge
mse_ridge = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

from sklearn.svm import SVR

#Treinamento pelo modelo SVR (support vector regressor)
svr = SVR()                                                                     #Inicializa o modelo de SVR
svr.fit(X_train, y_train)                                                       #Treinamento de dados por SVR

y_pred = svr.predict(X_test)                                                    #Previsao de y no conjunto de testes X, por SVR

#Calculo e impressao do erro quadratico medio, entre teste e previsao para SVR
mse_svr = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

#Definicao dos modelos e respectivos erros quadraticos para comparacao
models = ['Random Forest', 'Linear Regression', 'KNN', 'Ridge', 'SVR']
mse_scores = [mse_rf, mse_lr, mse_knn, mse_ridge, mse_svr]

#Grafico de barras para comparar os modelos e seus respectivos erros quadraticos medio
plt.figure(figsize=(10, 6))
sns.barplot(x=models, y=mse_scores)
plt.title('Comparação de MSEs dos Modelos de Regressão')
plt.xlabel('Modelos')
plt.ylabel('Mean Squared Error (MSE)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
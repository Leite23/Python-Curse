
# Passo 1: Entendimento do Desafio

# Passo 2: Entendimento da Área/Empresa

# Passo 3: Extração/Obtenção de Dados
import pandas as pd

tabela = pd.read_csv("barcos_ref.csv")
print(tabela)

# Passo 4: Ajuste de Dados (Tratamento/Limpeza)
print(tabela.info())

# Passo 5: Análise Exploratória
import seaborn as sns
import matplotlib.pyplot as plt

# criar o grafico
sns.heatmap(tabela.corr()[["Preco"]], cmap="Blues", annot=True)

#exibir o grafico
plt.show()

# Passo 6: Modelagem + Algoritmos (Aqui que entra a Inteligência Artificial, se necessário)

# Preparacao

    # Separar a base em dados de X e Y / X -> Informacoes de consulta (O Resto) E Y -> quem eu quero prever (Preco)
from sklearn.model_selection import train_test_split

y = tabela["Preco"]
x = tabela.drop("Preco", axis=1)

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1)

# Criacao e treino da IA

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# cria as inteligencias aritificiais
modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

# treina as inteligencias artificias
modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)

from sklearn import metrics

# criar as previsoes
previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

# comparar os modelos
print(metrics.r2_score(y_teste, previsao_regressaolinear))
print(metrics.r2_score(y_teste, previsao_arvoredecisao))  

# Passo 7: Interpretação de Resultados
tabela_auxiliar = pd.DataFrame()
tabela_auxiliar["y_teste"] = y_teste
tabela_auxiliar["Previsoes ArvoreDecisao"] = previsao_arvoredecisao
tabela_auxiliar["Previsoes Regressao Linear"] = previsao_regressaolinear

# plt.figure(figsize=(15,6))
sns.lineplot(data=tabela_auxiliar)
plt.show()

nova_tabela = pd.read_csv("novos_barcos.csv")
print(nova_tabela)
previsao = modelo_arvoredecisao.predict(nova_tabela)
print(previsao)

# Palpite: material, ano, tipo
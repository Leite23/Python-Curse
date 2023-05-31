# Passo 1: Pegar/Importar a base de dados
# Passo 2: Visualizar a base de dados
    #Entender as informaçoes que voce tem disponiveis
    #procurar os erro da base de dados
#Passo 3: Tratamento de dados
    #Valores no formato errado
    #Valores vazios
#Passo 4: Análise Inicial = entender como estão as notas dos clientes
#Passo 5: Análise completa = traçar o perfil ideal do cliente = entender como cada caraceteristica do cliente impacta na nota

#axis = 0 -> deletar uma linha, axis = 1 -> deletar uma coluna
import pandas as pd
import plotly.express as px


tabela = pd.read_csv(r"C:\Users\guiro\Documents\VS STUDIO\Python Curse\clientes.csv", encoding="latin", sep=";")
print (tabela)

tabela = tabela.drop("Unnamed: 8", axis=1)
#Informaçoes da tabelela:
#print (tabela.info())

tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")

tabela = tabela.dropna()
print (tabela.info())

print(tabela.describe()) 

#criar o grafico com plotly 
for coluna in tabela.columns:
    
    grafico = px.histogram(tabela, x=coluna, y="Nota (1-100)", histfunc="avg", text_auto=True , nbins=10 )
#x="Salário Anual (R$)"
#x="Profissão"
#x="Origem"
    grafico.show()
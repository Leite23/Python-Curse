#Passo 1: Entrar na internet 
#Passo 2: Importar a base de dados
#Passo 3: Para cada produto da nossa base
#Passo 4: Pegar o preço atual do produto
#Passo 5: Atualizar o preço na base de dados
#Passo 6: Decidir quais produtos a gente vai comprar
#Passo 7: Exportar a base de dados atualizada
# .send_keys("meu nome é") -> escrever nele
# .click() -> clicar nele
# .get_attribute() -> pegar uma informação dele
#import unicodedata
#link = unicodedata.normalize("NFKD", link).endcode("ascii", "ignore")

from selenium import webdriver
import pandas as pd

navegador = webdriver.Chrome()

tabela = pd.read_excel("commodities.xlsx")
print(tabela)

for linha in tabela.index:
    
    produto = tabela.loc[linha, "Produto"]

#entrar no site
    link = f"https://www.melhorcambio.com/{produto}-hoje"
    link = link.replace("ó", "o").replace("á", "a").replace("ã", "a").replace("ç", "c").replace("ú", "u").replace("é", "e")
    print(link)
    navegador.get(link)

#pegar a cotação do milho
    cotacao = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
    cotacao = cotacao.replace("." , "").replace("," , ".")
    cotacao = float(cotacao)

#na coluna Preço atual do milho preencher
    tabela.loc[linha, "Preço Atual"] = cotacao
    print(tabela)
    
#    
    tabela[ "Comprar"] = tabela["Preço Atual"] < tabela ["Preço Ideal"]
    print(tabela)
    
tabela.to_excel("commodities_atualizado.xlsx" , index =False)
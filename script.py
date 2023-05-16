import pyautogui 
import time
import pandas
import pyperclip


pyautogui.PAUSE = 1


#pyautogui.click
#pyautogui.write
#pyautogui.press
#pyautogui.hotkey


pyautogui.hotkey("alt" , "tab")
pyautogui.hotkey("ctrl" , "t")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter") 

pyautogui.click(x=1287, y=324)
pyautogui.write("meu login")

pyautogui.click(x=1251, y=419)
pyautogui.write("minha senha")

pyautogui.click(x=1215, y=501)

time.sleep(3)
pyautogui.click(x=518, y=327)
time.sleep(2)
pyautogui.click(x=653, y=763)

tabela = pandas.read_csv(r"C:\Users\guiro\Documents\VS STUDIO\Python Curse\Compras.csv", sep=";")
print(tabela)

total_gasto = tabela["ValorFinal"].sum()

quantidade = tabela["Quantidade"].sum()

preco_medio = total_gasto / quantidade

print(total_gasto)
print(quantidade)
print(preco_medio)

pyautogui.hotkey("ctrl", "t")
pyautogui.click(x=1017, y=47)
pyautogui.write("https://mail.google.com/mail/u/0/nbox")
pyautogui.press("enter")

pyautogui.click(x=145, y=158)
pyautogui.write("guiroleite@gmail.com")
pyautogui.press("tab")

pyautogui.press("tab")
pyautogui.copy("Relatório de Compras")
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab")

texto = f"""
Prezados,

Segue p relatório de compras

Total gasto: R${total_gasto}
Quantidade de produtos: {quantidade}
Precço Médio: R${preco_medio}

Qualquer dúvida é so falar.
Att.,
Guilherme Leite
"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")


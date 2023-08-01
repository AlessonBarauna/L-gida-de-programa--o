import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5
pyautogui.press("Win")
pyautogui.write("Google")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

pyautogui.click(x=273, y=397)
pyautogui.write("alesson.barauna1@gmail.com")

pyautogui.click(x=249, y=497)
pyautogui.write("123456")
pyautogui.press("enter")

tabela = pd.read_csv("produtos.csv")
print(tabela)

linha = 0

pyautogui.click(x=232, y=277)
codigo = tabela.loc[linha, "codigo"]
pyautogui.write(str(codigo))

pyautogui.press("tab")
pyautogui.write(str(tabela.loc[linha, "marca"]))

pyautogui.press("tab")
pyautogui.write(str(tabela.loc[linha, "tipo"]))

pyautogui.press("tab")
pyautogui.write(str(tabela.loc[linha, "categoria"]))

pyautogui.press("tab")
pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))

pyautogui.press("tab")
pyautogui.write(str(tabela.loc[linha, "custo"]))

pyautogui.press("tab")

obs = tabela.loc[linha, "obs"]
if not pd.isna(obs):
    pyautogui.write(str(tabela.loc[linha, "obs"]))
pyautogui.press("tab")




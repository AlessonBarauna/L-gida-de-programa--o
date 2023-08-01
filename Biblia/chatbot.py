import re
import tkinter as tk
from tkinter import scrolledtext, END

def carregar_biblia(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def encontrar_versiculo(versiculo):
    biblia = carregar_biblia("bible.txt")
    padrao = r"{}.*".format(versiculo)
    resultados = re.findall(padrao, biblia, re.IGNORECASE)
    return resultados

def responder_pergunta():
    entrada = entrada_texto.get().strip().lower()
    resposta_texto.delete(1.0, END)

    if entrada == "sair":
        resposta_texto.insert(tk.INSERT, "Até logo!")
        janela.quit()
    else:
        resultados = encontrar_versiculo(entrada)
        if resultados:
            for i, resultado in enumerate(resultados[:3]):
                resposta_texto.insert(tk.INSERT, f"{i+1}. {resultado}\n")
        else:
            resposta_texto.insert(tk.INSERT, "Desculpe, não encontrei nenhum versículo que corresponda à sua pergunta.")

janela = tk.Tk()
janela.title("Chatbot da Bíblia")

# Texto de entrada
entrada_label = tk.Label(janela, text="Digite sua pergunta:")
entrada_label.pack()

entrada_texto = tk.Entry(janela, width=50)
entrada_texto.pack()

# Botão para enviar a pergunta
enviar_botao = tk.Button(janela, text="Enviar", command=responder_pergunta)
enviar_botao.pack()

# Resposta do chatbot
resposta_label = tk.Label(janela, text="Resposta:")
resposta_label.pack()

resposta_texto = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=50, height=10)
resposta_texto.pack()

janela.mainloop()

import tkinter as tk
from tkinter import messagebox

def gerar_sequencia():
    try:
        nome_livro = entry_nome_livro.get()
        inicio = int(entry_inicio.get())
        quantidade = int(entry_quantidade.get())

        resultado.delete('1.0', tk.END)  # Limpar a caixa de texto antes de mostrar a sequência

        for i in range(inicio, inicio + quantidade):
            resultado.insert(tk.END, f"{nome_livro} 1:{i}\n")
    except ValueError:
        messagebox.showerror("Erro", "Certifique-se de que os números estão corretos.")

# Criar a janela principal
window = tk.Tk()
window.title("Gerador de Sequência")
window.geometry("400x300")

# Criar widgets
label_nome_livro = tk.Label(window, text="Digite o nome do livro:")
entry_nome_livro = tk.Entry(window)

label_inicio = tk.Label(window, text="Digite o número inicial da sequência:")
entry_inicio = tk.Entry(window)

label_quantidade = tk.Label(window, text="Digite a quantidade de valores na sequência:")
entry_quantidade = tk.Entry(window)

btn_gerar = tk.Button(window, text="Gerar Sequência", command=gerar_sequencia)

resultado = tk.Text(window, height=10, width=40)

# Posicionar os widgets na janela
label_nome_livro.pack(pady=5)
entry_nome_livro.pack(pady=5)

label_inicio.pack(pady=5)
entry_inicio.pack(pady=5)

label_quantidade.pack(pady=5)
entry_quantidade.pack(pady=5)

btn_gerar.pack(pady=10)

resultado.pack(pady=10)

# Executar a janela principal
window.mainloop()

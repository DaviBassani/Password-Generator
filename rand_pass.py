import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_show_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Erro", "O comprimento da senha deve ser um número positivo.")
            return
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número inteiro válido para o comprimento da senha.")
        return
    
    password = generate_password(length)
    password_display.config(state="normal")
    password_display.delete("1.0", tk.END)
    password_display.insert(tk.END, password)
    password_display.config(state="disabled")

# Configuração da janela
root = tk.Tk()
root.title("Gerador de Senhas")
root.geometry("400x200")
root.resizable(False, False)

# Criando os widgets
length_label = tk.Label(root, text="Comprimento da Senha:")
length_label.pack(pady=(10, 0))

length_entry = tk.Entry(root, width=10)
length_entry.pack()

generate_button = tk.Button(root, text="Gerar Senha", command=generate_and_show_password)
generate_button.pack(pady=(10, 0))

password_display = tk.Text(root, height=1, width=30, state="disabled")
password_display.pack(pady=(10, 0))

# Execução da aplicação
root.mainloop()

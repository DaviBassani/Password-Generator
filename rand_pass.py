import customtkinter as tk
from customtkinter import ctk_tk as ttk
from customtkinter import CTkTextbox as messagebox
import random
import string
import ttkthemes
import pyperclip

# Lista para armazenar as últimas 3 senhas geradas
password_history = []

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
    password_display.configure(state="normal")
    password_display.delete("1.0", tk.END)
    password_display.insert(tk.END, password)
    password_display.configure(state="disabled")
    
    # Adiciona a senha ao histórico com base no número de vezes que o botão foi pressionado
    password_history.append(password)
    update_password_history()

def copy_to_clipboard():
    password = password_display.get("1.0", "end-1c")
    pyperclip.copy(password)

def update_password_history():
    history_text.configure(state="normal")
    history_text.delete("1.0", tk.END)
    for i, password in enumerate(reversed(password_history), 1):
        history_text.insert(tk.END, f"Senha {len(password_history) - i + 1}: {password}\n")
    history_text.configure(state="disabled")

# Configuração da janela
root = tk.CTk()
root.title("Gerador de Senhas")
root.geometry("400x300")
root.resizable(False, False)

# Aplicando o tema do ttkthemes
style = ttkthemes.ThemedStyle(root)
style.set_theme("arc")

# Criando os widgets
length_label = tk.CTkLabel(root, text="Comprimento da Senha:")
length_label.pack(pady=(10, 0))

length_entry = tk.CTkEntry(root, width=10)
length_entry.pack()

generate_button = tk.CTkButton(root, text="Gerar Senha", command=generate_and_show_password)
generate_button.pack(pady=(10, 0))

password_display = tk.CTkTextbox(root, height=50, width=100, state="disabled")
password_display.pack(pady=(10, 0))

copy_button = tk.CTkButton(root, text="Copiar Senha", command=copy_to_clipboard)
copy_button.pack(pady=(5, 10))

# Widget para exibir o histórico de senhas
history_label = tk.CTkLabel(root, text="Histórico de Senhas:")
history_label.pack()

# Increase height of history_text to 5
history_text = tk.CTkTextbox(root, height=100, width=300, state="disabled")
history_text.pack()

# Execução da aplicação
root.mainloop()

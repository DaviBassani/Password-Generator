import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Bem-vindo ao Gerador de Senhas Automático!")
    print("Este programa irá gerar uma senha segura com base nas suas preferências.")

    try:
        length = int(input("Por favor, digite o comprimento da senha desejada: "))
        if length <= 0:
            print("Erro: O comprimento da senha deve ser um número positivo.")
            return
    except ValueError:
        print("Erro: Por favor, insira um número inteiro válido para o comprimento da senha.")
        return

    password = generate_password(length)
    print("\nA senha gerada é:", password)
    print("Por favor, anote esta senha em um local seguro.")

if __name__ == "__main__":
    main()

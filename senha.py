import random
import string

def gerar_senha(tamanho, apenas_numeros, apenas_letras, incluir_especiais):
    caracteres = ''
    
    if apenas_numeros:
        caracteres += string.digits
    if apenas_letras:
        caracteres += string.ascii_letters
    if incluir_especiais:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Você deve selecionar pelo menos um tipo de caractere.")

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    try:
        tamanho = int(input("Quantos caracteres deve ter a senha? "))
        
        apenas_numeros = input("Quer apenas números? (s/n) ").strip().lower() == 's'
        apenas_letras = input("Quer apenas letras? (s/n) ").strip().lower() == 's'
        incluir_especiais = input("Quer incluir caracteres especiais? (s/n) ").strip().lower() == 's'
        
        senha = gerar_senha(tamanho, apenas_numeros, apenas_letras, incluir_especiais)
        print(f"Sua senha gerada é: {senha}")
    
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()

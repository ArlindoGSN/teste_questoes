# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def count_a(text):
    if text.islower():
        return text.count('a')
    else:
        return text.lower().count('a')


string = input("Digite uma string: ")

print(f"Quantidade de 'a': {count_a(string)}")

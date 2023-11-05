"""
    Faça um programa que receba o nome do usuário
    Crie um laço de repetição while onde execute mesmo número de caracteres do nome digitado pelo
    usuário
    dentro do while, adicione a outra variavel letra por letra do nome digitado pelo usuário

"""

print('\n')

nome = input('Digite seu nome: ')
letras = len(nome)
nome_novo = ''
contador = 0

while contador < letras:
    nome_novo += nome[contador]
    contador += 1
    print(nome_novo)


print('\n')
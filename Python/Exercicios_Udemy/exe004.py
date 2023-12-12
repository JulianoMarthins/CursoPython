"""
        Faça um programa que peça ao usuário para digitar um número inteiro,
    informe se este número é par ou ímpar. Caso o usuário não digite um número
    inteiro, informe que não é um número inteiro
"""

print('\n')

num = input('Digite um número inteiro: ')

# Uma alternativa ao uso do try, seria verificar uma condicao com metodo isdigit()

try:
    num = int(num)

    if num % 2 == 0:
        print('Você digitou um número par')
    else:
        print('Você digitou um número ímpar')

except:
    print("Você digitou um valor inválido")

print('\n')
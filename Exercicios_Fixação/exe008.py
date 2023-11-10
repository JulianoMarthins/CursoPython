"""
    Programar uma calculadora usando while
    Usuário deve inserir 

"""
print('\n')

menu = """    
            Caculadora Python

        +   =>  Somar
        -   =>  Subtração
        *   =>  Multiplicação
        /   =>  Divisão

    "sair" para fechar o programa

"""

while True:
    op = input(menu).lower()

    if 'sair' in op:
        print('Fechando o programa')
        break

    # Bloco de código para contas de somar
    elif '+' in op: 
        print('Digite os números no qual deseja somar: ')
        num = input('Primeiro número:')
        num2 = input('Segundo número:')
        resultado = int(num) + int(num2)
        print(f'Resultado: {resultado}')

    # Bloco de código para contas de subtração
    elif '-' in op:
        print('Digite os números no qual deseja subtrair: ')
        num = input('Primeiro número:')
        num2 = input('Segundo número:')
        resultado = int(num) + int(num2)
        print(f'Resultado: {resultado}')
        
    # Bloco de código para contas de multiplicação
    elif '*' in op:
        print('Digite os números no qual deseja multiplicar: ')
        num = input('Primeiro número:')
        num2 = input('Segundo número:')
        resultado = int(num) + int(num2)
        print(f'Resultado: {resultado}')

    # Bloco de códigos para contas de divisão
    elif '/' in op:
        print('Digite os números no qual deseja dividir: ')
        num = input('Primeiro número:')
        num2 = input('Segundo número:')
        resultado = int(num) + int(num2)
        print(f'Resultado: {resultado}')

    else:
        print('Você digou um valor inválido, por favor, repita o processo')

print('\nObrigado por usar\n')




"""
        Faça um programa que receba o nome do usuário
        Crie um laço de repetição while onde execute mesmo número de caracteres do 
    nome digitado pelo usuário dentro do while, adicione a outra variavel letra 
    por letra do nome digitado pelo usuário

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
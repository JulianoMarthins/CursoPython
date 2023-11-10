"""
        Faça um programa que peça o primeiro nome do usuário. Se o nome tiver quatro 
    letras ou menos, escreva "Seu nome é curto";.
        Se o nome tiver entre 5 e 6 letras, escreva "Seu nome é normal
        Se o nome tiver mais que 6 letras, escreva "Seu nome é grande

"""
print('\n')

nome = input('Digite seu primeiro nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) <= 6:
    print('Seu nome possui um tamanho normal')
elif len(nome) >= 7:
    print('Seu nome é grande')

print('\n')

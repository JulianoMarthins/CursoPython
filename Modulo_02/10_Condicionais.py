"""
    Constantemente em um programa de computação existe a necessidade de desviarmos
    o caminho, realizar checagens, isso se faz com a palavra chave, if, elif e else

    if -> se
    else -> se não
    elif -> se não, se

    O bloco de código do if só será exacutado se a condição for verdadeira
    O bloco de código do else só será executada se a condição do if for falsa
    O bloco de código do elif será executado se sua consição for verdadeira, porem
    se a condição do primeiro if for falsa.

"""

print('\n')

idade = input('Digite sua idade: ')
idade = int(idade)

if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')


print('\n')
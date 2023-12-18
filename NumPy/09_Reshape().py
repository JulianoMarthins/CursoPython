"""
                        Np.reshape()

        A função reshape() é usada usada para alterar a forma de um array. Por
    exemplo, se você tem dados de vendas para duas semanas e quer reorganiz-alos em 
    uma matriz de 2x7 (duas semanas, sete dias por semana)

        A função recebe um array e o transformaça em uma matriz de um número x de
    dimensões a ser configurada pelo programador, no exemplo que daremos abaixo, 
    teremos um array com 14 valores, representando um valor por dia da semana,
    fechando assim, duas semanas de informações sobre as vendas de um estabelecimento.

        Ao usar a função reshape, passamos como argumento o nome da variavel de arrays
    e entre parenteses, como segundo arugmento, as informações de formatações, esta,
    precisa ser números exatos para diviões das informações do array, em outras 
    palavras, se o array tiver 14 valores, você poderá dividi-lo em 7x2 ou 2x7, criando
    assim, no primeiro caso, uma matriz com sete linhas e duas colunas, ou no segundo
    exemplo, que terá mais sentido para nosso exemplo, o 2x7, onde teremos duas linhas
    e sete colunas, representando, as linhas sendo semanas e as colunas os dias.
"""

import numpy as np
print()

# Vendas diárias
vendas = np.array([
    200, 220, 250, 210, 300, 280, 230, 210, 220, 240, 230, 210, 280, 220
    ])

# Reorganizazar os dados em uma matriz de 2x7
vendas_reshape = np.reshape(vendas, (2, 7))

print(vendas_reshape)

print()

# Array original
print('Array original: \n{}'.format(vendas))

# Atribudo .ndim retorna o número de dimenções do array
print(f'\nDimenções: {vendas.ndim}')

# Atributo .shape retorna quantos elementos tem dentro do array
print(f'Forma: {vendas.shape}')


# Realização dos mesmes testes acima, mas agora do o array bi-dimencional
print(f'\nArray Bi-Dimencional: \n{vendas_reshape}')

print(f'\nDimenções: {vendas_reshape.ndim}')

print(f'Forma: {vendas_reshape.shape}')


# Para acessar seus indices, posso pensar como as matrizes em Java, onde o primeiro
# valor do colchetes representa as linhas e o segundo, as colunas.

# Acesso das linhas da matriz
print('Linha 1: '.format(vendas_reshape[0]))
print('Linha 2: '.format(vendas_reshape[1]))

# Acessando o primeiro elemento de cada linha
print(f'Linha 1, elemento 1: {vendas_reshape[0][0]}')
print(f'Linha 2, elemento 1: {vendas_reshape[1][0]}')



# É possivel usar funções já conhecidas como .sum() por exemplo.
soma = np.sum(vendas_reshape)
semana_1 = np.sum(vendas_reshape[0])
semana_2 = np.sum(vendas_reshape[1])

print(f'\n1° Semana: R$ {semana_1:.2f}')
print(f'2° Semana: R$ {semana_2:.2f}')
print(f'Vendas totais: R$ {soma:.2f}')

# Podemos realizar calculos usando os eixos da matriz, visando que o eixo 0 representa
# a soma das colunas da matriz, em outras palavras, ele retornaria a soma das vendas
# na segunda feira da primeira semana com a segunda feira da segunda semana, e assim
#  em diante. Para realizar calculos pelas linhas, se usa o eixo apartir do valor 1

soma_dias = vendas_reshape.sum(axis=0)
semana = vendas_reshape.sum(axis=1)


print(f'\nVendas por dia:\n{soma_dias}')
print(f'\nVendas Semanais:\n{semana}')

# Lembre-se, Pensando como se fosse uma tabela de dias, com duas semanas, o eixo=0
# retorna a soma dos dias da semana, o eixo=1 retorna o valor das vendas de toda a
# semana. Ou seja:
# (axis=0) segunda + segunda, terça + terça, etc. <Soma  das vendas por dia>
# (axis=1) segunda + terça + quarta. etc. <Soma das vendas por semana>
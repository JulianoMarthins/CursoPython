print()

venda_produtos = [1500, 150, 2100, 1950]
produtos = ['Vinho', 'cafeteira', 'microondas', 'iphone']

# Precisamos ordenar a lista de produtos por ordem de venda, porem, a função sort da lista
# não pode ser utilizada pois, quando uzado, perderiamos a vinculação entre a ordem dos produtos
# forem a mesma ordem da quantidade vendida, mas, então, como podemos ordenar as duas listas
# mantendo vinculado o produto a quantidade vendida deste produto? O list comprehensions nos
# ajudará a tratar este caso.

# Para realizar a vinculação das listas, devemos criar uma lista auxiliar onde cada produto é 
# uma tupla contendo o nome do produto e a quantidade de vendas

# O método zip ira juntar as duas listas em uma só porem, para armazena-lo em uma variavel
# composta, o retorno do zip deve ser convertido para o tipo que se deseja trabalhar, neste
# caso, uma lista, ele pode ser convertido para qualquer variável composta, seja ela uma tupla,
# dicionário ou listas.
lista_auxiliar = list(zip(venda_produtos, produtos))

# Agora podemos armazenar uma nota lista do retorno da função sorted, que ordenará a lista
# pelo primeiro valor da tupla, neste caso, a quantidade de produtos vendidas, usaremos neste
# caso o reverse, que ordenará a lista de tuplas de trás pra frente deixando assim, na ordem
# dos produtos mais vendidos contidos na lista de tuplas
lista_auxiliar = sorted(lista_auxiliar, reverse=True)

# Faremos agora um list comprehensions para realizar um unbacking da lista de tupas e guardar
# em uma nova lista, somente o nome dos produtos na ordem de mais vendidos

produtos_mais_vendidos = [produto for vendas, produto in lista_auxiliar]

print(produtos_mais_vendidos)

print()
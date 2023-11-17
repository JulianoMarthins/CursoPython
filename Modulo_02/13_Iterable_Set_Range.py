"""
        Um iterable é uma estrutura que armazena dados que pode ser "iterada", ou
    seja, que você pode fazer um loop como um for dentro dela e ir passando de 
    item a item. É como se fosse um tipo de lista de coisas que você pode ir
    olhando cada um dos elementos dentro dela.

"""

                # Listas
print()

produtos = ['iphone', 'samsung galaxy', 'tv samsung', 'playstation 5']

for produto in produtos:
    print(produto.title())

     

                    # Range

print()


# O range cria uma contagem dentro dos valores passados no paramêtro, sendo o 
# primeiro elemento o número inicial,o segundo onde ele terminará, e o terceiro
# dará um valor de saltos da numeração, por exemplo, se os parâmetros forem 
# 1, 10, 2, o range retornará os número de dois em dois até o dez, sendo eles os 
# números 1, 3, 5, 7, 9

for num in range(1, 10, 2):
    print(num, end=' ')

lista = ['Juliano', 'Martins', 'Souza']
tupla = ('Juliano, Martins', 'Souza')
dicionario = {'Nome': 'Juliano', 'Sobrenome': 'Martins de Souza'}
set_list = {'Juliano', 'Martins', 'Souza'}

print()
print(type(set_list))

# Set é uma espécie de listas porem, não podem existir valores duplicados, sua
# criação é realizada com chaves, porem passado em seu argumento somente um tipo
# de valor, o que diferencia do dicinorio, pois este, precisa obrigatóriamente
# se passado chave e valor. Set não possui ordem fixa, logo, não deve ser acessado
# por indice.

# O uso do set é indicado quando precisamos analisar uma lista sem querer que exista
# repição de valores na mesma

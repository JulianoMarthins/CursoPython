"""
            Metodos básicos que o Python oferece

        * Items() -> Este metodo irá pegar todos os valores do dicinoário
    individualmente. Este método retornará uma lista de tuplas sendo contido nesta
    a chave como primeiro elemento e o valor como segundo elemento. Todos os dados
    do dicionário será armazenado em uma lista

        * Keys() -> Este método retornará uma lista com todas as chaves do 
    dicionário

        * Values() -> Este método retornará uma lista com todos os valores do 
    dicionario

      
"""
print()

vendas_tecnologia = {
    'notebook': 2500,
    'iphone': 15000,
    'sansung galaxy': 12000,
    'tv samsung': 1000,
    'ps5': 14300,
    'tablet': 1720,
    'notebook dell': 1700,
    'ipad': 1000,
    'tv philco': 2500,
    'notebook hp': 1000
}


# O método items pegará todos os elementos do dicionário e armazenara tudo em uma 
# lista, onde cada "chave, valor" do dicionário ficará dentro de uma tupla 
itens_dicionario = vendas_tecnologia.items()

# Retorna uma lista para todo o dicinoário, onde cada elemento chave valor, será
# criado uma tupla para seu armazenamento
print(itens_dicionario)

print()
# Um jeito mais fácil de visualizar esta lista de tuplas é executar o items em um for
for item in vendas_tecnologia.items():
    print(item)


# Pode ser feito o unpacking da tupla durante o uso do for
print('\nLista de produtos:')
for produto, quantidade in vendas_tecnologia.items():
    print('Produto: {:<20} Vendas: {}'.format(produto, quantidade))


# Mostrar na tela somente os produtos que venderam mais de 5000 unidades
print('\nLista de Produtos que venderam acima de 5000 unidades: ')
for produto, quantidade in vendas_tecnologia.items():
    if quantidade > 5000:
        print('Produto: {:<20} Vendas: {}'.format(produto, quantidade))




                    # Metodos .keys() e .values()

# keys() retornará uma lista com todas as chaves do dicionário
print()
chaves = vendas_tecnologia.keys()
print(chaves)

# Values() retornará uma lista com todos os valores do dicionário
print()
valores = vendas_tecnologia.values()
print(valores)

# No codigo abaixo observe que, mesmo adicionando os valores nas linhas de código
# abaixo do da leitura das chaves e valores da lista, estes valores são alterados
# se utilizados abaixo da linha de incrementação, isso porque, apensar deste 
# metodo retornar uma lista com as chaves e valores contidos no dicionario, esta
# não é uma lista comum, logo, não podemos manipula-las como fazemos nas listas
# criadas manualmente por código. Caso haja necessidade de realizar este procedimento
# deverá ser feito um casting dos valores contidos nas variaveis chaves e valores
# convertendo a "lista" retornada pelo dicionário por uma lista comum
print()
vendas_tecnologia['julianus phone'] = 20
print(chaves, '\n')
print(valores)

# Exemplo de conversão da lista criada por um dicionário por uma lista comum

print()
lista_chaves = list(chaves)
lista_valores = list(valores)

print('Conversão de "dict_values" por uma lista comum: ', type(lista_chaves))

# Uma das necessidade de conversão se da pela necessidade de ordenação do dicionario
# por ordem alfabética pelas chaves

print()

# Comando abaixo ordena a lista de chaves por ordem alfabética
lista_chaves.sort()
print('Lista de chaves ordenada: {}'.format(lista_chaves ))   


# O código abaixo imprime o dicionário em ordem alfabética
print()
for chave in lista_chaves:
    print('{:.<20} {:>10} unidades'.format(chave, vendas_tecnologia[chave]))
          
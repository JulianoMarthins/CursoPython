"""
        Usando módulos para ajudarr a resolver desafios

        Objetivo
            * Muitas vezes algum módulo vai ajudar a gente a resolver um desafio
        que talvez até conseguíssemos resolver de outra forma.

        Exemplo
            * Digamos que você está analisando todas as vendas dos produtos de um
        e-commerce e quer saber quais foram os cinco produtos que mais venderam
        (e suas respectivas quantidades de vendas), ou seja, queremos descobrir um
        top três produtos de forma simples


"""
print()

# O código abaixo analisa um dicionario e retorna os três maiores valores encontrados
# no dicionário
from collections import Counter

vendas_tecnologia = {
    'notebook asus': 2450,
    'iphone': 15000,
    'samsung galaxy': 12000,
    'tv samsung': 10000,
    'ps5': 14300,
    'table': 1720
    }

# Retorna a variável uma lista do tipo 'Collections.Counter', com os elementos
# do dicionário passado como argumento

aux = Counter(vendas_tecnologia)

# Impressão do tipo da variável aux
print(type(aux))

# Imprimi na tela 
print(aux.most_common(3))


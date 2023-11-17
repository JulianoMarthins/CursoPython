"""
        Nas aulas de listas, tivemos diversos exemplos do uso de duas listas para
    cada elemento, sendo, digamos, uma lista de produtos e outra lista de valores.
        O uso do dicionário é claramente a evolução deste método e agora, 
    aprenderemos como tranformamos duas listas relacionadas em um dicionario
    sendo uma lista para as chaves, e a outra lista para os valores.

"""

print()

# Criação de uma lista de produtos e outra lista com os valores do produto
produtos = ['computador', 'monitor', 'impressora']
valores = [3500, 1000, 650]

# O método do dicionario, .fromkeys() recebe em seu argumento os listas como 
# parâmetros, elas terão todos seus elementos convertidos para chave e valor do 
# dicionário, sendo, o primeiro parâmetro para as chaves, e o segundo para os valores
 
dicionario = dict.fromkeys(produtos, valores)

for chave, valor in dicionario.items():
    print('Chave: {:<20} Valor: {:}'.format(chave.capitalize(), valor))


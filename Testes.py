print('\n')
 
vendas = [
    ['maçã', 5],
    ['banana', 15],
    ['azeite', 1],
    ['vinho', 3],
]

produtos = []

while True:

    nome = input('Nome do produto: ')

    if not nome:
        print('Programa será fechado')
        break
    
    quantidade = input('Unidades: ')
 
    produtos.append(nome)
    produtos.append(quantidade)

    vendas.append(produtos)
    produtos.clear()

print('Lista de produtos')


for prod in vendas:

    nome = prod[0]
    quantidade = prod[1]

    print(f'Produto: {nome} {quantidade} unds')

print('\n')
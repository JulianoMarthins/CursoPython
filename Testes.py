print('\n')

cardapio = [
    ('cachorro_quente', 100, 1.20),
    ('bauru_simples', 101, 1.30),
    ('bauru_ovo', 102, 1.50),
    ('haburguer', 103, 1.20),
    ('cheeseburguer', 104, 1.30),
    ('refrigerente', 105, 1.00),
]

preco = 0
lista_produtos = []

while True:
    codigo = int(input('código do produto: '))

    for produto in cardapio:
        if codigo in produto:
            nome, codigo, valor = produto
            lista_produtos.append(nome)
            preco += valor
    if codigo == 0:
        print('Pedido finalizado')
        break

print('\nPedido: ')
for name in lista_produto:
    print(name)
print(f'Valor a pagar: {preco:.2f}')


print('\n')
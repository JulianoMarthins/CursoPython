"""
        Um uso mais 'natural' das Tuplas é, ser passada como um valor de uma lista, 
    digamos que você tenha uma lista de pessoas, e cada pessoa possui um nome, cpf, 
    endereco, etc... Você pode armazenar todos esses dados em uma tupla e adicionar
    esta tupla em uma lista


"""

print('\n')

# Abaixo, temos uma lista de produtos, sendo produtos, uma tupla
vendas = [
    # Data da venda | Produto | Cor | Caracteristica | Preço | Und. vendida 
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
    
]

# Como calcularmos o valor total de venda do iphone x azul?
# Basta mutilplicarmos o valor unitário pela quantidade vendida

# Abaixo, acessamos os valores desejados utilizando o mesmo conceito de Matriz em
# Java, onde percorremos o primeiro produto pelo indice 0, como se fosse a coluna, 
# e na linha, acessamos os valores da tupla, do produto, no caso, o indice 4 acessa
# o valor unitário e o indice 5 acessa a quantidade total de venda

faturamento = vendas[0][4] * vendas[0][5]
print(f'Faturamento: R$ {faturamento:.2f}') # Retorno do total vendido

# Em Python, podemos utilizar o concetio de unpacking para nomearmos cada elemento
# da lista deixano o código mais legivel

# Abaixo, passamos todos os valores o primeiro produto para variaveis simples
data, produto, cor, caracteristica, preco, total_vendas = vendas[0]
# Calculo básico sobre faturamento 
faturamento = preco * total_vendas
print(f'\nFaturamento: R$ {faturamento:.2f}') # Retorno do total vendido



print('\n')
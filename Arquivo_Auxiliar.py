print()

# Criar dicionario

# loop infinito, usuário entra o nome do produto, vendas do mes atual e
# a taxa de crescimento

# Dentro do loop, use uma declaração if para verificar se o usuario digitou sair

# se sair, break

# usar a entrada do usuario para calcular o crecimento

# depois do loop encerrado, use o for para iterar sobre o dicionário e mostrar
# as previsões de vendas para cada produto

def previsao_venda(dicionario, produto, vendas, crescimento):
    vendas += vendas * crescimento / 100
    dicionario[produto] = int(vendas)



dicionario = {}

while True:
    
    print('\nAdicione um novo produto')
    produto = input('\nNome do produto: ').title()

    if 'Sair' in produto:
        print('\nPrevisão de crescimento dos produtos:\n')
        break
    
    try: 
        vendas = int(input('\nVendas: '))
        crescimento = int(input('\nPrevisão de crescimento (%): '))
        previsao_venda(dicionario, produto, vendas, crescimento)
    except:
        print('Valor digitado é inválido')

    
for chave, valor in dicionario.items():
    print('Produto: {} Previsão: {} und'.format(chave, valor))

    
   



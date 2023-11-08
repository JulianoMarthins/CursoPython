
# Menu do programa
menu = """
                        Programa de compras

            1 - Adicionar mercadoria no carrinho de compras
            2 - Retirar mercadoria do carrinho de compras
            3 - Mostra o carrinho de compras
            0 - Sair do programa

"""
print('\n')


# Main
carrinho = []

while True:
    op = input(menu)

    if '1' in op:
        print('\nColocar produtos no carrinho')

        try:
            nome = str(input('\nNome do produto: '))
            preco = float(input('Preço: '))
            quantidade = float(input('Quantidade: '))
            valor = preco * quantidade

            produto = [nome, valor, quantidade] 
            carrinho.append(produto)
        except:
            print("Erro ao adicionar produto")
    
    elif '2' in op:
        try:
            print('\nRemover produto do carrinho')
            indice = int(input('Digite o ID do produto: '))
            del carrinho[indice]
            
        except:
            print('Produto não listado em seu carrinho ')
        

    elif '3' in op:
        if carrinho:            
            for indice, produto in enumerate(carrinho):
                print(f'ID: {indice} {produto}')

        else:
            print('\nCarrinho vazio')

    elif '0' in op:
        print('\nFechando o programa\nObrigado por usar')
        break

    else:
        print('\nValor digitado é inválido')


print('\n')

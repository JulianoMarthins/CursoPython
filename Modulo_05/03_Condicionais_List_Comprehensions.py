"""
        Você pode adicionar condições no meio do list Comprehensions, a condição deve ficar ao
    final do código

"""

meta = 1000
venda = [1500, 150, 2100, 1950]
produto = ['vinho', 'cafeteira', 'microondas', 'iphone']

# Na linha de código abaixo, examinamos se o número de produtos vendidos na lista vendas é
# superior a 1000, retornando True, adicionamos a variavel acima_media o nome do produto que 
# está no mesmo indice da variavel vendas, obtendo assim, o nome do produto correspondente
# aquela vaga.

acima_media = [produto for i, produto in enumerate(produto) if venda[i] > meta]

print('Produtos acima da média:\n{}'.format(acima_media))
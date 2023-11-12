"""
        Dicionario é outro tipo de estrutura de dados assim como as tuplas e listas,
    a diferença entre dicionários e as outras estruturas de dados que ele é 
    acessado por uma chave, em vez de indexação.

        Logo, podemos afirmar que o dicionário é uma estrutura de dados que 
    utilizada chave, valor, quando precisarmos acessar um valor específico do
    dicinoário, vamos acessar utilizando a chave ao invés de indice..

"""
print()

mais_vendidos = {
    'tecnologia': 'iphone',
    'refrigeracao': 'ar consul 12000 btu',
    'livros': 'o alquimista',
}

vendas_tecnologia = {
    'iphone': 1500,
    'samsung galaxy': 1200,
    'tv samsung': 1000,
    'playstation 5': 14300
}

livro = mais_vendidos['livros'].capitalize()

print(livro)

"""
        Não confie na ordem dos dicionários, use as chaves para acessar os valores
    
        Python versões antigas x versões novas

    * Dicionários eram 'sem ordem'. Atualmente tem ordem, mas o certo é usar as
    chaves

    * Duas formas de pegar o valor:
    dicionario[chave]
    dicionario.get(chave)
    
"""
# Primeiro método para acessar o valor da chave iphone
print(vendas_tecnologia['iphone'])

# Segundo método para acessar o valor da chave iphone
print(vendas_tecnologia.get('iphone'))

# A difenreça no uso entre ele é que, no segundo caso caso não exista a chave 
# passada em seu argumento, ele retornará None, já o primeiro método, retorna 
# um erro

# Você pode realizar uma verificação para saber se existe a chave dentro do 
# dicionário

if 'copo' in mais_vendidos:
    print(mais_vendidos['copo'])
else:
    print('Chave inexistente no dicionário')

# Outro método de verificação

if vendas_tecnologia.get('copo') == None:
    print('Chave inexistente no dicionário')
else:
    print(vendas_tecnologia.get('copo'))



"""
        Crie um programa que analise um texto fornecido pelo usuário. O programa deve contar o número de palavras (independentemente
    se há repetição ou não), a quantidade de cada palavra e a quantidade de cadas letra. Ignore a diferenciação entre letras
    maiúsculas e minúsculas.

        O programa deve conter uma função chamada analisar_texto que recebe o texto como parâmetro e retorna a contagem de palavras, 
    a frequência de palavras e a frequência de letras. A função deve ser devidamente documentada

    
    Olá mundo! Este é um teste. Olá novamente.

"""


print()

def analisar_texto(args):
    """ A funçõa recebe um texto como argumento, trata ele retirando toda a acentuação e deixando todas as letras minusculas.
    Retorna a quantidade de palavras passadas na frase, quantas vezes cada palavra e cada letra apareceram na frase

    Parametros:
        args (str): Recebe uma String
        
    retorno:
        Contagem (int): Quantidade de palavras contidas na frase
        Palavras (int): Frequência de palavra contida na frase
        Letras (int): Frequência de letras contida na frase   
    """
        
    args = args.lower()
    args = args.replace('string.punctuation', '')
    args = args.split()

    lista_palavras = []
    lista_letras = []
    contagem = 0

    for palavras in args:
        lista_palavras.append(palavras)

        for letras in palavras:
            lista_letras.append(letras)
        contagem += 1
    
    palavras = Counter(lista_palavras)
    letras = Counter(lista_letras)
    
    return contagem, palavras, letras



import string
from collections import Counter

print('Vamos analisar sua frase')
texto = input('\nInsira sua frase: ')
print()

contagem, palavras, letras = analisar_texto(texto)

print(f'Contagem de palavras: {contagem}')
print(f'Frequência das palavras: {palavras}')
print(f'Frequência das letras: {letras}')


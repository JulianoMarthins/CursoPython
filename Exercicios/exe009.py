print('\n')

frase = input('Digite seu nome: ').lower()

i = 0
contagem_letras = 0
letra_mais_votada = ''

while i < len(frase):
    letra = frase[i]

    if letra == ' ':
        i += 1
        continue
    
    cont = frase.count(letra)

    if contagem_letras <= cont:
        letra_mais_votada = letra
        contagem_letras = cont
    
    i += 1
    
print('Letra que apareceu mais vezes:')
print(f'Letra "{letra_mais_votada.upper()}" apareceu {contagem_letras} vezes')

print('\n')
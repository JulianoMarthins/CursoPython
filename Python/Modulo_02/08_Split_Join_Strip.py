"""

            Split e Join com list e str
            Split   =>  Divide uma string retornando uma lista
            Join    =>  Une uma string
            Strip   =>  Retira espaços vazios no inicio, final ou toda a string.
            
        No Strip, tem variações em... lstrip, tira espaços a esquerda e rstrip que
        tira os espaços da direta

"""
print('\n')



frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split(',')

print(lista_palavras)

for i, frase in enumerate(lista_palavras):
    print(lista_palavras[i].strip())




print('\n')

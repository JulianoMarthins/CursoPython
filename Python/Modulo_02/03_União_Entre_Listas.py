""" 
        Juntar listas, ordenação


"""
print()

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

# Ao criar uma terceira lista, podemos definir os valores de outras listas
# concatenando-as
lista_c = lista_a + lista_b
print(lista_c) # Retorna os itens da lista a e b

# O comando abaixo não retorna nenhum valor, porem, ela copia os valores da lista 
# passada como argumento
lista_a.extend(lista_b)
print(lista_a) 

# Podemos observar que o método aceita elementos repetidos extenção da lista
lista_a.extend(lista_c)
print(lista_a)



                               # Ordenações nas listas

# Lista com os consoles principais de cada geração
consoles = [
    'Atari 2600', 'Nintendo', 'Master System', 'Mega Drive', 'Super Nintendo',
    'Nintendo 64', 'Playstation', 'Game Cube', 'Dreamcast', 'Nintendo DS', 
    'Xbox', 'Nintendo Switch', 'PSP'
           
]

# Lista sem ordenação, é impresa na ordem de contrução da lista
print('\nLista de consoles não ordenada: \n{}'.format(consoles))

# Ordenação da lista, é ordenada por ordem alfabética
consoles.sort()
print('\nLista de consoles ordenada: \n{}'.format(consoles))

# O metódo reverse() retornará a lista ordenada afabeticamente de trás pra frente
consoles.reverse()
print(f'\nLista de consoles ordenada de trás pra frente: \n{consoles}')

# Sobre ordenação, é muito importante resaltar que este processo é realizado
# com base na ordem alfabética porem, o Python ordenada palavras com letras
# maiusculas com prioridade sobre minusculas

nomes = ['Juliano', 'aline']

nomes.sort()
print(f'\nDemonstração da priorida de letras maíusculas sob as minusculas\n{nomes}')
# No caso acima, o retorno será primeiro Juliano, e em segundo aline, isso porque
# Juliano está com a primeira letra maiusculo enquanto aline, está com a primeira
# letra minuscula. Caso aline seja escrito com letra maíuscla, ela ser retornada
# como primeiro elemento neste caso da lista de nomes.

# Um modo de evitar este problema é o tratamento das strings, colocando todos os
# elementos da lista com o mesmo padrão de formatação, seja ele sendo todas as 
# letras minusculas, todas maiusculas ou com a primeira letra maiuscula.



# Em casos onde se use duas listas que estão relacionadas uma com a outra, deve-se
# tomar muito cuidado com o fato da ordenação pois os elementos que antes estavam
# relacionados pelo indice, não será mais possivel está relação

# Exemplo

produto = ['Java', 'Python', 'MySQL']
precos = [535, 997, 320]

# Veja no caso assim que, o indice 0 da lista de produtos, retorna o curso de python
# enquanto o indice 0 da lista de preços, retorna o valor de 997, sendo este, o 
# preço de venda do curso de Python, e assim com o indice um, que retornará o curso
# de java no preço de 535 e no indice 2, que retornará o curso de MySQL no preço de
# 320 reais
print('\n')

for i in range(len(produto)):
    print('Curso: {} Preço: R$ {:.2f}'.format(produto[i], precos[i]))

# Abaixo podemos observar que ao usar o comando sort em ambas as linhas, os valores
# e os preços terão alteração por causa do ordenamento das listas

print('\n')
precos.sort()

for i in range(len(produto)):
    print('Curso: {} Preço :R$ {:.2f}'.format(produto[i], precos[i]))


                    # Modificações de lista "JOIN"

consoles = [
    'Atari 2600', 'Nintendo', 'Master System', 'Mega Drive', 'Super Nintendo',
    'Nintendo 64', 'Playstation', 'Game Cube', 'Dreamcast', 'Nintendo DS', 
    'Xbox', 'Nintendo Switch', 'PSP' 
]

# O comando .join acresenta algum caracter previamente definido como separador entre
# cada elemento da lista. Ele recebe o valor a ser alterado, para depois entrar com
# o metodo .join, sendo em seu parâmetro, passado a lista a ser tratada

print()

# No código abaixo, cada elemento da lista, será adicionado o comando \n, uma
# quebra de linha, isso a cada elemento encontrado na lista
print('\n'.join(consoles))

print()

# Outro exemplo é a adição de um novo caracter, desta vez, adicionaremos o #
print(' # '.join(consoles))


                   # Modificações de listas, "split"

print()
nomes = 'Juliano, Thiele, Larissa, Clair, Regina, Eduardo, Gabriel, Tiago'

# O metodo split, recebe como argumento um caracter separador, no caso, usaremos
# a ",". O metodo retornara uma lista e a cada vez encontrado o caracter passado
# como o argumento, criando assim, uma lista com seus valores conforme exemplo
# abaixo.

lista = nomes.split(', ')

print(lista)

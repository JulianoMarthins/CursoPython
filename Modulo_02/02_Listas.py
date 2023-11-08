"""
        Listas em Python

        Durante as aulas de Strings foi comentador que uma string nada mais era do que uma lista de caracteres,
    seguindo está lógica, tudo o que aprendemos sobre o fatiamento de strings, acesso por indices, se aplica as listas
    e futuramente, veremos que se aplicará as Tuplas.

        As listas aceitam todos os tipos primitivos em suas estruturas, para adicionar elementos a listas existem
    comando específicos como o append, que serve para adicionar elementos ou o del, que serve para apagar

        Sempre que usarmos o append, o valor passado como argumento entrará no final da lista, a mesma não mantém a
    ordem e inserção, podem ser ordenada com comandos específicos, pode receber outra lista, tupla ou dicionários como
    valor.
        Sempre que usarmos o comando del, para deletar algum valor de uma lista, o Python mexerá em todos os elementos
    da lista, por exemplo, se tivermos uma lista de números inteiros com os valores vão do número 1 ao 100, caso seja
    necessário deletar da lista o valor do índice 8, este não irá ficar vazio, o pytho ira locomover o valor do índice
    9 para o lugar do 8, o 10 para o 9, o 11 para o 10, e assim por diante.

        Já é simples pensar que, em listas muito grandes, o programa se sobrecarregará nesta parte do código, pois
    seria muito valores para o Python mexer ao organizar a lista, logo, o recomendado é que você adicione e elemine
    sempre os valores no final da lista

    Vejamos abaixo alguns exemplos de códigos usando listas
"""



# O jeito mais comum de declararmos uma lista é utilizando colchetes
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numeros)

# Podemos acessar e alterar elementos da lista pelo indice
numeros[2] = 300
print(numeros)

# Com o comando del, excluíremos o valor passado como índice
del numeros[2]
print(numeros)

# Adicionando um valor ao final da lista
numeros.append(72)
print(numeros)

# Apaga o ultimo elemento da lista
numeros.pop()
print(numeros)

# Adiciona o valor ao final da lista, pode ser misturados tipos primitivos nas listas
numeros.append('BBB')
print(numeros)

# insere o valor 5 no index 1
numeros.insert(1, 5)
print(numeros)

# Exemplo de for para percorrer todos os elementos da lista
for x in numeros:
    print(x)

# Apagará toda sua lista
numeros.clear()

# Lista vazia
print(numeros)

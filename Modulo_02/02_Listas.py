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

                    # CRIAÇÃO DE UMA LISTA

# O jeito mais comum de declararmos uma lista é utilizando colchetes
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numeros)

# Podemos acessar e alterar elementos da lista pelo indice
numeros[2] = 300
print(numeros)



                    # DELETAR ELEMENTOS DE UMA LISTA
# Com o comando del, excluíremos o valor passado como índice
del numeros[2]
print(numeros)

# Apaga o ultimo elemento da lista
numeros.pop()
print(numeros)

# O pop tabém pode apagar passando o indice como parâmetro
# Não há obrigatóriedade, mas o item removido também pode ser armazenado em uma
# variavel
removido = numeros.pop(2)
print(f'Item removido da lista: {removido}')

# Remove o elemento passado no argumento, no caso, remove o elemento 90
numeros.remove(90)



                    # ADICIONAR ELEMENTOS A LISTA

# Adicionando um valor ao final da lista
numeros.append(72)
print(numeros)



# O comando insert serve para colocar um valor no meio da lista por meio da
# indexação.
numeros.insert(1, 5)
print(numeros)

numeros.append(1300)

                    # VERIFICAÇÕES NAS LISTAS

# Verificar indice do elemento passado como argumento, na lista
indice = numeros.index(1300)
print(f'Indice do valor 1300: {indice}')



                    # TRATAMENTOS DE LISTA, VALORES MAIORES E MENORES

# Retorna o maior elemento da lista, em caso de string, retorna o a última palavra
# da lista pela ordem alfabética
maior = max(numeros)
print(f'Maior valor da lista: {maior}')

# Retorna o menor elemento da lista, em caso de string, retorna a primeira palavra
# da lista pela ordem alfabética
menor = min(numeros)
print(f'Menor valor da lista: {menor}')

# Retorna quantos elementos tem na lista
quantidade = len(numeros)
print(quantidade)

# Pegar o indice do maior elemento da lista
indice_maior = numeros.index(max(numeros))
# Obviamente, para acessar o menor valor da lista, basta substituir o metodo max()
# pelo metodo min()


                    # EXEMPLO DE ITERAÇÃO DE UMA LISTA COM FOR
# Exemplo de for para percorrer todos os elementos da lista
for x in numeros:
    print(x)

                    # DELETAR TODOS OS ELEMENTOS DA LISTA

#   Apagará todos os elementos da lista, deixando ela vazia
numeros.clear()

# Lista vazia
print(numeros)


                 # EXEMPLOS DE FINALIZAÇÃO DE AULA

print('\n')
valores = [10, 30, 90, 7, 42, 71]

maximo = max(valores)
menor = min(valores)


indice_maior = valores.index(max(valores))
indice_menor = valores.index(min(valores))

print('Maior elemento da lista: {}'.format(maximo))
print('Menor elemento da lista: {}'.format(menor))

print('Indice do maior elemento: {}'.format(indice_maior))
print('Indice do menor elemento: {}'.format(indice_menor))

print()
for indice, valor in enumerate(valores):
    print(f'{indice}: {valor}')

"""
                Reforço de conteúdo

        Para adicionar elementos a lista, você deve usar o comando:
                .append() e passar no argumento, o valor a adicionar

        Para remover elementos da lista, temos duas funções distintas:
                .pop() e passar no argumento o indice do valor a remover -> 
            Exemplo -> lista.pop(1)
                .remove() e passar no argumento o valor a remover -> 
            Exemplo -> lista.remove('Juliano')
            

"""

if numeros:
    ...
else:
    pass


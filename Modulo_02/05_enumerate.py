"""
        Enumerate serve para numerar por indices valores de uma lista

        A finalidade do enumerate é númerar cada valor de uma lista ou dupla, números esses que podemos utilizar como indices
    para acessar cada elemento quando necessário, o retorno da enumeração será de uma tupla de listas, onde cada lista, contem
    o indice e o valor dos elementos da lista\ tupla passada como parametro ao método.

    

                                        Para reforço

                                        Lista       =   []
                                        Tupla       =   ()
                                        Dicionário  =   {}


"""
print()

# Criação de uma lista de nomes, linha abaixo, adição de um novo nome a lista
nomes = ['Juliano', 'Álvaro', 'Maikon', 'Emerson']
nomes.append('João')

# O retorno que o enumerate fará no caso acima, é a referência de memória
nomes_numerados = enumerate(nomes)
print(f'Referência em memória: {nomes_numerados}')

# Se convertermos a para uma lista, o enumerate retornara uma tupla contendo o numeração criada e o valor de cada elemento

# Para fins didáricos, o comando star=19 fará a contagem iniciar no indice 19
nomes_numerados = list(enumerate(nomes, start=19))
print(f'\nTuplas enumeradas: {nomes_numerados}')


"""

Obs: 
            Enumerate é um iterável, o que siginifica que podemos chamar a função next para acessar os valores

print(f'Função next: {next(nomes_numerados)}')

            Podemos acessar todos os elementos contidos na variavel nomes_numerados se usarmos o enumerate em um laço for

print('Abaixo, acesso da varaivel nomes_numerados pelo for')

for item in nomes_numerados:
    print(item)

"""


# Veremos a seguir o modo correto do uso do enumerate com o laço de repetição for, não sendo possivel utilização do mesmo
# como nas linhas acima porque, ao executar o programa, o enumerate consumirá linhas dos códigos, exemplo:
# Neste codigo atual, na linha 16, o enumerate consumirá o primeiro valor da varaivel nome, assim, ao chegar na linha 20,
# o enumerate consumirá as outras duas linhas restantes em nossa lista, causando, no código abaixo, retornando ao usuário
# a referência de memória e não, os valores da variavel nome. Nesta parte, para testes, vou comentar os códigos acima

print() 

for indice, nome in enumerate(nomes):
    print(f'{1 + indice} {nome}')


print()

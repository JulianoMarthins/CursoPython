"""
                            Intrudução ao NumPy

        NumPy significa 'Numerical Python', é uma biblioteca fundamental para a
    computação científica em Python. Ela fornece suporte para arrays e matrizes, 
    além de funções matemáticas para operações com esses objetos. É, também, a
    base da biblioteca Pandas.

        Um array é uma estrutura de dados que armazena valores do mesmo tipo. Em
    Python, isso é uma grande vantagem porque economiza espaço e permite operações
    mais eficientes.

"""

import numpy as np

print()

array = np.array(['a', 'b', 'c', 'd', 'e'])
print('Impressão da variável de Arrays: {}'.format(array))

# Pegando os elementos do array por indexação, valores do array -> 1, 2, 3, 4, 5

# Retorno -> a
print('Indice "0": N° {}'.format(array[0]))

# Retorno -> b, c, e,
print('Indice "1:4": N° {}'.format(array[1: 4]))

# Retorno -> a, b, c, d, e
print('Indice "0:-1": N° {}'.format(array[0:-1]))

# Rertorno -> a, c
print('Indice "0:-1:2": N° {}'.format(array[0:-1:2]))

# Retorno -> a, c, e
print('Indice "0::2": N° {}'.format(array[0::2]))

# Podemos observar que o acesso a indexação dos arrays, é igual aos usados em outros
# trechos do curso como para assesar os elementos de listas, tuplas, ou fragmentação
# de strings
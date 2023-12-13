"""
        A biblioteca NumPy é amplamente utilizada para realizar operações númericas
    e computacionais eficientes em Python. ela fornece estruturas de dados de alto
    desenpenho, como arrays multidimensionais e funções matemáticas para manipulação
    desses arrays. 

        Com o NumPy você pode realizar cálculos complexos, processamento de dados,
    álgebra linear, geração de números aleatórios e muito mais. É uma ferramente
    essencial para cientista de dados e programadores que lidam com análise numérica
    e computação científica.
       
"""

import numpy as np
import time

"""
        É muito importante entender qual a diferneça de uma lista para um array, 
        
        Um Array é uma estrutura de dados que armazena valores de um mesmo tipo, 
    em Python, isso é uma grande vantagem porque economiza espaço e permite operações
    mais eficientes.
        
        Uma lista é uma das estruturas de dados mais básicas em Pytho. ela pode 
    conter qualquer tipo de elemento, como números, string, outras listas, e todos
    eles podem ser de tipos diferentes.
    
"""
print()

array = np.array([1, 2, 3, 4, 5])

print('ArrayList: {}'.format(array))

# Caso seja criada uma lista, você pode passar qualquer tipo de elementos em sua
# composição, int, float, bool, str, e trabalhar com eles com seu tipo nativo.

# Já em um Array, todos os elementos são obrigatóriamente o mesmo tipo primitivo, 
# caso seja passado diferentes tipos primitivos para o array, o mesmo converterá
# este tipos para o padronizar todos os valores internos no array, será tentado 
# a conversão para o tipo primitivo mais gererico possível.
 
 # Observe que ao trablhar com a biblioteca de NumPy, para ver o tipo da variavel
 # deve ser usar o metodo .dtype, o retorno será o tipo primitivo e a quantidade  
 # gasto em memória em kbits

print(array.dtype) # Retornará int32, represntando um inteiro de 32kbits


#                       Operações Matemáticas

# O grande foco desta biblioteca são nas operações matemáticas

# Para acrescentar cada elemento de uma lista, somar este ao valor um, você
# precisaria realizar o código abaixo

print()

lista = [1, 2, 3, 4, 5]
nova_lista = []

for num in lista:
    nova_lista.append(1 + num)

print('Soma utilizando for: {}'.format(nova_lista))

# O código para somar um a cada valor da lista não é complicado mas, em listas grandes
# ele tornará o programa mais lento e, devemos lembrar que, a ideia da utilização
# do NumPy é de trabalhar com grande volume de dados.

# A ideia de realizar calculos para cada elemento da lista em NumPy é feita conforme
# código abaixo

print()
novo_array = array * 2 # Multiplicará cada elemento do array por dois

print(f'Multiplicação pelo NumPy: {novo_array}')


# Desempenho: Para grandes quantidades de dados, os arrays NumPy são significativamente
# mais eficientes em termos de memória e desempenho do que as listas em Python.
# Abaixo veremos um exemplo que demonstra isso: 

# Criamos uma lista e um array com um valor de dez milhões de números
print()
lista = list(range(1, 100_000_001))
array = np.array(range(1, 100_000_001))

# Cacluar a soma de todos os números da lista
inicio = time.time()
soma_lista = sum(lista)
fim = time.time()

print('Soma da lista: {}'.format(soma_lista))
print(f'Tempo da soma na lista: {fim - inicio:.2f} segundos') # Retorno 2.43seg

print()

# Calcular a soma de todos os números do Array
inicio = time.time()
soma_array = np.sum(array)
fim = time.time()

print(f'Soma do Array: {soma_array}')
print(f'Tempo da soma no Array: {fim - inicio:.2f} segundos') # Retorno 0.03seg


"""
                Diferenças chave entre lista e array

        1. Tipos de Dados: As listas podem armazenar elementos de tipos diferentes
    tempo, enquanto os arrays armazenam elementos do mesmo tipo.

        2. Operações matemáticas: Você pode realizar operações matemáticas em todos
    os elementos de um array de uma vez, o que não é possível com listas.

        3. Desempenho: Arrays são mais eficientes em termos de memória e desempenho
    do que listas quando se trabalha com grandes volumes de dados numéricos.

        4. Funcionalidades: NumPy arrays vêm com várias funções integradas para
    operações matemáticas e científicas, como média, soma, multiplicação de matrizes,
    etc., que não estão disponíveis com listas.
   
"""
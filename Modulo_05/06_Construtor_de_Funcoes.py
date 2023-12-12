""" 
        Uma grande utilidade das expressões lambdas, além do usos da aula 05 deste módulo, é
    a utilização para a criação de contrutor de funções. Nesse caso, usaremos as expressões
    lambdas no retorno de uma função, assim, a variavel que recebe este retorno se torna uma
    função, podendo ser assim reutilizada como tal  

"""

# A função abaixo possui em seu retorno uma expressão lambda
print()

def calcular_imposto(args):
    return lambda x: x * args

# O retorno da expressão lambda contida na função 'calcular_imposto' transformará a variavel
# produto em uma função
produto = calcular_imposto(1.3)

# A variavel produto foi transformada em uma classe, pode ser passada valores em seu argumento,
# sendo utilizada assim, par arealizar os calculos de impostos pela função calcular_imposto
print(f'Calculo do imposto: {produto(100)}')

print()
# A varivavel produto está classificada como uma classe, demostrada no código abaixo
print(f'Tipo da variável que recebeu o resultado da função que retornou uma expressão' +
      'lambda: {type(produto)}')


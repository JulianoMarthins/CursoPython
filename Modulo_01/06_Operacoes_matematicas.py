"""
    Matemática na programaçõa e um os pilares, não exatamente o ato de realizar contas
    mas sim, a lógica utilizada para resolver os problemas matemáticos são os mesmos
    que usaremos na programação

    Veja a similariedade do conta matemática abaixo e a mesma conta sendo atribuida a uma
    variavel

    Matemática
    X = (2 + 1) * (4 + 3)

    Código
    nome_variavel = (2 + 1) * (4 + 3)

    Assim como na matemática, teremos ordens de prioridade a execução do código,
    sendo priorizado

    1.   (n + n)    => Contas dentro de códigos
    2.   **         => Potencia
    3.   * / // %   => Multiplicação, divisão, divisão inteira, resto da divisão
    4.   + -        => Soma, subtração

"""

print('\n')

adicao = 10 + 10.2
print(f'Adição = {adicao}')

subtracao = 10 - 5
print(f'Subtração = {subtracao}')

multiplicacao = 10 * 10 # retorno sempre será do tipo primitovo float
print(f'Multiplicação = {multiplicacao}')

divisao = 10 / 2.2 # divisao simples, retorna um número float, não pode dividir por zero
print(f'Divisão = {divisao}')

divisao_inteira = 10 // 2.2 # retorna somente o valor inteiro da divisão, esten caso, 5
print(f'Resto inteiro da divisão = {divisao_inteira}')

potencia = 2 ** 3
print(f'Potencia = {potencia}')

resto_divisao = 64 % 4
print(f'Resto da divisão = {resto_divisao}')

print('\nPresendência de operadores')

conta = 1 + 1 ** 5 + 5 # Retorna 7
print('Conta 01: ', conta) 

conta = (1 + 1) ** (5 + 5) # Retorna 1022
print('Conta 01: ', conta) 


print('\n')


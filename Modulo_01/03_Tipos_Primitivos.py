"""
    Na aula passada falamos sobre o tipo primitivo String, porem, existem mais tipos
    primitivos em python

    String | str => String são textos, conjuntos de caracteres que devem ser definidos
    dentro de aspas simples

    Integer | int => Integer são os números reais, todo e qualquer número inteiro

    Float | float => Float são os números com casas decimais

    Boolean | boll => Boolean são tipos primitivos lógicos, ao realizar comparações
    entre valores, o boll retornará somente dois valores, ou True, ou False

"""

print('Exemplo de números inteiros: ')
print(11, -11, 0)
num = 0
print(type(num))

# Na programação, virgula é para concatenação, para números com casas decimais
# deve ser usado um ponto, para separar as casas decimais
print('Exemplo de números float: ')
print(11.0, 11.5, -23.5)
num = 3.1
print(type(num))

print('Exemplo de Strings: ')
print('11.0, Juliano, def5213d')
texto = '3.1'
print(type(texto))

"""
    Para o tipo primitivo bool, devemos, digamos, questionar o computador sobre uma condição onde o mesmo retornará
    somente verdadeiro ou falso, não há outra possibilidade de resposta e só pode ser uma das opções.

"""

print(10 == 10) # Retorna True, confirmando que dez é igual a dez
print(10 == 11) # Retorna False, confirmando que dez não é igual a onze
print(type(10 == 10))


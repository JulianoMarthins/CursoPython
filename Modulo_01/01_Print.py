print('\n')

# Imprime na tela os números 12 e 34
print(12, 34)

# Imprime na tela os números 56 e 78, a virgula serve para concatenação entre os 
# valores na impressão
print(56, 78)

# O codigo sep='' serve para separar os valores passado como argumento na função print
# Os valores serão jutandos pois, no separador, não foi adicionado espaço vazio
print(18, 55, sep='')

# Abaixo podemos ver a separação com um espaço vazio
print(22, 36, sep=' ')

# Podemos utilizar qualquer caracter como separador
print(55, 97, sep='-')

# Com o comando end='', podemos manipular o que colocaremos ao final da frase
print(57, 32, end='##')

# observe que neste caso, a linha não será pulada como antes, ao realizar dois prints
print(21, 57, end='%%')
print('Não pulou a linha')

# O código padrão para pulo de linhas é o \n

print(42, 37, end='##\n')
print("Agora pulamos a linha")

print('\n')
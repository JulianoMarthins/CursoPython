print('\n')

# O código abaixo mostrará a mensagem ao usuário, e o mesmo deverá inserir algum dado e guardar na variavel
# Seja qual for o tipo de entrada do usuário, o comando input sempre guardará uma String na variavel

# Você pode testar no console, ao inserir dandos, que mesmo passando números
# o programa armazenará uma string na variavel hoje

nome = input('Qual seu nome: ')
print('Tipo de dado inserido: ', type(nome))
print('Valor digitado: {}'.format(nome))

# Se você precisar receber do usuário um número, e realizar contas com ele, o mesmo
# deverá ser convertido de string para integer

print('\n')
num = input('Insira um número: ')
num = int(num)
print('Tipo de dado inserido: ', type(num))
resultado = num / 2
print('Valor digitado: {:.2f}'.format(resultado))

# O valor pode ser convertido na minha linha do input
num = int(input('Digite um valor: '))
# Porem, este método não é aconcelhavel porque, se tentar converter a string para 
# inteiro na mesma linha do input, caso o usuário digite algum valor que não possa
# ser convertido, o programa retornará uma execessão, sendo assim, mais seguro, 
# se convertermos em outra linha. Neste caso, o programa também retornará um erro,
# mas este, pode ser tratado para que não quebre o programa.

print('\n')
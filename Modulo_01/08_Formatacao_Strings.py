print('\n')

# Metodo de formatação usando o f antes da String

altura = 1.63
peso = 57

imc = peso / (altura * altura)

# Podemos observar que o f, antes da String, define ela para ser formatada, 
# Dentro de colchetes inserimos o nome da varaivel que desejamos visualizar naquele
# local
# Usar o código :.2f formata o número float para visualizarmos só duas casas
# decimais, o número 2 define quantas casas decimais será mostrada
print(f'IMC: {imc:.2f}')


# Metodo de formatação usando o format

# Neste método, dentro do colchetes passamos o valor a ser formatado, o comando
# .format após o fechamento das aspas passando o nome da ou das variaveis como
# argumento da funcao
print('IMC: {:.2f}'.format(imc))

# abaixo vemos que podemos passar varias variaveis
print('\nAltura: {}\nPeso: {}\nIMC: {:.2f}'.format(altura, peso, imc))

# a ordem das variaveis passadas como argumento na função format será a mesma ordem
# dos colchetes, estes, podem ser nomeados conforme exeplo abaixo

# print('\nAltura: {altura}\nPeso: {peso}\nIMC: {calculo_icm:.2f}'.format(calculo_imc = imc, peso = peso, altura = altura)')

print('\n')
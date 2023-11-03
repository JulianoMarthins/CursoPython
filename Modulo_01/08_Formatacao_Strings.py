"""
    Formatação básica de string

    %s  -> string
    %d  -> int
    %f  -> float

    .<número de dígitos>f

    x ou X -> Hexadecimal

    (Caractere) (><^) (quantidade)

    >   -> Esquerda
    <   -> Direita
    ^   -> Centro
    
    Sinal de +- ou -

    Exemplo:   0> 100, .1f
"""
print('\n')


# A variavel nome é substituída pela %s no frase, precisa ter o % antes da variavel passada como argumento
nome = 'Poa'
print('Meu nome é %s' % nome) 

# imprime um total de dez caracteres, se a varivel nome tiver 5 caracteres, a impressão preencherará os outros 5 
# espaços com o caracter passado entre os : e >, o simbolo > faz com que sejá preenchido do lado esquerdo, lado
# maior da boca do 
print(f'{nome:#>10}') # O caracter > deixa os hastag a esquerda

print(f'{nome:#^10}') # O caracter ^ centraliza o valor nas hastags

print(f'{nome:#<10}') # O caracter < deixa as hastags a direta

# Codigo abaixo mostra o uso da formatação de números float, o número dois define quantas casa decimais será impresa, 
# esta quantidade é a critério da necessidade do programador
num = 2.6548
print(f'Valor com duas casas deciamis: {num:.2f}')

# Sinal de mais mostra se o número é positivo ou negativo.... Mesmo passando o sinal positivo, aparecerá o número 
# negativo se este for o valor original dele
print(f'Valor fomatado positivamente: {num:+,.2f}')
num2 = -321
print(f'Valor negativo com formatação: {num2:+,.2f}')

# Porem, originalmente, se o número for negativo, será mostrado como tal mesmo sem a formatação
print(f'Valor negativo sem formatação: {num2:.2f}')


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
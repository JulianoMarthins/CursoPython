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

print('\n')
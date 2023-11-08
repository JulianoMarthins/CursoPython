"""
    Conversão de tipos primitivos, também são chamados de coreção, type convertion, typecasting, coercion

    Este é o ato de converter um tipo primitivo para outro tipo primitivo
"""
print('\n')

# O uso do sinal de + para números inteiros tem comportamento do uso do mesmo sinal para strings
print(1 + 4) # Retorna 5
print('1' + '4') # Retorna 14

nome = 'Juliano'
print(nome)

nome = int(321)
print(nome)

"""
        Você só pode converter um tipo primitivo para outro tipo primitivo que aceite o valor que está sendo tentando 
    converter.
        Por exemplo, não podemos converter uma string 'teste' para um valor int, float ou bool, mas a string '321' pode 
    ser convertida para números inteiros e ou float
        Conversão de números inteiros para float, será acrescentando uma casa decimal zerada, por exemplo, ao converter
    um número inteiro 15 para float, retornará 15.0

        Porem precisa ter atenção na conversão de float para int onde, caso seja convertido o valor 19.9 para inteiro, 
    ele receberá o valor 19. Conforme podemos ver abaixo

"""

print(int(19.8)) # conversão de um valor float para inteiro
print(float(19)) # conversão de um valor inteiro para float

# Uma String que contem números como caracter pode ser convertida para inteiro ou float, vice e versa tbm é aceito pela lingaugem
print(str(251)) # converte um número inteior para string
print(int('159')) # converte uma string para número inteiro
print(float('778')) # converte uma string para um número float

# caso tente converter um valor string de texto para números o compilador será interrompido e finalizara o programa com um erro

print('\n')
"""
        Utilizando asterisco antes do nome do argumento que a função receberá, o mesmo pode
    receber, naquela varaivel, um número indefinido de valores, sendo criado uma tupa de 
    valores, o que deve ser tratado como tal para percorrer todos os lementos utilizando
    um for conforme exemplo abaixo

        É importante resaltar que, caso precise pasar um argumento simples e depois um argumento
    multiplo usando o *, o argumento simples deve obrigatóriamente vir primeiro pois, caso 
    contrário, todos os elementos que você adicinoar no parametro da função ira para a lista
    de argumentos definidas pelo *


    
"""



def somar(*args): # Recebe um número indefinido de valores
    soma = 0
    for numeros in args: # Percorre todos os elementos passados no argumento
        soma += numeros

    return soma


print(somar(2, 4, 6, 4, 7, 9, 0))


"""
            kwargs -> Parametros nomeados


"""


def preco_final(preco, **kwargs):
    print(kwargs) # Apenas demonstração, kwargs retorna um dicionario
    if 'desconto' in kwargs:
        preco *= (1 - kwargs['desconto'])
    if 'garantia_extra' in kwargs:
        preco += kwargs['garantia_extra']
    if 'imposto' in kwargs:
        preco *= (1 + kwargs['imposto'])
    
    return preco


valor = preco_final(1000) # O argumento preço é obrigatório, porem, os argumentos nomeados não, retorno: 1000

valor = preco_final(1000, desconto=0.1) # Passando um argumento posicional, retorno: 900

valor = preco_final(1000, desconto=0.1, imposto=0.20) # Passando dois arugmentos posicionais, retorno: 1080,00
print(valor)

"""
                            Lambdas expression

        As lambdas expressions são funções anônimas que tem uma linha de códigos
    e são atribuidas a uma variável, como se a variável virasse uma função.
        Elas normalemente são usadas para fazer uma única ação, mas em Python
    usamos principalmente dentro de métodos como arugmento, para não precisarmos
    criar uma função só para isso.
        Outra aplicação delas está em criar um gerador de funções

        Obs: O uso das lambdas expressions não são obrigatória, usamos a mesma
    filosofia utilizadas nas list comprehensions, onde o seu uso não é obrigatório
    porém facilita a vida do programador a sua utilização, e, mesmo que não seja
    utilizada, é de suma importancia saber ler o que está acontecendo em suas linhas
    de códigos
     
"""
print()



# Abaixo criamos uma função que multiplica o valor passado como argumento por dois.

def minha_funcao(args):
    return args * 2

print('Resultado da função: {}'.format(minha_funcao(5)))

print()

# Podemos fazer o mesmo código acima, em expressão lambda, conforme vêmos abaixo

# A variavel resultado recebe o resultado da exmpressão lambda, o parâmetro é 
# denominado como num, ':' significa que apartir dele, será feito a função, que
# no caso de nosso exemplo, é o num * 2

resultado = lambda num: num * 2
print('Resultado utilizando a expressão lambda: {}'.format(resultado(5)))


print()
# Um exemplo de utilidade é calcular 


icms = 1.3
imposto = lambda num: num * icms

print(f'Produto com imposto: R$ {imposto(100):.2f}')
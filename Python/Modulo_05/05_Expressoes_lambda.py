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


# A grande utilidade das expressões lambdas é passar ela como argumento para alguma
# função map ou filter.


print()

preco_tecnologia = {
    'notebook assus': 2450,
    'iphone': 4500,
    'samsung galaxy': 3000,
    'tv samsung': 1000,
    'playstation 5': 3000,
    'tablet': 1000,
    'notebook dell': 3000,
    'ipad': 3000,
    'tv philco': 800,
    'notebook hp': 1700
}

# Map -> Percorre todo o dicinoário e executa alguma ação em cada elemento do
# iteravel

# Relembrando, no dicionario tu retorna todos os items do dicionario em tuplas com
# o metodo .items(), se usar o .keys() você retorna todas as chaves e se usar o 
# metodo .values() você retorna todos os valores do dicionario

def calculo_preco(args):
    return args * 1.3

preco_com_imposto = list(map(calculo_preco, preco_tecnologia.values()))

print('Preço sem expressão lambda: R$ {}'.format(preco_com_imposto))

print()

# Explicação do código abaixo, os parâmetros passador para o map são:

# lambda -> Indica que será realizado uma expressão lambda a seguir

# preco: -> Variavel criada para ser utilizada na expressão lambda

# preco * icms -> Função passada para realização de algum calculo, no caso do 
# código abaixo, foi realizado um calculo simples diretamente no local que seria
# Reservado ao uso da função

# preco_tecnologia.values() -> Pega o valor do dicionario para ser usado nos
# calculos da função lambda.

preco_imposto = list(map(lambda preco: preco * icms, preco_tecnologia.values()))

print('Preço com expressão lambda: R$ {}'.format(preco_imposto))


print()
# Uso do filter -> O proprio nome já ele, esta função filtrará elementos da lista
# durante o uso das expressões lambda

# Abaixo filtraremos todos os valores acima de 2000

# Código abaixo estamos criando uma expressão lambda com a variavel local item, nela,
# acessoamos o indice 1, quer seria os valores contidos no dicionario, testamos uma
# condição, se o valor contido em item[1] for maior que 2000, ele armazenara o valor
# da chave e do valor na variavemo preco_maior, preco_tecnologia.items() é o arugmento
#  a ser analizado pela função filter.
preco_maior = dict(list(filter(lambda item: item[1] > 2000, preco_tecnologia.items())))

print('Itens acima de 2000: {}'.format(preco_maior))


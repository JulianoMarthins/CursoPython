"""
        List comprehensions nada mais é do que torar o código mais 'pytesco' por assim se dizer 
    já que, o objetivo da linguagem quando criada era de ser o mais parecida possivel com a forma
    que nós humanos falamos.


"""
print()


lista_precos = [100, 150, 300, 5500]
preco_impostos = []

# Acrescentar 30% de imposto para cada produto da lista acima
for preco in lista_precos:
    preco_impostos.append(preco * 0.30)

print('Uso do For: {}'.format(preco_impostos))

# Abaixo repetiremos o mesmo código com a utilização do list comprehensions

impostos = [preco * 0.3 for preco in lista_precos]

print('List Comprehensions: {}'.format(impostos))
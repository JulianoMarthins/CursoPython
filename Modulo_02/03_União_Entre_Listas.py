"""



"""

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

# Ao criar uma terceira lista, podemos definir os valores de outras listas
# concatenando-as
lista_c = lista_a + lista_b
print(lista_c)

# O comando abaixo não retorna nenhum valor, porem, ela copia os valores da lista 
# passada como argumento
lista_a.extend(lista_b)
print(lista_a)

# Podemos observar que o método aceita elementos repetidos extenção da lista
lista_a.extend(lista_c)
print(lista_a)

print()


lista = [('juliano', 321, 14), ('thieles', 65748, 31)]


for indice in lista:
    cpf, x, y = indice
    
    if x > 300:
        print(cpf)

print(type(lista))
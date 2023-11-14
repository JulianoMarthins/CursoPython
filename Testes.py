print()

valores = [10, 30, 90, 7, 42, 71]

maximo = max(valores)
menor = min(valores)


indice_maior = valores.index(max(valores))
indice_menor = valores.index(min(valores))

print('Maior elemento da lista: {}'.format(maximo))
print('Menor elemento da lista: {}'.format(menor))

print('Indice do maior elemento: {}'.format(indice_maior))
print('Indice do menor elemento: {}'.format(indice_menor))

print()
for indice, valor in enumerate(valores):
    print(f'{indice}: {valor}')

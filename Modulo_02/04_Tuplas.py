"""
                                Intrudução a tuplas

        Se falarmos em metódos e teorias de uso, tudo o que aprendemos nas aulas ateriores sobre listas se aplica em
    tupla.
        A grande diferença é que, em tuplas, uma vez que definida, não pode ser alterada os valores já adicionados
    a ela.
        Você pode adicionar ou remover valores, mas jamais alteralos

"""
print()

# Lista se cria passando os valores dentro de colchetes
nomes = ['Maria', 'Helena','Luiz']
print(f'Lista de nomes: {type(nomes)}')

# Conversão de uma lista para uma tupla
nomes = tuple(nomes)
print(f'Conversão da lista para uma tupla: {type(nomes)}')
print(f'Acessando último elemento da tupla: {nomes[-1]}')
print(f'Valores da tupla: {nomes}')
      
print()
"""
                                Intrudução a tuplas

        As tuplas e as listas são muito parecidas em sua estrutura base, literalmente
    é uma variável composta como as listas porem, como grande diferencial, as tuplas
    são imutáveis, isso é, uma vez definido os valores dela, eles não poderão ser 
    substituídos, deletados ou adicionar novos elementos a ela, o que, este, é visto
    como uma vantagem sobre as listas pois, uma vez sendo imutável, a mesma protege
    seus valores.

        Outra vantagem é que a tupla se torna mais simples de ser processada, deixando
    assim nosso programa mais rápido  

"""

print('\n')

# Lista se cria passando os valores dentro de colchetes
nomes = ['Maria', 'Helena','Luiz']
print(f'Lista de nomes: {type(nomes)}')

# Conversão de uma lista para uma tupla
nomes = tuple(nomes)
print(f'Conversão da lista para uma tupla: {type(nomes)}')
print(f'Acessando último elemento da tupla: {nomes[-1]}')
print(f'Valores da tupla: {nomes}')

print('\n')
vendas = ('Juliano', '25/05/2008', '04/06/1982', 2000, 'Estagiário')

print('Nome: {}'.format(vendas[0]))
print('Admissão: {}'.format(vendas[1]))
print('Nascimento: {}'.format(vendas[2]))
print(f'Salário: {vendas[3]}')
print(f'Cargo: {vendas[4]}')

print('\n')

valor = [1000, 2000, 300, 300, 150]
funcionarios = ['João', 'Juliano', 'Ana', 'Maria', 'Paula']

for i, venda in enumerate(valor):
    print('{} vendeu {} unidades'.format(funcionarios[i], venda))

# Podemos realizar unpacking para desmembrar cada valor das tuplas, exatamente
# como feito nas listas

nome, admissao, data_nascimento, salario, cargo = vendas
print(f'\nNome: {nome}')
print(f'Contratação: {admissao}')
print(f'Nascimento: {data_nascimento}')
print(f'Salário: {salario}')
print(f'Cargo: {cargo}')




print('\n')
print()

"""
        Introdução ao desenpacotamento com tuplas
        
        Em python, pode ser passado mais de uma variavel para receber mais de um valor por linha, este receberá os valores
    como se fosse por indices.

"""
# A variavel nome recebe uma lista de nomes
nome = ['Juliano', 'Gabriel', 'Michele']
print(f'Nome 01: {nome}')

# As variaveis nome2, nome3 e nome4, vão receber, cada uma um dos nomes da lista abaixo, respeitando a ordem da escrita
# nome2 recebe Olavo, nome3 recebe Eduardo, nome4 recebe Fernanda

nome2, nome3, nome4 = ['Olavo', 'Eduardo', 'Fernanda']
print(f'\nNome 2: {nome2}\nNome 3: {nome3}\nNome 4: {nome4} ')


# O número de variaveis deve ser, obivmante, a mesma quantidade do número de valores da lista, caso tenha a mais, ou a menos, 
# o programa retornará um erro

# Você pode passar um número x de variaveis inicial, e adicionar uma variavel com o sinbolo * antes de seu nome, este, fará
# com que recebá todas os outros valores da lista

# Exemplo, nome5 recebe o nome Maria, já a variavel resto, receberá o resto de valores contidos na lsita, neste caso, Helena e Luiz
nome5, *resto = ['Maria', 'Helena', 'Luiz']
print(f'\nNome 5: {nome5}\nResto da lista: {resto}')

# Caso você não utilizar a variavel resto em nenhuma parte do programa, a convenção adotada em Python é nomear a varaive com '_'
filme, *_ = ['Bastardos inglorius', 'Era uma vez em Hollywood', 'Jango Livre']
print(f'Filme: {filme}')
print()
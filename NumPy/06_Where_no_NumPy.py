"""
                        Filtros e np.where()

        A função np.where() é muito útil para fazer uma seleção condicional de
    elementos de um array. Por exemplo, em uma empresa, você póde querer identificar
    quais funcionários têm salários acima da média.

"""

import numpy as np

print()

# Salário dos funcionários
salarios = np.array([3000, 3500, 4000, 2000, 4500, 4000, 5000])

# Calcular a média salarial
media_salarial = np.mean(salarios)

print('Média salarial: R$ {:.2f}'.format(media_salarial))

# Na linha de código abaixo, utilizamos o where para realizar um filtro no array
# de salario onde, todos que forem maiores que a media salaria, irá ser armazenado
# na variavel funcinoarios_acima_media.

# É importante resaltar que este retorno será apenas dos indices dos salarios acima
# da média, e não os valores em si
funcionarios_acima_media = np.where(salarios > media_salarial)

# Para acessar o valor de um array, fazemos isso colocando entre colchetes o indice
# do valor desejado, porem, em array, podemos passar outro array de valores.
# Assim, passando a variavel funcionarios_acima_media como indice para salarios,
#  retornaremos os valores de todos os salarios acima da média 
valores = salarios[funcionarios_acima_media]
print('Funcionários acima da média: {}'.format(valores))

# A condição utilizada acima é considerada simples e casos similares, não há
# a necessidade da utilização do where, a condição passada no argumento do where
# pode ser passada diretamente no argumento dos indices do array

acima_media = salarios[salarios > media_salarial]

print(f'\nAcima da média, utlização da condicional como argumento diretamente \n\
no argumento do array: {acima_media}')

# A função where possui muito mais vantagens e modos diferenciados para a sua
# utilização, no caso do estudo acima, caso você precise a pocição é indispensavel
# o uso do where porém, caso você precise dos valores, pode passar a condição
# diretamente como indice do array

# Mais exemplos do uso de condicional como parametro de indices de um array

print('\nSalários acima de 4.000,00: {}'.format(salarios[salarios > 4000]))


# Mas então porque utilizariamos o where? No caso abaixo, podemos perceber o uso 
# do where, com a mesma lógica do if e do else, onde, caso o salario do funcionar
# seja acima da média, será retornado a mensagem "acima da média", caso contrário
# sera retornado a mensagem "abaixo da média"

print('\nUso do where para condicionais que analisam o verdadeiro e o falso:\n\
{}'.format(np.where(salarios > media_salarial, 'Acima da média', "Abaixo da média")))


# Digamos que você precise aumentar em 10% o salário de todos os funcionários de
# sua empresa que ganhe abaixo da média da empresa, podemos resolver isso facilmente
# com a utlização do where
print('\nSalários atuais: {}'.format(salarios))

salarios = np.where(salarios < media_salarial, salarios * 1.1, salarios)

print('Salários atualizado dos funcionários: {}'.format(salarios))
media_salarial = np.mean(salarios)
print(f'Nova média salárial: R$ {media_salarial:.2f}')

# Digamos que eu precise retornar os salarios entre 3000 e 4500 mil reais mensais,
# este exemplo é para mostrar que, na biblioteca NumPy, para realizar condicionais
# que utilizem o operador 'E', deve ser utilziado o caracter '&', este, padrão para
# esta operação em muitas liguagens, é utilizada no numpy pois existe a necessidade
# de separar claramente o operador 'and' do python para o operador '&' do NumPy

faixa = np.where((salarios >= 3000) & (salarios <= 4500))
print('\nSalários em uma faixa específica: {}'.format(salarios[faixa]))

# Digamos que agora, precisamos aumentar o salários dos funcionários que estão
# na faixa salárial descrita acima.
salarios = np.where((salarios >= 3000) & (salarios <=4500), salarios * 1.05, salarios)

print('\nAtualização de salárial: {}'.format(salarios))
media_salarial = np.mean(salarios)
print('Média salárial atualizada: {:.2f}'.format(media_salarial))


# Acima estudamos sobre a alteração do operador e de "and" para "&", porém, se houve
# alteração neste operador, o operador ou, representado pelo "or", também será
# alterado, na biblioteca NumPy utilizamos o operador "|" para representar ou.

salarios = np.where((salarios < 3000) | (salarios > 4500), salarios * 1.1, salarios)
print('\nSalários fora da média salarial: {}'.format(salarios))
media_salarial = np.mean(salarios)

print(f'Média salárial: R$ {media_salarial:.2f}')

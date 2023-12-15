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
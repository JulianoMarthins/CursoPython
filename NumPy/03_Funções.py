"""
            Aplicações do dia a dia com NumPy

"""
import numpy as np

# Digamos que precisamos aumentar o preço de todos os produtos de um array.

print()
preco = np.array([200, 250, 300, 350, 400])
imposto = 1.1
novos_precos = preco * imposto

print('Preços dos produtos R$ {}'.format(preco))
print('Preços atualizados com impostos: R$ {}'.format(novos_precos))

print()
# Para somar todos os elementos de um array podemos usar a função .sum(). Podemos observar que
# existe nativamente o método sum() em python porem, é sempre recomendando que, se estamos usando
# a biblioteca NumPy, usarmos os métodos do NumPy, obviamente ambos métodos farão a soma dos
# elementos porém, como já foi mencionado aqui antes, as funções do NumPy são mais otmizadas
# e respondem melhor e mais agilmente com grandes volumes de dados.

soma = np.sum(novos_precos)
print('Soma de todos os produtos do Array: R$ {:.2f}'.format(soma))


# A funçãço .mean() serve para calcualr a média dos valores contidos no array
print()
media = np.mean(novos_precos)

print('Média dos valores: R$ {:.2f}'.format(media))


# Temos as funções .max() e .min() para retornar o maior e menor elementos da array
maior = np.max(novos_precos)
menor = np.min(novos_precos)

print('\nMaior valor: R$ {:.2f}'.format(maior))
print('Menor valor: R$ {:.2f}'.format(menor))


# A função .sort() ordenará a array

array_ordenada = np.sort(novos_precos)
print('\nArrayList ordenada: {}'.format(array_ordenada))

# A função .dot() faz um calculo unindo duas arrays diferentes, por exemplo, no código abaixo nós
# teremos duas arrays, uma da quantidade dos produtos e a outra dos preços, ao final, calcularemos
# o valor total das vendas

quantidade = np.array([10, 20, 30, 40])
preco_unitario = np.array([5, 10, 15, 20])

preco_total_por_produto = np.dot(quantidade, preco_unitario)

print('\nValor total de vendas: R$ {:.2f}'.format(preco_total_por_produto))


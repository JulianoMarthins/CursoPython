"""
                            Guia de introdução ao NumPy
        NumPy, que significa Numerical Python, é uma biblioteca fundamental para 
    a computação científica em Python. Ela fornece suporte para arrays e matrizes,
    além de funções matemáticas para operações com esses objetos. É também, a base 
    da biblioteca Pandas.
"""

# Números aleatórios e estatísticas básicas

import numpy as np

print()

# O código abaixo estamos criando uma variavel para gerador números aleatórios
rng = np.random.default_rng()

# Abaixo, a variavel num_aleatorio recebe uma randomização númerica
num_aleatorio = rng.random()

print('Número aleatório gerado: {}'.format(num_aleatorio))

# Podemos passar como arugmento um número que será a quantidade de números aleatórios
# que o gerador gerará, estes valores podem ser multiplicados se assim necessário
# com o código <rng.random(3) * 10>
array_aleatorio = rng.random(3)

print('\nArray aleatória com três valores: {}'.format(array_aleatorio))


"""
        Vamos criar um cenário onde esses dados aleatórios podem ser úteis para
    análise de vendas.

        Suponha que voocê seja um analista de vendas em uma empresa e queira entender
    melhor o desempenho das vendas de um produto específico. No entando, você não tem
    acesso aos dados reais de vendas, então você decide gerar alguns dados de vendas
    aleatórios para realziar sua análise

"""
print()

# O parametro passado na linha abaixo, seed=0, significa que o rng irá gerar uma
# sequencia de números uma única vez, mesmo que você rode o programa novamente, 
# ele se manterá igual para facilitar o analise de dados por você e outros membros
# de sua equipe.
rng = np.random.default_rng(seed=42)

dados_vendas = rng.integers(low=50, high=200, size=30)

print(dados_vendas)

print()
# Agora que temos esses dados, podemos fazer qualquer análise que desejarmos.
# Por exemplo, você pode querer saber qual foi o dia com as vendas mais alta, as
# vendas mais baixas, ou a média de vendas durante todo o mês. Aqui está como você
# pode fazer isso


# Dia com as vendas mais altas

# A função .argmax retorna o indice do maior elemento encontrado
melhor_dia = np.argmax(dados_vendas + 1)
maior_vendas = np.max(dados_vendas + 1)

print(f'\nMaior venda foi no {melhor_dia}° dia: R$ {maior_vendas:.2f}')


# De mesma lógica, a função .argmin retorna o indice do menor elemento encontrado
# Dias com as vendas mais baixas

pior_dia = np.argmin(dados_vendas)
menor_venda = np.min(dados_vendas)

print(f'Menor venda foi no {pior_dia}° dia: R$ {menor_venda:.2f}')


# Média de vendas durante o mês
media_vendas = np.mean(dados_vendas)
print(f'Média de vendas mensal: R$ {media_vendas:.2f}')

# Calcula a mediana das vendas mensais
print('Mediana: {:.2f}'.format(np.median(dados_vendas)))

# Calcula percenti, passando também a porcentagem a ser dividida
print('Percenti: {:.2f}'.format(np.percentile(dados_vendas, 50)))

# Calcula o desvio padrão
print(f'Desvio: {np.std(dados_vendas):.2f}')

# calcula a variância
print('Variância: {:.2f}'.format(np.var(dados_vendas)))


"""
        Breve resumo e conceitos simplificados das funções de estatisticas acima
    citadas.

        1. Mediana -> A mediana é um valor que divide um conjunto de dados em duas
    partes iguais. Para encontra-la, você deve organizar os dados em ordem crescente
    ou decrescente e escolher o valor do meio. Se houver um número ímpar de dados, a
    mediana será exatamente o valor central. Se houver um número par de dados, a
    medina será a média dos dois valores do meio.

        2. Percentil -> O percentil é uma medida estatística que indinca a posição
    Relativa de um dado dentro de um conjunto de dados. Ele informa a porcentagem de
    valores que estão abaixo desse dado. Por exemplo, o percecntil de 50, (também
    conhecida como mediana) divide os dados em duas partes iguais, com 50% dos valores
    abaixo dele e 50% por cento acima dele.

        3. Desvio padrão -> O desvio padrão é uma medida que indica o quão dispersos
    os valores de um conjunto de dados estão em relação a média. Ele mostra a 
    variabilidade dos dados em relação ao valor médio. Um desvio padrão maior indica
    que os dados estão mais espalhados, enquanto um desvio padrão menor indica que
    os dados estão mais proximos da média

        4. Variância -> A variância é outra medida de dispersão que indica o quão
    distantes os valores de um conjunto de dados estão da média. Ela é calculada como
    a média dos quadrados das diferenças entre cada valor e a média. A variância
    fornece uma medida da dispersão total dos dados, independentemente de serem
    maiores ou menores que a média.

        Essas medidas são amplamente utilizadas na estatístca para resumir e analisar 
    conjuntos de dados. Elas fornecem informações valiosas sobre a distribuição, a
    visibilidade e a posição dos dados, permitindo uma compreensão mais completa dos
    mesmos.
    
"""
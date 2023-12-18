"""
        Considere que uma loja funciona de segunda a sábado, independentemente de
    feriados. Nos últimos 30 dias, teve o menor volume de vendas sendo 20 e o maior
    sendo 200. Crie uma simulação das vendas desses últimos 30 dias, separando por
    semanas. 

    Calcule: 

    1. Total de vendas por semana
    2. Média de vendas por semana
    3. Média de vendas por dia da semana


    Pelo enunciado, o padrão de dias é :

    seg, ter, qua, qui, sex, sab, seg, ter, qua, qui, sex, sab ....

"""
import numpy as np

print()

# Código abaixo criamos um gerador default, seed é um argumento passado para realizar
# fixação do números gerados, assim, estes, não serão alterados a cada vez que formos
# rodar o código
rng = np.random.default_rng(seed=42)

# Abaixo, criamos um gerador de números inteiros, sendo o valor minimo 20, e o máximo
# 200, o tamanho, esta recebendo diretamente uma matriz 5 x 6, deixando assim, sem
# a necessidade de convertermos a variável vendas futuramente com a função reshape
# O parâmetro endpoint, serve para tronar o maior elemento, analisado pela lista.
vendas = rng.integers(low=20, high=200, size=(5, 6), endpoint=True)

total_vendas_semanais = vendas.sum(axis=1)
media_vendas_semanais = vendas.mean(axis=1)
media_vendas_dia = vendas.mean(axis=0)

print(f'Vendas Semanais: \n{total_vendas_semanais}')
print(f'\nMédia Semanal: \n{media_vendas_semanais}')
print(f'\nMédia Diária: \n{media_vendas_dia}')


"""
    Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito,
    exiba a saudação com bom dia, boa tarde ou boa noite

    # Bom dia   =>  8 às 11
    # Boa tarde =>  12 às 17
    # Boa noite =>  18 às 23
    # Bons sonhoes  =>  00 às 7

"""
from typing import Any

print('\n')

hora = input('Digite a hora: ')

if 8 <= hora <= 11:
    print('Bom dia')
elif 12 <= hora <= 17:
    print('Boa tarde')
elif 18 <= hora <= 23:
    print('Boa noite')
else:
    print('Dormindo')

print('\n')


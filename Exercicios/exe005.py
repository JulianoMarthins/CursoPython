"""
    Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito,
    exiba a saudação com bom dia, boa tarde ou boa noite

    # Bom dia   =>  8 às 11
    # Boa tarde =>  12 às 17
    # Boa noite =>  18 às 23
    # Bons sonhoes  =>  00 às 7

"""
print('\n')

hora = input('Digite a hora: ')

hora = int(hora)

if hora >= 8 and hora <= 11:
    print('Bom dia')
elif hora >= 12 and hora <= 17:
    print('Boa tarde')
elif hora >= 18 and hora <= 23:
    print('Boa noite')
else:
    print('Dormindo')

print('\n')


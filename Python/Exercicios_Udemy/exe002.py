"""
    Crie um programa que calcule o IMC (índice de massa corporal)
"""
print('\n')

altura = float(input('Altura: '))
peso = float(input('Peso: '))
imc = peso / (altura * altura)

print(f'IMC: {imc:.2f}')

print('\n')

"""
                Imprecisão de ponto flutuante

        Linguagens de promgração utilizam contas apróximadas para agilizarem o 
    processamento do programa, existe módulos que tiram essa impressição 


        Função round

"""
print('\n')


import decimal

num = 0.1
num2 = 0.7

resultado = num + num2

print(f'Resultado: {resultado}') # Retorno 7.999999...

print(f'Resultado: {resultado:.2f}') # Retorno 8.00

print(f'Resultado: {round(resultado, 2)}') # Retorno 8.00


num3 = decimal.Decimal('0.1') # Os números devem ser passados como String
num4 = decimal.Decimal('0.7') # Este método calcular 100% corretamente

print(num3 + num4) # Retorno 8.0



print('\n')
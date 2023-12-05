import matplotlib.pylab as plt

# Recebe uma string como argumento, trata a mesma removendo o cifrão monetário, pontos e virgula
# Retorna a string tratada convertida para float
def converter_para_float(args):
    valor = args.replace('R$ ', '').replace('.', '').replace(',', '.')
    valor = float(valor)
    return valor


# Recebe um valor float como argumento
# Retorna o valor de impostos mensais a serem pagos em float
def imposto_mensal(args):
    imposto_iss = 0.05
    imposto_pis = 0.065
    imposto_confins = 0.03
    
    impostos = imposto_iss + imposto_pis + imposto_confins
    taxa = args * impostos

    return taxa


# Recebe um valor float como argumento
# Analisa o argumento e adiciona imposto extra caso este ultrapasso R$ 20.000,00
# Retorna os impostos trimestrais a serem pagos
def imposto_trimestral(args):
    imposto_ir = 0.048
    imposto_ir_maior_20k = 0.10
    imposto_csll = -.0288

    if args > 20000.00:
        impostos = imposto_csll + imposto_ir + imposto_ir_maior_20k
        return args * impostos
    else: 
        impostos = imposto_csll + imposto_ir
        return args * impostos

print()    


# Dicionário com o faturamento mensal a ser analisado
faturamento = {
    'jan': 'R$ 95.141,98',
    'fev': 'R$ 95.425,16',
    'mar': 'R$ 89.716,31',
    'abr': 'R$ 78.459,99',
    'mai': 'R$ 71.087,28',
    'jun': 'R$ 83.911,06',
    'jul': 'R$ 56.467,26',
    'ago': 'R$ 88.513,58',
    'set': 'R$ 66.552,49',
    'out': 'R$ 80.164,07',
    'nov': 'R$ 66.964,33',
    'dez': 'R$ 71.525,25',
}

# Criação de listas auxiliares
lista_chaves = []
lista_faturamento = []
lista_imp_mensal = []
lista_imp_trimestral = []


for mes in faturamento:
    valor = converter_para_float(faturamento[mes])
    
    # Condição para analise de imposto trimestral, com acrescimo dos impostos mensais desses meses.
    if 'mar' in mes or 'jun' in mes or 'set' in mes or 'dez' in mes:
       
        lista_chaves.append(mes)
        lista_faturamento.append(valor)
        lista_imp_mensal.append(imposto_mensal(valor))
        lista_imp_trimestral.append(imposto_trimestral(valor))

    # Tratamento de impostos mensais       
    else:
        lista_chaves.append(mes)
        lista_faturamento.append(valor)
        lista_imp_mensal.append(imposto_mensal(valor))
        lista_imp_trimestral.append(None)


# Criação de dicionário com os valores de impostos inclusos
faturamento_impostos = dict.fromkeys(
    lista_chaves, (lista_faturamento, lista_imp_mensal, lista_imp_trimestral)
    )

print('Tabela de impostos:')

cont = 0

# List auxiliar para utilização nos graficos
grafico_faturamento = []

for chave in faturamento_impostos:
    print()
    print('-' * 40)
    print()
    
    meses = faturamento_impostos.keys()
    vendas, mensal, trimestral = faturamento_impostos[chave]
    
    vendas = float(vendas[cont])
    mensal = float(mensal[cont])

    try:
        trimestral = float(trimestral[cont])
    except:
        trimestral = float(0)
    cont += 1
    
    chave = str(chave)

    print(f'Faturamento no mês de {chave.title()}')
    print()

    print(f'Vendas: R$ {vendas:.2f}')
    print(f'Imposto mensal: R$ {mensal:.2f}')
    print(f'Imposto trimestral: R$ {trimestral:.2f}')

    faturamento_mensal = (vendas - (mensal + trimestral))

    print()
    print(f'Total de impostos a pagar: R$ {mensal + trimestral:.2f}')
    print(f'Faturamento mensal: R$ {faturamento_mensal:.2f}')

    grafico_faturamento.append(faturamento_mensal)


plt.plot(lista_chaves, grafico_faturamento, color='green')

plt.show()

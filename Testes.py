print()

dicionario = {
    'nome': 'Juliano',
    'cpf': '01164336045'
}

for chave, valor in dicionario.items():
    print('{}: {}'.format(chave, valor))

dicionario['nome'] = 'Thiele'


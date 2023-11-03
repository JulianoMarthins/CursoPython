"""
    Exercício:

    Usuário deve digitar seu nome
    

    Se nome e idade forem digitados:
        Exiba no console
        * Nome do usuário
        * Nome invertido
        * Número de caracteres com espaços
        * Número de caracteres sem espaços
        * Primeira letra do nome
        * Última letra do nome
    
    Se nada for digitado:
        Exiba uma mensagem sobre não poder deixar campos vazios
"""
print('\n')

nome = input('Insira se nome: ') or 'Você não digitou seu nome'

if nome: 
    print('Nome: ', nome)
    print('Nome invertido: ', nome[::-1])
    print('Quantide de caracteres com espaços: ', len(nome))
    nome_sem_espaços = nome.replace(' ', '')
    print('Quantidade de caracteres sem espaços: ', len(nome_sem_espaços) )
    print('Primeira letra do seu nome: ', nome[0])
    print('Última letra do seu nome: ', nome[1])

else:
    print('Não pode deixar este campo vazio')

print('\n')

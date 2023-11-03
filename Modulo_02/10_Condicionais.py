"""
    Constantemente em um programa de computação existe a necessidade de desviarmos
    o caminho, realizar checagens, isso se faz com a palavra chave, if, elif e else

    if -> se
    else -> se não
    elif -> se não, se

    O bloco de código do if só será exacutado se a condição for verdadeira
    O bloco de código do else só será executada se a condição do if for falsa
    O bloco de código do elif será executado se sua consição for verdadeira, porem
    se a condição do primeiro if for falsa.

    Um bloco condicional é sempre iniciado pelo if, finalizado pelo else, você pode crirar mais condicionais
    sendo esta chamada de elif, o codigo será checado uma condicao por vez e encerrará todas as checagens 
    quando achar o primeiro True do bloco de código

"""

print('\n')

condicao = False
condicao2 = True
condicao3 = True

if condicao: # Esta condição será falsa
    print('Primeira condição verdadeira') # Para funcionar, o bloco de código deve estar identado.
elif condicao2: # Esta condicação será verdadeira, executara o bloco de código interno e encerarra a checagem
    print('Segunda condicao verdadeira')
elif condicao3: # Compilador pulará esta parte porque a condição dois já verdadeira
    print('Terceira condição verdadeira')
else: # Else só será executado se nenhuma condição acima for verdadeira, else não pode ter condição em seu argumento
    print('Nenhuma condição atendida')



print('\n')
"""
                        Fatiamento de Strings

        Quando se escreve um valor, cada letra digitada é formada por um caracter.
        Juliano possui 7 letras.
        Juliano Martins possui 14 letras, porem, na programação, o espaço entre os dois nomes contam, totalizando 15
    caracters

        O que devemos ter atenção no incio é que em programação, a grande maioria das linguagens de programaçaõ
    iniciam suas contagens no zero, logo, Juliano tem 7 letras porem, na contagem do computador, continuam sendo 7
    valores mas a última letra, a letra o, é representada pelo número 6

    Exemplo

        0   1   2   3   4   5   6  
        J   U   L   I   A   N   O
    -   7   6   5   4   3   2   1

        Veja também que pode ser definido como números negativos

        Temos uma importante função para strings, a len(), está retorna a contagem de valores contidos na String

    Exemplo:
        len('Juliano')  =>  Retornará o valor 6, lembrando novamente, retorna 6 porque a contagem se inicia no 0.

"""

nome = 'Juliano Martins de Souza'

# função len retorna o número de caracteres contido na variavel, contagem incia no 0, e soma espaços vazios
print(f'Total de valores na string => {len(nome)}')

# Pode ser acessado qualquer caracter pelo indice
# Retorna o caracter de número 6, isso porque a contagem se inicia no 0. Neste caso, retorna a letra n
print('Acessando o indice 5 => ', nome[5])

# No código abaixo, o número 8 representa onde o fatiamento ira começar, o 15, até onde vai, neste caso, retornará
# Martins 
print('Acessando os indices do 8 ao 15 => ', nome[8:15])

# Ha um terceiro argumento que pode ser passado, no código abaixo, o 2 representa pulos que o leitor fará na string
# Digamos que ele inicie no caracter 4, termine no carater 22, mas mostrará os caracteres que cairem em uma contagem de dois
# em dois

# Inicia no 4, termina no 22, pula de 2 em 2... Retornando ao usuario "aoMrisd o"
print('Acessando pelo indice, do 4 ao 22, pulando de dois em dois   =>', nome[4:22:2]) 

# Exemplo de acesso a indices por números negativos
# Como a variavel tem 24 caracteres, retornará o primeiro caracter, letra J
print('Acessando o ultimo indice pelo número de caracteres  =>', nome[-24]) 

# Podemos usar o -1 para acessar o ultimo caracters, idependentemente de quanto caracters a variavel tenha,
# ou este valor seja desconhecido

print('Acessando o último indice pelo valor negativo  =>',  nome[-1]) # Retorna a letra "a"

# Caso o programador precise retornar o valor contido da variável de trás pra frente
print('Acessando a variavel de trás pra frente  =>', nome[::-1])

#Fatiamento de trás pra frente
# Código abaixo => -1 (inicia da última letra): -10(até a deciam letra de trás pra frente):
# -1(pula de um em um nos caracteres)
print('Acesso ao fatiamento reverso =>', nome[-1:-10:-1]) 

print('\n')
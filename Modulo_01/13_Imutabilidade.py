"""
        Ao inicializarmos uma variavel, a mesma pode ser alterada posteriormente no código, por exemplo, podemos
    definir uma variavel com a string 'Juliano' e, mais adiante no código, atribuirmos outro valor a mesma variável,
    por exemplo, 'Fernanda'

        Isso pode ser realizado com qualquer tipo de variavel, incluído, alterar seu tipo primitivo, digamos que ao
    inizializar uma variavelo com a str 'Juliano', posteriormente no código podemos alterar a mesma variável para um
    número 52, que se tornaria, devido a linguagem python ser de tipagem dinâmica, um int.

        Obviamente este exemplo é para compreensão, não é recomendável altrar drasticamente os valores das variáveis
    porque o nome da mesma não irá condizir com o valor contido nela, em outras palavras, seria consideráda uma péssima
    pratica de programação a variavel nome guardar um número float por exemplo, variável nome deve guardar um nome.

        Porem, os conteúdos contidos nas variávels são imutáveis, o que isso quer dizer? Uma vez que definirmos a
    variável nome_liguagem, por exemplo, e atribuírmos o valor 'Python' a está variável, não será permitido mudar algum
    valor da string Python acessando seus indicies.


"""
print('\n')

# Inicialização da variavel com o valor em string. Uma string é considerada uma lista de caracteres, apesar do
# professor afirmar isso em aula, e em outras linguagens que estudei como Java, no caso de Python, com o conhecimento
# que tenho hoje ela se encaixaria mais em tuplo pois, apensar de tuplas e listas serem identicos, o conceito em que
# elas mais de diferenciam é justamente a imutabilidade contida nas tuplas.

nome_linguagem = 'Java'
# Mesmo após definir o valor da variável, este pode ser alterado conforme necessidade do programador
nome_linguagem = 'Python'
# Porem, os caracteres desta string não podem ser alterado

# Blobo try não será executado pois lançará uma excessão
try:
    nome_linguagem[3] = 'z' # Este trecho de código tenta alterar a letra 'h' da variavel pela letra 'z'
except:
    print('Valors contidos em variáveis não podem ser alterados')

# Durante a escrita do código acima me surgiu a dúvida de que, apensar da aula ser focada em imutabilidade dos valores
# contídos nas variáveis, a mesma pode ser alterada com o método replace, este disponível somente para Strings

nome = 'Juliano Martins de Souza'
nome = nome.replace('a', '#') # Altera todos os caracteres 'a' encontrados na string por '#'

print(nome)

# Duvida sobre o assunto questionado ao professor, aguardando resposta para atualizar este trecho de conteúdo

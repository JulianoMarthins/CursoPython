"""
        Um dos objetivos do Python e realizar códigos o mais parecido possivel com a fala humana, tornando assim, uma linguagem
    mais simples de ser utilizada.
        Exeste uma técina em python pra nos ajudar a fazer isso acontecer chamada list comprehensions que, torna pequenos trechos 
    do nossos códigos podendo ser escrito em uma única linha o tornando assim mais legível e otimizado.

        O uso no list comprehensions não é obrigatório nem considerado uma boa prática de programação, mas é impostante aos estudantes
    conhecer o uso desta técnica para entender possiveis leituras desta técnica em outros código.

        Observações importantes
            * Você não precisa de list comprehensions para programar, tudo que veremos apartir de agora da para fazer do jeito
        que já aprendemos
            * Você não vai sair de uma hora para outra fazendo tudo em list comprehensions ao invés de for, porque é realmente 
        mais confuso.
            * Você deve saber ler e entender o que tá acontecendo quando ver o código de alguém utilizando o list comprehensions
            * A medida do tempo que você vai se acostumando com isso, vendo mais, usando mais, você acabará útilziando o list
        comprehensions naturalmente, a medida que você for pegando experiência em programação com Python



        O uso de list comprehensions não é recomendando nas seguintes situações

            * Normalmente isso é usado quando queremos fazer uma única coisa com os itens da lista. Não é obrigatório, mas é comum
        de encontrar principalmente com programadores mais experiêntes, que esteja preocupados em fazer seus códigos da melhor
        forma possível.

            * Muito atenção no uso de list comprehensions ao utilizado para percorrer listas muito grandes, isso pode acabar deixando
        o código mais lendo pela dificuldade de compilação. Nesses casos podemos usar funções tradicionais com breaks para interromper
        ou até bibliotecas como o panda que trabalham bem com muitos dados.


"""
print()


lista_precos = [100, 150, 300, 5500]
preco_impostos = []

# Acrescentar 30% de imposto para cada produto da lista acima
for preco in lista_precos:
    preco_impostos.append(preco * 0.30)

print('Uso do For: {:.2f}'.format(preco_impostos))

# Abaixo repetiremos o mesmo código com a utilização do list comprehensions

impostos = [preco * 0.3 for preco in lista_precos]

print('List Comprehensions: {:.2f}'.format(impostos))

# O mesmo código pode também ser passar uma função ao invés do calculo dentro da list comprrehensions

def calculo_imposto(args):
    return args * 0.30

imposto_funcao = [calculo_imposto(x) for x in lista_precos]

print('List Comprehensions usando função: {:.2f}'.format(imposto_funcao))


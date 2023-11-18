"""
        Em uma função, existe dois tipos de possibilidade de execução, com e sem
    retorno. Mas o que exatamente é o retorno?
        Quando uma função não possui retorno, isso significa que ela realiza
    uma tarefa pré definida pelo programador, faz a alteração pela qual foi criada
    e se encerra.
        Retorno é quando esta função retorna ao programador algum valor que foi
    programado dentro da função.

        Por exemplo, uma funçõa que some dois números, o retorno dela é o valor 
    dessa soma.
"""
print()

def somar():
    soma = 5 + 3
    return soma

# Observe que, se chamar a função somar() nada acontece, é preciso guardar o valor
# retornado pela mesma em uma variável para poder usar este valor como desejar
retorno_funcao = somar()
print(retorno_funcao)

# Devemos sempre ter ciencia de que variaveis criadas dentro de funções tem seu uso
# unico e exclusivo aquela função, não sendo possivel acessa-la fora da função, 
# logo, se tentarmos usar a variavel soma em um trecho de código fora da função, 
# o programa lançará uma excessão alegando não existir a variavel com este nome

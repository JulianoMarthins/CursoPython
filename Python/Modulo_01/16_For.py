"""
        A filosofia do for é identica ao while, porem, o uso dele é recomendando 
    quando o programador sabe quantas vezes o laço de repetição será executada, 
    isso ao contrario do while que é recomendado o uso quando não sabemos quantas 
    vezes será repetido.

        O for recebe a condição diretamente nele e só para de funcionar quando 
    retornar falso a esta condição, apesar de na aula passada termos visto o while 
    fazer algo similar, era apenas para exemplo de didádita, o normal do uso do 
    while, não é ser usado daquele jeito pois o mesmo se torna ineficiente.

        As palavras chaves continue e break que aprendemos no while, funciona 
    normalmente, de forma igual, em laços de repetições do for

       

"""
print('\n')

# range realizará a contagem do número 1 ao 10, pois o 11 não será concluído
# num é uma variavel criada para o for, ela recebe os valores da contagem pelo range
for num in range(1, 11): 
    # Retornará ao usuário cada contagem do range, que é guardada na variavel de 
    # scopo local num
    print(num) 

# O retorno do usuário será     {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


# No código abaixo, o primeiro argumento, o número 1, é o valor inicial da contagem, 
# o segundo argumento, o número 101, é a contagem de termino da contagem, porem, 
# lembrando novamente, a contagem irá até o 100, pois o 101 não conta.
# O terceiro argumento é o step, a quantidade de casas que o programa pulará, logo, 
# neste caso, o programa sempre imprimirá um número e pulará outro, imprimindo na 
# tela somente os números impares.

for num in range(1, 101, 2):
    print(num) # Retorno será:  {1, 3, 5, 7, 9, 11, 13, 15, 17, 19....}


for i in range(6):
    print(i)




print('\n')
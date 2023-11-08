"""
    Uma das orientações de boa prática de programação é a não repetição de códigos, existem conceitos das linguagens de programação
    para auxiliar os programadores a não repetir códigos desnecessáriamente, neste modolo que focaremos nas estruturas de controle, 
    além das estruturas de controle, as de repetição

    Nesta aula falaremos sobre o while.

    Imagine que você precise escrever dez vezes seguidos um determinado comando, o while, recebe uma condição para que retipa o bloco
    de código quantas vezes forem necessários para satisfazer as necessidades do programador

    O uso do while para quando, o código precisa ser repetido sem que o programação saiba quantas vezes ele será executado, por exemplo, 
    caso o usuário do programa precise informar quantas vezes será repetido um processo, ou digamos no uso de um menu onde o usuário fica
    interagindo naquele menu até que ele escolha sair, atendendo assim, a condição para para o programa.

"""
print('\n')

print('\nExemplo do uso do while')
contador = 1 # contador será utilizado como condição para o funcionamento do while

while contador < 11: # O while repetirar seu bloco de código enquanto o contador for menor que 11
    print(contador) # imprime o valor contido na variavel contador
    contador += 1 # está linha acrescenta um a cada repetição que o while fizer
# quando o contador cheguar a 11, a condição do while retornará falsa e o programará sairá do bloco de código

# Devemos ter atenção porque while gera a repetição do código infinitamente se mal programado, um exemplo que pode ser dado é caso
# O programador erre ao acrescentar um valor a cada volta do laço fazendo com que a condição para sair do while, jamais seja atendida

# Existe palavras chaves que quebram o laço de repecição como exmplo no código abaixo

print('\nExemplo do uso do while')
contador = 0 # contador
while True:# Podemos inicar o while passando verdadeiro para ele, neste caso, não pode mais ser alterado este valor bolleano
    contador += 1 # contador acrescenta um ao valor anterior
    print(contador) # imprime na tela o valor contido na variavel contador

    if contador == 11: # executará o bloco de código quando o contador chegar a onze
        break # a palavra chave break, quebra o laço de repetição, paranando asssim, o funcionamento do while

# Tempo a palavra chave continue, conforme exemplo abaixo

print('\nExemplo do uso do while')
contador = 0 # inicialização de contador
while True: # laço de repetição
    contador += 1 # Acrescenta um ao valor do contador
    

    if contador % 2 == 1: # Caso a condição seja atendida, acionará o bloco de de código abaixo
        # A palavra chave continue vai para a leitura do código neste ponto, e retornará ao inicio do laço, neste caso, 
        # nenhum código abaixo dele será executado
        continue 

    if contador == 22: # Quando a condição do if acima, retornar falso, o compilador verificará esta condição
        break # Quando a condição acima retornar verdadeiro, o break encerrará o laço de repetição
    
    # Este printe só será executando quando não for atendido mas condições dos if's acima, assim, pela lógica deste código do while, 
    # o programa irá imprimir somente os números pares já que, quando o resto da divisão, condição do if número um, for atendida, 
    # a palavra chave continue, interromperá o código sem dar acesso ao resto do código dentro do laço while, quando não atendido, 
    # o programa chegará ao print e imprimirá os números pares já que, o primeiro if filtra números pares.
    # Quando o contador chegar ao número 22, a condição do segundo if será atendida e, a palavra chave break, encerá o código do while
    # sem que o compilador impria o 22 como sendo um número par.
    print(contador)

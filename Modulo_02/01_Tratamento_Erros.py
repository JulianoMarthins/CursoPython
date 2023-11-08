"""
    Tudo o que fizemos até agora foi ordenar o computador a realizar uma tarefa, e ordens nem sempre podem ser cumpridas, por
    exemplo, você ordenar o computador conveter a string 'Python' em um valor inteiro, o computador tentará executar sua ordem
    e retornará um erro.

    Tipo de erros no Python

    Erros de sintaxe =>  Ocorrem quando o código viola as regras da sintaxe Python e não pode ser compilado.

    Erros de tempo de execução  =>  Ocorrem quando o código é compilado com sucesso, mas há um problema durante a execução
    do programa. Isso pode incluir erros como divisão por zero, acesso a índices inválidos em listas, strings, entre outros.

    Erros de Exceção    =>  São erros específicos que ocerrem em determinadas situaçãos, como a tentativa de abrir um arquivo
    que não existe ou chamar um método em um objeto que não suporta este método.

    Erros lógicos   =>  Esses erros ocorrem quando o programa não produz os resultados esperados devido a lógica incorreta ou a
    um erro na implementação do algoritmo.

    Alguns erros dos citados acima pode deixar o programa funcionando, sem alertas ao programador, porem não se comportar como
    deveria, isso é o que chamamos de bug

    Outros erros dos citados acima podem travar o programa por completo, este erros podem ser tratados para que, o programa não 
    trave por completo, e retorne ao usuário, ou programado, códigos específicos para facilitar o programador a corrigir esses bug

    Nesta aula seremos introduziso a palavra chave "Try", que muda a lógica do que fizemos até aqui, em trechos do código que podem
    ocorrer erros, não seria interessante o programador ordenar que o computador faça algo, forçando ele a possivel erro, seria mais
    interessa usar o comando Try, onde "pede" para o computador tentar fazer algo.

    A lógica deste processo é muito similar ao if e else, Try, significa, tente executar a linha de código abaixo, caso dê algum
    erro, caia pro bloco de código except, em comparação, if é igual ao try, ifele é igual ao except, e ainda temos um bloco de
    código, não obrigatório, chamado de finaly, que será executado em todas as condições, o programa tendo executado sem erros o
    trecho de código do bloco try, ou dando erro e executando o trecho de código do except.

    O bloco do try somente irá tratar erros de compilação ou tempo de execução

    Usar termos condicionais como o if e else, podem fazer tratamento de erro mas, não é aconcelhave, este método de tratamento
    iria apenas testar condições, sendo muito mais propisso ter erros durante o processo, pois ele não evita erros. A segurança
    que o try e except trás ao programador é muito maior sendo estritamente recomendavel o uso do try para tratamento de erros, na
    verdade, ele existe básicamente só pra isso.



"""

print('\n')

num = input('Digite um número: ') # A variável num receberá uma string

# No trecho de código abaixo, o programa lançará uma excessão caso o usuário digite letras ao invés de números
# <num_numerico = float(num)> # A variavel receberá a conversão da string para num

# Para garantir que o programa não lance a exessão, vamos tratar a mesma


# Solicita que o compilador "tente", e não "faça" o que está no bloco de código abaixo
try: 
    num_numerico = float(num) # Possibilidade de erro, programa sai do bloco try caso não possa converter este valor.
    print(f'O dobro do valor digitado foi {num_numerico * 2:.2f}') 

except: # Bloco abaixo só será acionado se houver erro no bloco try
    print('Erro, impossivel converter este valor para um número')
    # Com o tratamento acima, o programa não trava, retorna a mensagem de erro





print('\n')

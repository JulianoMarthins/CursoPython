"""
    Python é uma linguagem de programação de tipagem dinâmica e forte
    Todas as linguagens de programação tem um estilo de tipagem, a dinâmica faz com
    que o python 'Deduza' o tipo de dado passado como argumento para a função print
    ou variaveis. 

    Strings nada mais é do que textos, dados com uso de caracteres, onde o mesmo pode
    ser números, caso este seja tratado como string, não pode ser realizado calculos
    com ele.

    O uso de números como string serve, por exemplo, para o armazenamento de CPF de
    clientes já que, ao ser armazenado, string deixará todos os números, até mesmo 
    espaços vazios nas linhas, porem, se um CPf foi armazenado como um tipo primitivo
    de número, e o mesmo iniciar com zero, a linguagem eliminará o zero deixando o CPF
    do cliente incompleto

    O codigo de String em python é str, e sempre deve estar entre aspas simples, a 
    linguagem aceita o uso de aspas duplas porem, por convenção, se usa aspas simples.

    Neste texto que está lendo agora, ele está entre três aspas duplas, também pode
    ser feito em três aspas simpes, este formato também é uma string mas a convenção
    é a ser usado para realizar a documentação, explicando o programa ou uma função
    em específico.

    Durante o código pode ser observado o uso do # para realizar um comentário no
    código, isso serve para o programador fazer pequenos comentários que o auxilie
    a lembrar, futuramente, sobre o que se trata aquele trecho de código ou melhorar
    a legibilidade do código a outros programadores qeu venham a dar manuntenção
    futura no código

"""
print('\n')

# retorna o tipo primitivo da variavel teste, neste caso, int
teste = 1234 
print(type(teste)) 

# retorna str porque os números foram salvos entre aspas
teste = '1234'
print(type(teste)) 

# A convenção do python pede que use aspas simples, porque, no texto, caso seja
# necessario colocar aspas em uma palavra, deve ser contrarária a aspas da string
# ou seja, se aberto a string com aspas simples, a palavra em destaque terá aspas
# dupas

print('A plavra em "MAIUSCULO" está entre aspas duplas')

print('\n')
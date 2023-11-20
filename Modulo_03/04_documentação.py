"""
                    DocString e Annotation

        DocStrings e Annotation são dois tipos de documentações que se deve implementar as 
    funções, o mais recomendado por ser mais completa e utilizado no mercado de trabalho é a
    DocString.
        Na primeira linha das funções, deve ser aberto três aspas simples ou duplas, exatamente
    como fazemos para poder escrever este texto agora, na realidade, conforme mencionado no
    inicio do curso, comentários de código deve ser escritos ao lado de um '#', este será
    ignorado pelo código e serve para ajudar no entendimento ou realizar pequenas lembraças,
    organização do código, etc...

        Já as DocStrig são sempre lidas pelo compilador, o uso dela não é para o que estamos
    fazendo aqui agora, anotações pessoas, no caso eu optei por usar assim por ser mais pratico
    do que ficar colocando '#' linha por linha que eu quizesse escrever algo e, para uso pessoal,
    para os estudos, escrever tentando explicar o que entendi me ajuda muito no entendimento do 
    conteúdo

        DocString exige uma padronização e serve para passar as funcionalidades, parametros de
    entrada e saída da função, ela pode ser consultada futuramente e, por isso, tem sua
    obrigatoriedade as funções.

                    Exemplos abaixo mostram o uso da DocString
 

"""
print()

def somar(num=0, num2=0):
    ''' Realiza a soma de dois números

    Parametros:
        num (int): Primeiro número inteiro
        num2 (int): Segundo número inteiro

    retorno:
        soma (int): Retorna a soma dos números inteiros
       
    '''
    soma = num + num2
    return soma


resultado = somar(5, 3)
print(resultado)

def dividir(num, num2):
    ''' Realiza a divisão de dois números
    
    Parametros:
        num (int): Primeiro valor
        num2 (int): Segundo valor

    Return: 
        divisao (int | float): Retona a divisão 
    '''
    try:
        divisao = num / num2
    except ZeroDivisionError:
        print('Impossivel realizar divisões por zero')
    else:
        return divisao


resultado = dividir(15, 3)
print(resultado)

testando = dividir(20, 2)

# Observe abaixo que, ao deixar o cursor do mouse dentro dos parenteses, do código abaixo, no
# VsCode, ele abre a DocString automáticamente podendo assim, realizar a consulta sobre a 
# documentação do mesmo. No caso da função somar(), para não ficar dando erro pois não foi passado
# os parâmetros, foi adicinonado valores padrão, assim, tirando a obrigatoriedade de adição dos
# valores para a demonstração do exemplo abaixo
somar()

# Caso ficasse dando erro, o VsCode mostraria a DocString normalmente, porem, teria mais
# informações sobre o motivo do erro apontando na linha.

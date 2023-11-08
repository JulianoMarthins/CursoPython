"""
    Operadores lógicos são palavras chaves que auxiliam na checagem por condições para valores booleanos, elas ligam
    dois valores a ser chegado, retornando verdadeiro ou false dependendo de sua exigência


    As palavras chaves são

    and ->  Retorna verdadeiro se o primeiro valor "e" o segundo forem verdadeiros
    or  ->  Retorna verdadeiro se o primeiro valor "ou" o segundo forem verdadeiros
    in  ->  Verifica se o primeiro valor está dentro do segundo valor
    not ->  Valor negacional, inverte o valor da expressão, ou seja, se ela retornar verdadeiro, e usarmos o not, ela 
    inverterá o retorno para falso

    Existe também os operadores de comparação

    ==  ->  Chega se o primeiro valor é igual ao segundo
    >   ->  Chega se o primeiro valor é maior que o segundo
    >=  ->  Chega se o primeiro valor é maior ou igual ao segundo
    <   ->  Chega se o primeiro valor é menor que o segundo
    <=  ->  Chega se o primeiro valor é menor ou igual ao segundo

"""
print('\n')

if 10 == 10:
    print('Retorna verdadeiro, pois 10 é igual a 10')

if 10 > 10:
    print("Retorna falso, pois 10 não é maior que 10")

if 12 >= 10:
    print('Retorna verdadeiro pois 12 é maior ou igual a 10')

# Comparação usando palavras chaves

nome = 'Juliano'

if 'Jul' in nome:
    print('Existe os caracteres, sequenciais "Jul" na palavra Juliano')

if 'Jul' not in nome:
    print('Perceba que este trecho de código não será executado pois, apesar de ter "Jul" na palavra Juliano,'
          + ' a expressão esta com a negação "not", a leitura seria, "se não tiver Jul em Juliano"')


# Um uso interessante para o operador or

# A variavel senha receberá a string "Não digitou nenhum valor" caso o usuário não digite nada na solicitação de senha
senha = input('Digite algum valor: ') or 'Não digitou nenhum valor'

print(senha)


print('\n')
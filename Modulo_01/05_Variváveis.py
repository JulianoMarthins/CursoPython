"""
    Variváveis são usadas para salvar informações na memória do computador, em Python, existe uma convenção de boas praticas
    que padroniza a linguagem chamda de PEP8, ao longo do curso veremos os aspéctos dela.

    A PEP8 define que, para ser criado uma variável, ela não pode começar com números, deve ser toda com letras minusculas e,
    quando necessário usar duas palavras, fazer a separação dessas com um underline, não deve ser usado acento.
    
    O sinal de igual (=) serve para atribuir o valor a direita, a variavel criada 
    Os nomes das variavels devem ter, segundo orientação do PEP8, nome plausivel com o valor contido na mesma, 
    se vai guardar um cpf, o nome da variável deve ser cpf, se foi guardar um nome, a variavel deve ser chamar nome.

    A variavel não deve ser criada para diminuir um código mas sim, para deixar o código mais legivel.

    Exemplo:

    nome_variavel = 'valor'

"""
print('\n\n')


# A variavel guarda um valor e pode ser utilizada em outras cituações
soma = 2 + 2 # variavel soma guarda a soma de 2 com 2
print(f'A soma de dois números: {soma}') # A variavel soma é passada como argumento para imprimir seu valor na tela

# Pode ser feito calculos usando variaveis, pois, nem sempre, saberemos qual valor terá dentro da mesma.
soma = 2 + 5 # A variavel soma recebe a soma de 2 e 5
multiplicaçao = 4 * 3 # A variavel multiplicaçao recebe a multiplicação de 4 por 3

# A variavel resultado recebe a soma do valor contido em soma com o valor contido na variavel multiplicação
resultado = soma + multiplicaçao 

# Imprime na tela os valores guardados nas variaveis
print(f'O resultado da primeira soma "{soma}" com a multiplicação "{multiplicaçao}" é: {resultado}') 

# Podem ser feitos concatenação em variaveis
nome = 'Marcelo'
sobrenome = 'Ribeiro'

print(nome, sobrenome)

maior_idade = 46 >= 18 # Retorna um valor boleano, neste caso, como 46 é maior que 18, ele retornará True
print(f'Pessoa é maior de idade? {maior_idade}')

print('\n\n')






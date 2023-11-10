"""
    Função id

"""
print('\n')


# Retorna a referência de memória da variável valor
valor = 'a'
print(id(valor)) 
variavel = 'a'

# Apesar de ser variáveis diferentes, como guardam o mesmo valor, elas apontam 
# para a mesma referência de memória
print(id(variavel)) 

# Na verdade, a conferência abaixo não é sobre o valor guardado nas variveis, 
# mas sim, sobre a conferência dos endereços de memória das variaveis, retorna 
# true porque, como contém o mesmo valor, contém o mesmo endereço de memória
print(variavel == valor) 


print('\n')

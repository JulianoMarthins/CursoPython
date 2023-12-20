"""
                            Data Frame
        Data Frame é como se fosse uma tabela onde:

            As colunas funcionam como chaves de dicionários
            As linhas funcionam como listas



"""
import pandas as pd
print()

vendas_df = pd.read_csv(r'D:\\WorkSpace\\Python\\Python_Impressionador\\Pandas\\Contoso - Vendas - 2017.csv', sep=';')

# Abaixo será impresso a tabela completa
print(vendas_df)

print('\nAcessando tabela pela chave da coluna Id produto:')
# As colunas da tabela funcionam similarmente as chaves dos dicinários, logo, 
# podemos acessar somente os valores específicos necessários, no caso do exemplo 
# abaixo, será retornado somente a coluna do ID Produto
print(vendas_df['ID Produto'])

print('\nAcessando a tabela pelas chaves ID Produto e ID Cliente:')
# Caso seja necessário acesar mais de uma coluna, você precisa passar uma lista de
#  strings como 'chave' da tabela
print(vendas_df[['ID Produto', 'ID Cliente']])


print('\nAcessando a tabela por indice:')
# As linhas da tabela poder ser acessada pelo indice, no código abaixo, será 
# impresso todas as colunas da tabela, das linhas 00 até a linha 02
print(vendas_df[:3])

# Caso seja necessário a impressão somente da primeira linha, o Python retornará 
# um erro caso você tente acessar somente pelo indice 0, (vendas_df[0]). O correto
# será acessar os elementos da tabela 'ATÉ' o indice zero, mesmo que o indice zero
# seja o primeiro, exemplo: (vendas_df[:1]), lembrando que o elemento de indice 1,
# neste caso, não será retornado.


print()
# O primeiro passo da sua base de dados, é entender os elementos de sua base de dados
# Para isso, podemos utilizar a função .info()

print('Informações sobre a tabela: ')
print(vendas_df.info())

# O retorno do método info() trás informações úteis sobre os dados contidos no
# arquivo analisado, como a quantidade de colunas, nome delas, número de linhas total
# da tabela, informa se existe colunas com informações vazias, nulas no caso, e o
# tipo primitivo dela.


# Exemplo de código para pegarmos uma lista dos clientes da tabela

lista_clientes = vendas_df['ID Cliente']
print(f'\nLista de clientes: \n{lista_clientes}')

# Exemplo de controle de um estoque
lista_colunas = ['ID Produto', 'Quantidade Vendida', 'Quantidade Devolvida']
produtos_quatidade = vendas_df[lista_colunas]
print(f'\nQuantidade de produtos:\n{produtos_quatidade}')
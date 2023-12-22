import pandas as pd

# Lendo os arquivos CSV da empresa
vendas_df = pd.read_csv(r'Contoso - Vendas - 2017.csv', sep=';')
produtos_df = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';', encoding='ISO8859-1')
lojas_df = pd.read_csv(r'Contoso - Lojas.csv', sep=';', encoding='ISO8859-1')
cliente_df = pd.read_csv(r'Contoso - Clientes.csv', sep=';', encoding='ISO8859-1')

# Renomeando colunas para padronizar as tabelas
produtos_df = produtos_df.rename(columns={'ÿNome do Produto': 'Nome Produto'})
lojas_df = lojas_df.rename(columns={'ÿID Loja': 'ID Loja'})
cliente_df = cliente_df.rename(columns={'ÿID Cliente': "ID Cliente"})
cliente_df = cliente_df.rename(columns={'E-mail': 'E-mail do Cliente'})


# Filtrando colunas necessárias a tabela
cliente_df = cliente_df[['ID Cliente', 'E-mail do Cliente']]
produtos_df = produtos_df[['ID Produto', 'Nome Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]

# Associando as tabelas pela ID
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(cliente_df, on='ID Cliente')

vendas_lojas = vendas_df.groupby('Nome da Loja').sum()
vendas_loja = vendas_lojas[['Quantidade Vendida']]                                                            
print(vendas_lojas)
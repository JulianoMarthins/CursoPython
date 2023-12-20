import pandas as pd

produtos_df = pd.read_csv(
    r'D:\\WorkSpace\\Python\\Python_Impressionador\\Pandas\\Contoso - Cadastro Produtos.csv', sep=';', encoding='cp1252'
    )

print(produtos_df)

"""
* encoding='Latin1'
            * encoding='ISO-8859-1'
            * encoding='utf-8'
            * encoding='cp1252'
            """
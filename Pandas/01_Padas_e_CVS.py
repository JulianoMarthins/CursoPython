"""
                                O que é pandas e para que ele serve?

    * Pandas é uma biblioteca com foco em análise de dados, ou seja, para DataScience, seja para trabalhar de forma integrada
    com arquivos em Excel e Banco de Dados

    * Melhor Biblioteca/Módulo para se trabalhar com quantidades enormes de informações

    * Uma mistura de listas e dicionários de forma muito eficientes.

    Em resumo, se você trabalha com muitos dados, você vai precisar usar o pandas.

    Quase sempre quando formos "ler" um arquivo csv, vamos usar o pandas, com ele o processo se torna mais prático, e muito mais
    eficiente.

    Devemos lembrar que o formato padrão de arquivos .csv é de vir todas as informações unidas, como se fosse um texto só, a cada
    quebra de linha que existe no arquivo, é marcada por um ponto e virgula (;), sendo assim, ao passar o parâmetro ao método de
    leitura, sep=';', o leitor do pandas irá separar todas as palavras que forem encontradas um ponto e virgula criando novas colunas
    para a tabela.

"""

import pandas as pd

print()

vendas = pd.read_csv(r'D:\WorkSpace\Python\Python_Impressionador\Pandas\Contoso - Vendas - 2017.csv', sep=';')

print(vendas)
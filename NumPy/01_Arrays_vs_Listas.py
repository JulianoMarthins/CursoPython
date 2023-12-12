"""
        A biblioteca NumPy é amplamente utilizada para realizar operações númericas
    e computacionais eficientes em Python. ela fornece estruturas de dados de alto
    desenpenho, como arrays multidimensionais e funções matemáticas para manipulação
    desses arrays. 

        Com o NumPy você pode realizar cálculos complexos, processamento de dados,
    álgebra linear, geração de números aleatórios e muito mais. É uma ferramente
    essencial para cientista de dados e programadores que lidam com análise numérica
    e computação científica.
       
"""

import numpy as np

"""
        É muito importante entender qual a diferneça de uma lista para um array, 
        
        Um Array é uma estrutura de dados que armazena valores de um mesmo tipo, 
    em Python, isso é uma grande vantagem porque economiza espaço e permite operações
    mais eficientes.
        
        Uma lista é uma das estruturas de dados mais básicas em Pytho. ela pode 
    conter qualquer tipo de elemento, como números, string, outras listas, e todos
    eles podem ser de tipos diferentes.
    
"""

array = np.array([1, 2, 3, 4, 5])

print('ArrayList: {}'.format(array))
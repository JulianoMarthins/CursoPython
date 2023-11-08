"""
STYLE       0   =>  None
            1   =>  Bold (Texto em negrito)
            4   =>  Underline (Sublinhar a palavra)
            7   =>  Negativo (Inverte as configurações da letra e fundo)

TEXT        30  =>  Branco
            31  =>  Vermelho
            32  =>  Verde
            33  =>  Amarelo
            34  =>  Azul
            35  =>  Roxo
            36  =>  Ciano       
            37  =>  Cinza

BACKGROUND  40  =>  Branco
            41  =>  Vermelho
            42  =>  Verde
            43  =>  Amarelo
            44  =>  Azul
            45  =>  Roxo
            46  =>  Ciano       
            47  =>  Cinza

Código      => '\033[style;text;backgroungmTEXTO\033[m'


"""

print('\033[1;36mJuliano\033[m')

print()
import string
from random import choice, shuffle

def gerar_senha(args):
    if args <= 4:
        print('O tamanho da senha deve ser de pelo menos quatro caracteres')
        return None
    
    else:
        senha = [
            choice(string.ascii_letters),
            choice(string.digits),
            choice(string.punctuation)
        ]

        escolha = "".join([string.ascii_letters, string.punctuation, string.digits])
        for x in range(args - len(senha)):
            senha.append(choice(escolha))

        shuffle(senha)

    return "".join(senha)


 
tamanho = int(input("Digite o comprimento da senha: "))
print()
print(gerar_senha(tamanho))
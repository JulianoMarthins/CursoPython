from random import choice
from time import sleep

print('\n') # Trecho de código apenas para dar espaçamento nas informações do VSCODE


regras = """
                    Jogo de palavras secretas

                        Regras do jogo

        1   =>  Palavra secreta terá até seis letras
    
        2   =>  Só é permitido inserir um caracter por jogada
    
        3   =>  Mesmo que a palavra tenha acentos ou caracteres
        especiais, o mesmo não precisa ser digitado
        
"""

LISTA = [ 'exceto', 'cinico', 'mister', 'convem', 'escopo', 'merito', 'gentil', 'defina', 'otario', 'julgar', 'habito', 'obeso', 'buscar',
         'objeto', 'mulher', 'vulgar', 'ciente', 'diante', 'rancor', 'grande', 'espaco', 'coagir', 'metodo', 'servir', 'franco', 'maroto',
        'limite', 'tirano', 'inibir', 'estado', 'genero', 'trazer', 'sereno', 'deixar', 'proeza', 'teoria', 'talvez', 'divino', 'forjar',
        'suprimir', 'triste', 'sentir', 'ajudar', 'senhor', 'patria', 'brasil', 'tipico', 'depois', 'chapeu', 'patroa', 'xingar', 'expert',
        'devoto', 'timido', 'estilo', 'oficio', 'viavel', 'escola', 'voltar', 'clinica', 'agente', 'exigir', 'alegre', 'amante', 'oposto'
]

contagem_acertos = 0
contagem_erros = 0 
digitadas = str()
letras_acertadas = str()

# Seleciona uma palavra dentro as opções da lista
palavra_secreta = choice(LISTA).upper() 

print(regras)

while True:
    print('\n')
    letra = input('\nDigite uma letra: ').upper()

    # Valida quantidade de caracteres digitados pelo usuário
    if len(letra) == 0: 
        print('\nDigite apenas uma letra')
        continue

    # Armazena cada caracter encontrado na palavra secreta, na variavel letras acertadas
    for letra_secreta in palavra_secreta: 
        if letra in letra_secreta:
            print('Acertou')
            contagem_acertos += 1
            letras_acertadas += letra       

    # Consome uma vida do usuário caso ele erra alguma letra, finaliza o jogo se não tiver mais vidas
    if letra not in palavra_secreta:
        contagem_erros += 1
        print(f'\nErrou')
               

    # Retorna ao usuário a letra acertada ou um # em caso de erro    
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            print(letra_secreta, end='')
            
        else:
            print('#', end='')

    # Verificação de vitória
    if len(letras_acertadas) == len(palavra_secreta):
        print("\n\n\n\nPARABÉNS\nVocê venceu")
        
        sleep(0.5)
        
        print(f'\nRelatário de jogo\nAcertos: {contagem_acertos}\nErros: {contagem_erros}')
        
        sleep(1)

        # Opções de encerrar ou continuar no jogo
        while True:
            op = input('\n\nDeseja jogar novamente?\n[S]sim [N]não: ').upper()

            if 'S' in op:
                palavra_secreta = choice(LISTA)
                print('Novo jogo sendo executado\n\nPalavra chave alterada')
                vidas = 5
                sleep(1)
                break
            elif 'N' in op:
                break
            else:
                print("Digite [S] para continuar\nDigite [N] para encerrar o programa")

        if 'N' in op:
            sleep(1)
            print("Obrigado por jogar\nPrograma encerrado")
            break            
    

print('\n') # Trecho de código apenas para dar espaçamento nas informações do VSCODE
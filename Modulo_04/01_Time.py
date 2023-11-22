'''
                            Modulo time
    
        O módulo time em python fornece uma variedade de funções para trabalhar com
    tempo.

        O módulo time.time() -> Retorna o tempo atual em segundos desde a Epoch,
    que é datada em 1° de janeiro de 1970

'''

import time
import locale

print()

# Retorna o tempo em segundos da Epoch até agora
tempo_atual_segundos = time.time()
print(f'Tempo atual: {tempo_atual_segundos} segundos desde a Epoch')

# O uso deste método poder ser útil quando você tem um programa muito grande, e o 
# mesmo está apresentando lentidão, você pode usar o método como mostrado no exemplo
# abaixo para calcular quantos segundos cada funções chave do seu programa está
# demorando para ser concluída.

inicio = time.time()

for i in range(100_000_000):
    pass

fim = time.time()

print(f'Tempo percorrido para execução da função: {fim - inicio} seg.')

print()

# O método sleep() para o programa na quantidade de segundos passado no parâmetro.
# Um exemplo de uso do sleep é pra quando você está varrendo informações de um site, 
# se você fizer isso muito rápido pode ser que ações do seu programa sejam perdidas
# por acontecerem mais rápido que o carregamento da página, por exemplo, ou até mesmo
# o ip do seu computador ser banido pelo site em caso de indentificação de processos
# muito rápidos, sendo detectado como ação de robo.

print('Inicio do sleep: 2 segundos')
time.sleep(2)
print('Fim do sleep')


# Time.ctime() -> A função ctime() converte um tempo expresso em segundos desde a
# epoch em uma string representando o tempo local.
print()
tempo_segundos = time.time()
tempo_local = time.ctime(tempo_segundos)
print(f'Tempo local: {tempo_local}')


# time.time()  vs time.localtime() -> A função time() retorna o tempo atual em 
# segundos desde a epoch. A função localtime() converte um tempo em segundos desde
# a epoch em um objeto "struct_time". Este objeto contém informações sobre o tempo 
# local, como ano, mês dia, hora, minuto, etc. A função localtime() usa o fuso
# horario local.

# Observe que será impresso na tela a hora atual, porem com cada valor nomeado, como
# se fosse um dicinário, porem, é uma tupla, mesmo assim, podemos usar essas palavras
# chaves para acessar elementos específicos de cada valor retornado pelo 
# time.localtime

print()
tempo_segundos = time.time()
tempo_local = time.localtime(tempo_atual_segundos)
print(f'Tempo local: {tempo_local}')

# Retorna o local da hora, no meu caso, Brasil
print(f'Local de captação da hora: {tempo_local.tm_zone}')

# Imprime o ano
print(f'\nAno: {tempo_local.tm_year}')

# Retorna o dia do ano
print(f'Dia do ano: {tempo_local.tm_yday}')

# Retorna o dia do mês
print(f'Dia do mês: {tempo_local.tm_mday}')

# Retorna o mês do ano
print(f'Mês do ano: {tempo_local.tm_mon}')

# O retorno da dastas é um inteiro





locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

tempo_struct = time.localtime()
tempo_formatado = time.strftime("%A, %d de %B de %Y, %H:%M:%S", tempo_struct)

print(f'Tempo formatado: {tempo_formatado}')


# time.strptime() -> A função analisa uma string representando um horario de acordo
# com um formato. O retorno é um objeto struct_time.


# Sentido inverso, pegar uma string e transformar em um objeto de tempo válido

string_tempo = '30 Junho, 2023'
formato = '%d %B, %Y'
tempo_struct = time.strptime(string_tempo, formato)

print(f'Data formatada em struct: {tempo_struct}')
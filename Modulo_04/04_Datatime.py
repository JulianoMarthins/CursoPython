"""
        O modulo time é considerada mais simples que o modulo datatime, ela é 
    geralmente menos usada e, tem seu foco em serviços mais simples. Já o modulo
    datatime é mais completa e tem execelentes metodos para realizar o calculo
    entre datas e horários.

        O modulo datetime tem uma classe chamada datetime, logo, parece estranho
    sua importação, que seria 'from datetime import datetime.


"""
# Importação da função datetime, que faz parte da biblioteca datetime
from datetime import datetime

print()

# O metodo abaixo retorna a data e dia atual
agora = datetime.now()
print(f'.now() => {agora}')
# Retorna a data no formato - (ano, mês, dia, hora, minutos, segundos, milesegundos)

# Retorna somente a data
print(f'.date() => {agora.date()}')

# Retorna somente a hora
print(f'.time() => {agora.time()}')

# Abaixo veremos alguns atributos da classe, por isso os 'METODOS' ACIMA tem 
# parenteses e os de baixos naõ tem

# Retorna somente o ano
print(f'.year => {agora.year}')

# Retorna somente o mês
print(f'.month => {agora.month}')

# Retorna somente o dia
print(f'.day => {agora.day}')

# Retorna somente a hora
print(f'.hour => {agora.hour}')

# Retorna somente os minutos
print(f'.minute => {agora.minute}')

# Retorna somente os segundos
print(f'.second => {agora.second}')


# O modulo datetime possui uma classe chamada .timedelta(), que é usada para 
# operações com datas, no caso, adição e subtração.

print('\n')
# Importação do timedelta
from datetime import timedelta

# Imprime a data e horario atual
data_atual = datetime.now()
print(f'Data atual: {data_atual}')

# Ao passar 'days=10' como parâmetro para o timedelta, ele acrescentará dez dias
# a data_atual
data_futura = data_atual + timedelta(days=10)
print(f'.timedelta(days=10), adição => {data_futura}')

data_passada = data_atual - timedelta(days=10)
print(f'.timedelta(days=10), subtração => {data_passada}')

# Soma dez horas ao horario atual
dez_horas_futuro = data_atual + timedelta(hours=10)
print(f'.timedelta(hours=10), somando dez horas => {dez_horas_futuro}')
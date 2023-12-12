"""
        O módulo datetime em Python fornece classes para manipulação de datas
    e horas. Aqui está um guia simples para algumas das funções mais úties deste
    módulo.

"""

# A função strftime() converte um objeto datetime par auma string de acordo com um
# formato específico.

print()

# Importa a lib de localização
import locale
from datetime import datetime

# Definir localização para português
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')


                    # Função strftime()

agora = datetime.now()
print(agora)

# Variavel agora é do tipo datetime
print(type(agora))

print()
# O código %a retorna as iniciais do dia da semana
print(agora.strftime('%a'))
# O código %A retorna o dia da semana completo
print(agora.strftime('%A'))

# Código abaixo retorna a data de hoje completa, no caso do dia de estudo deste
# módulo, retorna -> Segunda-feira, 27 de novembro de 2023, 20:37
print(agora.strftime("%A, %d de %B de %Y, %H:%M"))


                    # Função strptime()

    # A função strptime() analisa uma string representando uma data e hora de
    # acordo com um formato. O retorno é um objetivo datetime

print()

string_data = "04 Junho, 1982, 15:30"
formato = "%d %B, %Y, %H:%M"

data = datetime.strptime(string_data, formato)

print(f'Data: {data}')


                    # Trabalhando com fuso horário
print()


data_hora = datetime(2023, 6, 26, 15, 30, 20 )
print(f'Data/hora: {data_hora}')
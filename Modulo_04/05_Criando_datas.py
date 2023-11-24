"""
            Criação de um objeto datatime

        Podemos criar um objeto datetime usando a classe datetime. O construtor
    da classe possui como principais arumgos: 

        * year: ano, 2023
        * month: mês (1-12)
        * day: dia (1-31)
        * hour: hora(0-23)
        * minute: minuto(0-59)
        * microsegund: microssegundo (0-999999)
        * tzinfo: fuso horario

        Os parametros podem ser passados no contrutor por nomes, apensar dessa ser
    uma boa prática de programação, caso você passe somente os valores, a linguagem
    aceitará e, interpretará na ondem acima descrita, ano, mes, dia, hora, minuto,
    microssegundo e fuso horario.
        Para a instanciação deste objeto não é obrigado a passar todos os arugmentos
    mas obrigado a fechar os argumentoe necessários por cada informaçõa, por exemplo, 
    a data, será obrigado a passar o ano, mes e dia. Já no caso de horas, pode ser
    passado qualquer argumento, somente hora, somente minutos, ou ambos.
        Porem, o construtor sempre inicializará com a data e hora, caso a hora não 
    seja adicionado no construtor, seu valor será zerado e retornado quando utilizado
    

"""
print()

from datetime import datetime

# O contrutor foi instanciado com a data 04/06/1982
nascimento = datetime(year=1982, month=6, day=4,)
print(f'Aniverssário: {nascimento}') # Retorna a data passada pelo construtor

print()
# O formato de data (2023-6-4) é o formato padrão pela iso, você pode passar uma
# string que respeite essa isso, assim ela será utilizada como uma data válida
# para o python, porem, a string precisa ser passada como argumento dentro da 
# função datetime.fromisoformat(data)

data_string = '2023-06-26 15:30'
data_hora_iso = datetime.fromisoformat(data_string)
print(f'Data formatada: {data_hora_iso}')


                # Calculando a diferença entre duas datas
print()

# Pega a hora e data atual pelo sistema do computador
data = datetime.now()
# Retorna a variável a diferença entre o dia atual e o nascimento
tempo_vida = data - nascimento
# Retorna quantos dias de vida possou o dia de hoje, no dia deste estudo, eu tinha
# 15147 dias de vida, 22:15 horas de vida... Quase envelhecendo mais um dia... kkk 
print(f'Dias de vida: {tempo_vida}')
# Idade
idade = tempo_vida.days / 366
print(f'Idade: {int(idade)}')



                    # Comparação entre duas datas


data1 = datetime(2023, 6, 25)
data2 = datetime(2023, 7, 25)

# Comparações seguem o padrão comprarativo utilizados com if e else. Caso suas datas
# tiverem horarios, obviamente, as horas, minutos e segundos importam nas condições
# do if e else.
if data1 > data2:
    print('A data1 é posterior a data2')
elif data1 < data2:
    print('A data1 é anterior a data2')
else:
    print('As datas são iguais')


                    # Ordenação de datas

print()
# Criaremos uma lista de datas
lista_datas = [
    datetime(2023, 6, 28),
    datetime(2023, 5, 28),
    datetime(2023, 7, 28),
    datetime(2023, 6, 18)
]

# Utilizamos uma nova variavel para retornar uma nova lista com a ordenação das
# datas passadas como argumento no método sorted
datas_ordenadas = sorted(lista_datas)

print('Datas ordenadas pelo metodo sorted')
# Laço de repetição para impressão de cada data da lista em ordem
for cont, data in enumerate(datas_ordenadas):
    print(f'{cont + 1}°: {data}')

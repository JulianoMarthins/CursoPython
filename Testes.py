print()

import time
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
tempo_segundos = time.time()
tempo_local = time.ctime(tempo_segundos)

print(f'Tempo local: {tempo_local}')
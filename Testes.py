print('\n')

while True:
    estado_civil = input(\
        'Digite seu estado civil:\n[S]olteiro\n[C]asado\n[V]iuvo\n[D]disquitado'\
            ).upper()
    
    if 'SCVD' not in estado_civil:
        print('Naõ achei')
    else:
        print('achei')
  

print('\n')
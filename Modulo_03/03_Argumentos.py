def padronizar_codigo(lista_codigos, padrao='m'):
   
    for i, item in enumerate(lista_codigos):
        item = item.replace('  ', ' ')
        item = item.strip()

        if padrao == 'm':
            item = item.casefold()
        elif padrao == 'M':
            item = item.upper()
            
        lista_codigos[i] = item
            
              

    return lista_codigos




print()
cod_produtos = [' ABC12 ', 'abc34', 'AbC37']

retorno = padronizar_codigo(lista_codigos=cod_produtos, padrao='M')

print(retorno)


import matplotlib.pyplot as plt

print()

# Dados a serem analisados
venda_mes = [1500, 1727, 1350, 999, 1050, 1027, 1022, 1500, 2000, 1433, 2100, 2762]
mes = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

# Recebe no parâmetro os valores para criar os graficos, sendo meses para o eixo x e vendas
# para o eixo Y
plt.plot(mes, venda_mes)

# Adiciona um nome ao eixo y
plt.ylabel('Vendas')
# Adiciona um nome ao eixo X
plt.xlabel('Meses')

# Linha de código abaixo apresenta erro apensar do código funcionar corretamente com a linha
# descomentada. 

# plt.axis([0, 11, 0, max(venda_mes)+500])


# Mostra em tela o gráfico dos dados analisados
plt.show()

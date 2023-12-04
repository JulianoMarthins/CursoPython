import matplotlib.pylab as plt
import numpy as np

print()

# Randomiza 50 números inteiros entre 1000 e 3000
vendas = np.random.randint(1000, 3000, 50)

# Randomiza númeração entre 1 e 50
meses = np.arange(1, 51)

# Cria figura no tamanho 15x3
plt.figure(1, figsize=(15, 3))

# Figura 1, gráfico em linha
plt.subplot(1, 3, 1)
plt.plot(meses, vendas, color='green')

# Figura 2, gráfico em bolas
plt.subplot(1, 3, 2)
plt.scatter(meses, vendas)

# Figura 3, gráfico em barras
plt.subplot(1, 3, 3)
plt.bar(meses, vendas)

# Mostra na tela os gráficos ao usuário
plt.show()

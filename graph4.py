import pandas as pd
import matplotlib.pyplot as plt

manchas = pd.read_csv("a2_MANCHAS.csv")
manchas = manchas.head(30)

plt.style.use('Solarize_Light2')

plt.plot(manchas.Ano, manchas.manchas, '.c-')
plt.step(manchas.Ano, manchas.manchas, '.', color='c')
plt.title("Número de manchas solares em Wolfer", color='c')
plt.xticks(manchas.Ano, manchas.Ano, rotation='70', color='k', size='x-small', style='italic')
plt.yticks(color='k')
plt.subplots_adjust(bottom=0.15)
plt.xlabel("Ano", color='c')
plt.ylabel("Manchas", color='c')
plt.grid(True)

plt.savefig("graph4.jpg", quality=100, optimize=True, dpi=300)


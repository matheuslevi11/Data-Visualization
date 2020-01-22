import pandas as pd
import matplotlib.pyplot as plt

manchas = pd.read_csv("a2_MANCHAS.csv")
manchas_tail = manchas.tail(10)


plt.style.use('dark_background')

plt.plot(manchas_tail.Ano, manchas_tail.manchas, ':', color='w')
plt.scatter(manchas_tail.Ano, manchas_tail.manchas, marker='*', color='m')
plt.title("Número de manchas solares em Wolfer", color='m')
plt.xticks(manchas_tail.Ano, manchas_tail.Ano, rotation='70')
plt.subplots_adjust(bottom=0.15)
plt.xlabel("Ano", color='m')
plt.ylabel("Manchas", color='m')
plt.grid(True, color='m')

plt.savefig("graph2.jpg", quality=100, optimize=True, dpi=300)
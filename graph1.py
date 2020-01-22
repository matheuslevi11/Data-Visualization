import pandas as pd
import matplotlib.pyplot as plt

manchas = pd.read_csv("a2_MANCHAS.csv")
manchas_head = manchas.head(10)

plt.style.use('dark_background')

plt.plot(manchas_head.Ano, manchas_head.manchas, '--', color='r')
plt.title("Número de manchas solares em Wolfer", color='r', weight=650)
plt.xticks(manchas_head.Ano, manchas_head.Ano, rotation='70')
plt.subplots_adjust(bottom=0.15)
plt.xlabel("Ano", color='r', weight=600)
plt.ylabel("Manchas", color='r', weight=600)
plt.grid(True)
plt.savefig("graph1.jpg", quality=100, optimize=True, dpi=300)
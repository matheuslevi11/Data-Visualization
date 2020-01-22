import pandas as pd
import matplotlib.pyplot as plt

manchas = pd.read_csv("a2_MANCHAS.csv")

plt.style.use('seaborn')

plt.plot(manchas.Ano, manchas.manchas, 'r-', linewidth=0.8)
plt.title("Número de manchas solares em Wolfer", color='r', weight='650', size='large')
plt.xticks(color='k', style='italic')
plt.yticks(color='k')
plt.subplots_adjust(bottom=0.15)
plt.xlabel("Ano", color='r', weight=500, size='large')
plt.ylabel("Manchas", color='r', weight=500, size='large')
plt.grid(False)
plt.savefig("graph5.jpg", quality=100, optimize=True, dpi=300)
import pandas as pd
import matplotlib.pyplot as plt

manchas = pd.read_csv("a2_MANCHAS.csv")

plt.boxplot(manchas.manchas)
plt.title("Número de manchas solares em Wolfer")
plt.ylabel("Quantidade de manchas")


plt.savefig("graph3.jpg", quality=100, optimize=True, dpi=300)
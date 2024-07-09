import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

d = 0.2
L = 0.5
k = 10000
g = 9.81
m = (180 + 39)
h = np.sqrt(L**2 - d**2)

def f(u):
    return 2 * k * (L - ((h - u) ** 2 + d ** 2) ** 0.5) * ((h - u) / ((h - u) ** 2 + d ** 2) ** (0.5))-m*g

def keq(u):
    h = 1e-9
    return (f(u + h) - f(u)) / h  # derivada da funcao f

resposta = fsolve(f, [0, h])
keq1 = keq(resposta[0])
keq2 = keq(resposta[1])
print("Valores do deslocamento no equilíbrio estático em m:", resposta[0],resposta[1])
print("Valores da rigidez efetiva no equilíbrio estático em N/m:", keq1,keq2)
u = np.linspace(-h, h, 1000)

fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(u, f(u))
ax1.scatter(resposta, [0, 0], color='red')
ax1.set_title('f(u)')
ax1.grid()

ax2.plot(u, keq(u))
ax2.scatter([resposta[0], resposta[1]], [keq1, keq2], color='red')
ax2.set_title('keq(u)')
ax2.grid()

plt.tight_layout()
plt.show()
import math
import numpy as np
import matplotlib.pyplot as plt

b = 0.2
delta_k = (50 + 0.5 * 39) * 1000
k_min = 10 * 1000
k = []

F1 = np.zeros((10, 1))
K1 = np.zeros((10, 10))

F1[4][0] = -50
F1[9][0] = 100

for i in range(10):
    kn = k_min + delta_k * math.exp(-b * (i + 1))
    k.append(kn)

for i in range(10):
    if i == 0:
        K1[i][i] = k[i] + k[i + 1]
        K1[i][i + 1] = -k[i + 1]
    elif i == 9:
        K1[i][i - 1] = -k[i]
        K1[i][i] = k[i]
    else:
        K1[i][i - 1] = -k[i]
        K1[i][i] = k[i] + k[i + 1]
        K1[i][i+1] = -k[i + 1]

u1 = np.linalg.solve(K1, F1)
print("Caso 1: \n",np.round(u1,4))

K2 = K1[:-1, :-1]
F2 = np.zeros((9, 1))

F2[8][0] = 0.03*k[9]

u2 = np.linalg.solve(K2, F2)

print("Caso 2: \n",np.round(u2,4))

n = np.linspace(0, 10, 10)

plt.figure(figsize=(8, 10))

plt.subplot(2, 1, 1)
plt.plot(n, u1, label='u1', color='blue')
plt.xlabel('x [m]')
plt.ylabel('u(x) [m]')
plt.title('Deslocamento para um ponto x')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(n[:-1], u2, label='u2', color='green')
plt.xlabel('x [m]')
plt.ylabel('u(x) [m]')
plt.title('Deslocamento para um ponto x')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
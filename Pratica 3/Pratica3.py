import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt

N = 39
r = 100
v0 = (10 + 0.1 * N)

def a_t(s):
    return (4 + 0.01 * N * s - 0.01 * s * s)

def v(s):
    return np.sqrt(8 * s + 0.01 * N * s**2 - (0.02 * s**3)/3 + v0**2)

def a_r(s):
    return v(s)**2/r

def a(s):
    return np.sqrt(a_t(s)**2 + a_r(s)**2)

tempo = integrate.quad(lambda s: 1/v(s), 0, 20)

print("A velocidade do veículo ao percorrer 20 metros é:", v(20))
print("A aceleração do veículo ao percorrer 20 metros é:", a(20))
print("O tempo necessário para percorrer 20 metros é aproximadamente:", tempo[0])

s = np.linspace(0, 1000, 1000000)
v_s = v(s)

plt.figure(figsize=(8, 10))
plt.subplot(2, 1, 1)
plt.plot(s, v(s), label='v*s', color='blue')
plt.xlabel('s [m]')
plt.ylabel('v [m/s]')
plt.title('Grafico da velocidade para um certo deslocamento')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(s, a(s), label='a*s', color='blue')
plt.xlabel('s [m]')
plt.ylabel('a [m/s]')
plt.title('Grafico da aceleracao para um certo deslocamento')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
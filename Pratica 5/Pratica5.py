import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

N = 39
r = (1 + N/100)
m = 1
c = 0.5
g = 9.81

def sistema(y, t):
    theta, theta_ponto = y
    dydt = [theta_ponto, (-g*np.sin(theta))/r - (c*theta_ponto)/m]
    return dydt

y0 = [0, 15]

t = np.linspace(0, 100, 1000)

sol = odeint(sistema, y0, t)

plt.figure(figsize=(8,6))
plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.legend(loc='best')
plt.ylabel(r'$\theta$ (rad)')
plt.xlabel('t(s)')
plt.grid()

plt.figure(figsize=(8,6))
plt.plot(t, sol[:, 1], 'b', label='theta(t)')
plt.legend(loc='best')
plt.xlabel('t(s)')
plt.ylabel(r'$\dot{\theta}$ (rad/s)')
plt.grid()

plt.figure(figsize=(8,6))
plt.plot(sol[:,0], sol[:, 1], 'b', label='theta(t)')
plt.legend(loc='best')
plt.ylabel(r'$\dot{\theta}$ (rad/s)')
plt.xlabel(r'$\theta$ (rad)')
plt.grid()

frequencia = sol[:, 1] / (2 * np.pi)

plt.figure(figsize=(8,6))
plt.plot(t, frequencia, 'b', label='theta(t)')
plt.legend(loc='best')
plt.ylabel('f(Hz)')
plt.xlabel('t(s)')
plt.grid()

T = m*g*np.cos(sol[:,0]) + sol[:, 1]**2 * r

plt.figure(figsize=(8,6))
plt.plot(t, T, 'b', label='theta(t)')
plt.legend(loc='best')
plt.ylabel('T(N)')
plt.xlabel('t(s)')
plt.grid()

plt.show()

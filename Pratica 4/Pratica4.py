import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

N = 39

def r(theta):
    return 20 * (3 - 2 * np.cos(theta))

def v(t):
    return 0.05 * (100 + N) * (100 - t)

def theta_ponto(t, theta):
    return v(t) / np.sqrt(1600 * np.sin(theta)**2 + r(theta)**2)

def r_ponto(t, theta):
    return 40 * np.sin(theta) * theta_ponto(t, theta)

theta_initial = 0
t = (0, 100)

sol = solve_ivp(theta_ponto, t, [theta_initial], t_eval=np.linspace(t[0], t[1], 1000))

index = np.abs(sol.y[0] - 6 * np.pi).argmin()
tempo = sol.t[index]

t = (0, tempo)
print(tempo)
sol = solve_ivp(theta_ponto, t, [theta_initial], t_eval=np.linspace(t[0], t[1], 1000))

plt.figure(figsize=(10, 6))
plt.plot(sol.t, sol.y[0], 'b')
plt.xlabel('t (s)')
plt.ylabel(r'$\theta$ (rad)')
plt.title(r'$\theta$ vs t')
plt.grid(True)
plt.show()

val_r = r(sol.y[0])

plt.figure(figsize=(10, 6))
plt.plot(sol.t, val_r, 'b')
plt.xlabel('t (s)')
plt.ylabel(r'$r$ (mm)')
plt.title(r'$r$ vs t')
plt.grid(True)
plt.show()

val_theta_ponto = theta_ponto(sol.t, sol.y[0])

plt.figure(figsize=(10, 6))
plt.plot(sol.t, val_theta_ponto, 'b')
plt.xlabel('t (s)')
plt.ylabel(r'$\dot{\theta}$ (rad/s)')
plt.title(r'$\dot{\theta}$ vs t')
plt.grid(True)
plt.show()

val_r_ponto = r_ponto(sol.t, sol.y[0])

plt.figure(figsize=(10, 6))
plt.plot(sol.t, val_r_ponto, 'b')
plt.xlabel('t (s)')
plt.ylabel(r'$\dot{r}$ (mm/s)')
plt.title(r'$\dot{r}$ vs t')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(sol.y[0], val_r, 'b')
plt.xlabel(r'$\theta$ (rad)')
plt.ylabel(r'$r$ (mm)')
plt.title(r'$r$ vs $\theta$')
plt.grid(True)
plt.show()

val_v = v(sol.t)

plt.figure(figsize=(10, 6))
plt.plot(sol.t, val_v, 'b')
plt.xlabel('t (s)')
plt.ylabel('v (mm/s)')
plt.title('v vs t')
plt.grid(True)
plt.show()

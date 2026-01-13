# Tercera parte del script, aquí generamos los gráficos

import numpy as np
import matplotlib.pyplot as plt # Para graficar

datos = np.load('resultados_qss.npz')
theta = datos['theta']
p = datos['p']
T = datos['T']
h = datos['h']
t= datos['t'] 
M = datos['M']

# ahora graficaremos la densidad de espacio de fase del estado QSS Y la evolución de la magnetización

# Grafico de la densidad del espacio de fase del QSS:
plt.figure(figsize=(6,5))
H, xedges, yedges, im = plt.hist2d(theta, p, bins=100, range=[[-np.pi, np.pi], [-2,2]], cmap='viridis', cmin=1) 
plt.xlabel(r'$\theta$')
plt.ylabel(r'$p$')
plt.title(f'Densidad de espacio de fase (t={T*h:.2f})', fontsize=14)
plt.show()

# Grafico de la magnetización en el transcurso del tiempo:
plt.figure(figsize=(7, 4))
plt.plot(t, M, 'k-', linewidth=2, label=r'$M(t) = \sqrt{M_x^2 + M_y^2}$')
plt.xlabel('Tiempo $t$', fontsize=12)
plt.ylabel(r'$M(t)$', fontsize=12)
plt.title('Magnitud de la magnetización', fontsize=14)
plt.grid(alpha=0.3)
plt.legend()
plt.xlim(0, t[-1])
plt.tight_layout()
plt.show()
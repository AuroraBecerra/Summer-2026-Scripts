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
#plt.figure(figsize=(6,5))
#H, xedges, yedges, im = plt.hist2d(theta, p, bins=100, range=[[-np.pi, np.pi], [-2,2]], cmap='viridis', cmin=1) 
#plt.xlabel(r'$\theta$')
#plt.ylabel(r'$p$')
#plt.title(f'Densidad de espacio de fase (t={T*h:.2f})', fontsize=14)
#plt.show()

# Grafico de la magnetización en el transcurso del tiempo:
#plt.figure(figsize=(7, 4))
#plt.plot(t, M, 'k-', linewidth=2, label=r'$M(t) = \sqrt{M_x^2 + M_y^2}$')
#plt.xlabel('Tiempo $t$', fontsize=12)
#plt.ylabel(r'$M(t)$', fontsize=12)
#plt.title('Magnitud de la magnetización', fontsize=14)
#plt.grid(alpha=0.3)
#plt.legend()
#plt.xlim(0, t[-1])
#plt.tight_layout()
#plt.show()

# Crear figura con 2 subgráficos
fig, axes = plt.subplots(2, 1, figsize=(7, 8))

# --- Subgráfico 1: Densidad de fase ---
H, xedges, yedges = np.histogram2d(theta, p, bins=100, 
                                    range=[[-np.pi, np.pi], [-2, 2]])
im = axes[0].imshow(H.T, origin='lower', aspect='auto', 
                    extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], 
                    cmap='viridis')
axes[0].set_xlabel(r'$\theta$', fontsize=12)
axes[0].set_ylabel(r'$p$', fontsize=12)
axes[0].set_title(f'Densidad de fase (t={T*h:.2f})', fontsize=13)
fig.colorbar(im, ax=axes[0], label='Número de partículas')

# --- Subgráfico 2: Magnetización M(t) ---
axes[1].plot(t, M, 'b-', linewidth=1.5)
axes[1].set_xlabel('Tiempo $t$', fontsize=12)
axes[1].set_ylabel(r'$M(t)$', fontsize=12)
axes[1].set_title('Evolución de magnetización', fontsize=13)
axes[1].grid(alpha=0.3)
axes[1].set_xlim(0, t[-1])

# Ajustar diseño
plt.tight_layout()
plt.show()
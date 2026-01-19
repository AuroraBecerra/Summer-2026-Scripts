# Tercera parte del script, aquí generamos los gráficos

import numpy as np
import matplotlib.pyplot as plt # Para graficar
from matplotlib.animation import FFMpegWriter, FuncAnimation # Para animar
import matplotlib.gridspec as gridspec

datos = np.load('resultados_qss.npz')
theta = datos['theta']
p = datos['p']
T = datos['T']
h = datos['h']
t= datos['t'] 
M = datos['M']
Mx = datos['Mx']
My = datos['My']
theta_s = datos['theta_s']
p_s = datos['p_s']
t_s = datos['t_s']
N_frames = len(t_s) # para la creación del video del espacio de fase

pi = np.pi

# Aquí vamos a redefinir los thetas para que estén dentro del intervalo [-pi,pi]
# Primero se desplaza el ángulo al intervalo [0,2 pi], luego lo volvemos a desplazar el ángulo redefinido a [0,2 pi]
theta = (theta + pi) % (2*pi) - pi
theta_s = (theta_s + pi) % (2*pi) - pi

# ahora graficaremos la densidad de espacio de fase del estado QSS Y la evolución de la magnetización

# Crear figura con 2 gráficos + animación
fig = plt.figure(figsize=(10, 10))
gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1.2], width_ratios=[1, 1])

# Primer gráfico: Densidad de fase final (arriba izquierda)
ax0 = fig.add_subplot(gs[0, 0])
H, xedges, yedges = np.histogram2d(theta, p, bins=50, 
                                    range=[[-np.pi, np.pi], [-2, 2]])
im = ax0.imshow(H.T, origin='lower', aspect='auto', 
                extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], 
                cmap='viridis',vmax=10)
ax0.set_xlabel(r'$\theta$', fontsize=11)
ax0.set_ylabel(r'$p$', fontsize=11)
ax0.set_title(f'Densidad de Espacio de Fase Final (t={T*h:.2f})', fontsize=11)
fig.colorbar(im, ax=ax0, label='N partículas', shrink=0.8)

# Segundo gráfico: Magnetización M(t) (arriba derecha)
ax1 = fig.add_subplot(gs[0, 1])
ax1.plot(t, M,  'b-', linewidth=1.8, label=r'$M(t)$')
ax1.plot(t, Mx, 'r--', linewidth=1.2, label=r'$M_x(t)$', alpha=0.8)
ax1.plot(t, My, 'g-', linewidth=1.2, label=r'$M_y(t)$', alpha=0.8)
ax1.set_xlabel('Tiempo $t$', fontsize=11)
ax1.set_ylabel(r'$M$', fontsize=11)
ax1.set_title('Evolución de Magnetización', fontsize=12)
ax1.grid(alpha=0.3)
ax1.set_xlim(0, t[-1])
ax1.legend(loc='best', fontsize=9, framealpha=0.8)

# Opcional: añadir líneas horizontales en y=0
#ax1.axhline(y=0, color='k', linestyle=':', linewidth=0.5, alpha=0.5)

# Animación (abajo)
ax2 = fig.add_subplot(gs[1, :])
ax2.set_xlim(-np.pi, np.pi)
ax2.set_ylim(-2, 2)
ax2.set_xlabel(r'$\theta$', fontsize=11)
ax2.set_ylabel(r'$p$', fontsize=11)
ax2.set_title('Evolución de Densidad de Espacio de Fase', fontsize=13)

# Crear imagen inicial vacía
H0, xedges, yedges = np.histogram2d(theta_s[0], p_s[0], bins=50, range=[[-np.pi, np.pi], [-2, 2]])
im_anim = ax2.imshow(H0.T, origin='lower', aspect='auto',
                     extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]],
                     cmap='viridis', vmin=0,vmax=10)# vmax=H0.max()*1.2)
cbar = fig.colorbar(im_anim, ax=ax2, label='Densidad')
time_text = ax2.text(0.02, 0.95, '', transform=ax2.transAxes, fontsize=11,
                     verticalalignment='top',
                     bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

# Función de actualización:
def update(frame):
    H, _, _ = np.histogram2d(theta_s[frame], p_s[frame], bins=50,
                             range=[[-np.pi, np.pi], [-2, 2]])
    im_anim.set_data(H.T)
    # Opcional: ajustar escala de colores dinámicamente
    # im_anim.set_clim(vmin=0, vmax=H.max())
    time_text.set_text(f'$t$ = {t_s[frame]:.2f}')
    return im_anim, time_text

ani = FuncAnimation(fig, update, frames=min(N_frames, 300),
                    interval=50, blit=True, repeat=True)

plt.tight_layout()
#ani.save('evolucion_fase_2.gif', writer='pillow', fps=15, dpi=100)
plt.show()
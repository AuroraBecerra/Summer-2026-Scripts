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
theta_s = datos['theta_s']
p_s = datos['p_s']
t_s = datos['t_s']
N_frames = len(t_s) # para la creación del video del espacio de fase

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

# Crear figura con 2 gráficos + animación
fig = plt.figure(figsize=(10, 10))
gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1.2], width_ratios=[1, 1])

# Primer gráfico: Densidad de fase final (arriba izquierda)
ax0 = fig.add_subplot(gs[0, 0])
H, xedges, yedges = np.histogram2d(theta, p, bins=100, 
                                    range=[[-np.pi, np.pi], [-2, 2]])
im = ax0.imshow(H.T, origin='lower', aspect='auto', 
                extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], 
                cmap='viridis')
ax0.set_xlabel(r'$\theta$', fontsize=11)
ax0.set_ylabel(r'$p$', fontsize=11)
ax0.set_title(f'Densidad final (t={T*h:.2f})', fontsize=12)
fig.colorbar(im, ax=ax0, label='N partículas', shrink=0.8)

# Segundo gráfico: Magnetización M(t) (arriba derecha)
ax1 = fig.add_subplot(gs[0, 1])
ax1.plot(t, M, 'b-', linewidth=1.5)
ax1.set_xlabel('Tiempo $t$', fontsize=11)
ax1.set_ylabel(r'$M(t)$', fontsize=11)
ax1.set_title('Evolución de magnetización', fontsize=12)
ax1.grid(alpha=0.3)
ax1.set_xlim(0, t[-1])

# Animación (abajo)
ax2 = fig.add_subplot(gs[1, :])
ax2.set_xlim(-np.pi, np.pi)
ax2.set_ylim(-2, 2)
ax2.set_xlabel(r'$\theta$', fontsize=11)
ax2.set_ylabel(r'$p$', fontsize=11)
ax2.set_title('Evolución de la densidad de fase', fontsize=12)

# Crear imagen inicial vacía
H0, xedges, yedges = np.histogram2d(theta_s[0], p_s[0], bins=50,
                                     range=[[-np.pi, np.pi], [-2, 2]])
im_anim = ax2.imshow(H0.T, origin='lower', aspect='auto',
                     extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]],
                     cmap='viridis', vmin=0, vmax=H0.max()*1.2)
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
plt.show()
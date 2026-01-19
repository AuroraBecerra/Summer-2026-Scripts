# Tercera parte del script, aquí generamos los gráficos

import numpy as np
import matplotlib.pyplot as plt # Para graficar
from matplotlib.patches import Rectangle
import matplotlib.gridspec as gridspec

datos = np.load('resultados_qss.npz')
theta = datos['theta']
p = datos['p']
T = datos['T']
h = datos['h']
t= datos['t'] 
Mx = datos['Mx']
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

# Crear figura con 2 gráficos (por ahora no crearemos animación)
fig = plt.figure(figsize=(12, 6))

# PRIMERO: Gráfico principal de magnetización (ocupa toda la figura)
ax_main = plt.subplot(111)  # Un solo gráfico que ocupa toda la figura

# Gráfico de magnetización como gráfico principal
ax_main.plot(t, Mx, 'black', linewidth=2.0, label=r'$M_x(t)$', alpha=0.8)
ax_main.set_xlabel('Tiempo $t$', fontsize=12)
ax_main.set_ylabel(r'$M_x$', fontsize=12)
ax_main.set_title('Evolución de Magnetización con Densidad de Fase', fontsize=14)
ax_main.grid(alpha=0.3)
ax_main.set_xlim(0, t[-1])

# Ajustar límites de Y para el gráfico principal (0.5 a 0.9 como mencionaste)
ax_main.set_ylim(0.5, 0.9)
ax_main.legend(loc='upper right', fontsize=10, framealpha=0.8)

# SEGUNDO: Crear el gráfico de densidad de fase COMO INSET dentro del gráfico de magnetización
# Definir posición del inset: [left, bottom, width, height] en coordenadas del eje principal
# Ajusta estos valores para posicionar donde quieras

# Opción 1: Inset en la esquina inferior izquierda (centrado horizontalmente, abajo)
left = 0.15    # 15% desde la izquierda del eje principal
bottom = 0.15  # 15% desde abajo del eje principal  
width = 0.3    # 30% del ancho del eje principal
height = 0.3   # 30% del alto del eje principal

ax_inset = fig.add_axes([ax_main.get_position().x0 + left * ax_main.get_position().width,
                         ax_main.get_position().y0 + bottom * ax_main.get_position().height,
                         width * ax_main.get_position().width,
                         height * ax_main.get_position().height])

# Opción 2: O usando coordenadas absolutas (más fácil de ajustar)
# ax_inset = fig.add_axes([0.15, 0.15, 0.3, 0.3])  # [left, bottom, width, height] de la figura completa

# Ahora crear el gráfico de densidad de fase en el inset
H, xedges, yedges = np.histogram2d(theta, p, bins=80, 
                                    range=[[-np.pi, np.pi], [-2, 2]])
im = ax_inset.imshow(H.T, origin='lower', aspect='auto', 
                     extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], 
                     cmap='viridis')

ax_inset.set_xlabel(r'$\theta$', fontsize=9)
ax_inset.set_ylabel(r'$p$', fontsize=9)
ax_inset.set_title(f'Densidad de Fase (t={T*h:.2f})', fontsize=10)

# Agregar colorbar al inset (opcional, más pequeño)
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
cb_inset = inset_axes(ax_inset, 
                      width="5%",  # ancho de la colorbar
                      height="80%", # alto de la colorbar
                      loc='center right',
                      borderpad=0)
plt.colorbar(im, cax=cb_inset, label='Densidad')

# Opcional: agregar un recuadro para destacar el inset
ax_inset.patch.set_edgecolor('black')
ax_inset.patch.set_linewidth(1.5)
ax_inset.patch.set_alpha(0.95)  # fondo ligeramente transparente

plt.tight_layout()
plt.show()
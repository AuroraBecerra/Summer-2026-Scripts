# Tercera parte del script, aquí generamos los gráficos

import numpy as np
import matplotlib.pyplot as plt # Para graficar

datos = np.load('resultados_qss.npz')
theta = datos['theta']
p = datos['p']
T = datos['T']
h = datos['h']

# ahora graficaremos la densidad de espacio de fase del estado QSS:

plt.figure(figsize=(6,5))
H, xedges, yedges, im = plt.hist2d(theta, p, bins=100, range=[[-np.pi, np.pi], [-2,2]], cmap='viridis', cmin=1) 
# H es la matriz 2D del histograma, contiene los (theta,pi)
# La cantidad de bins establece los espacios en los cuales se medirán la cantidad de partículas (el tamaño de la grilla) 
# se usan los límites de \theta entre -\pi y -\pi porque theta es un ángulo y solo puede tomar entre esos dos valores
# cmin hace que se grafique únicamente donde sí hay partícuals, y el resto blanco. 
plt.colorbar(label='Número de partículas')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$p$')
plt.title(f'Densidad de espacio de fase (t={T*h:.2f})', fontsize=14)
plt.show()
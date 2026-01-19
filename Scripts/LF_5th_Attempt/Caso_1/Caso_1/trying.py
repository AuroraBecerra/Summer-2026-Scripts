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
Mx = datos['Mx']
theta_s = datos['theta_s']
p_s = datos['p_s']
t_s = datos['t_s']
N_frames = len(t_s) # para la creación del video del espacio de fase
pi= np.pi
theta_s = (theta_s + pi) % (2*pi) - pi

H, xedges, yedges = np.histogram2d(theta_s[700], p_s[700], bins=80, 
                                    range=[[-np.pi, np.pi], [-2, 2]])

print(f"Histograma H - forma: {H.shape}")
print(f"Histograma H - valor mínimo: {H.min()}")
print(f"Histograma H - valor máximo: {H.max()}")
print(f"Histograma H - suma total: {H.sum()} (debería ser ~8100)")
print(f"Histograma H - número de celdas no vacías: {(H > 0).sum()}")

# Si la suma no es ~8100, los datos podrían estar fuera del rango
print(f"\ntheta_s[700] - min: {theta_s[700].min():.2f}, max: {theta_s[700].max():.2f}")
print(f"p_s[700] - min: {p_s[700].min():.2f}, max: {p_s[700].max():.2f}")

# Verifica si los datos están en el rango esperado
theta_in_range = np.sum((theta_s[700] >= -np.pi) & (theta_s[700] <= np.pi))
p_in_range = np.sum((p_s[700] >= -2) & (p_s[700] <= 2))
print(f"\nPartículas con theta en [-π, π]: {theta_in_range}/{len(theta_s[700])}")
print(f"Partículas con p en [-2, 2]: {p_in_range}/{len(p_s[700])}")
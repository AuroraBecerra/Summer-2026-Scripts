# Segundo script, donde se ejecuta el ciclo de Leapfrog

from tqdm import trange 
from numba import njit
import numpy as np
import time
from S1 import N, theta, p, a 

# En los pasos de tiempo solo haremos lo suficiente para llegar a t = 650
T = 70000 # 2 **17 #131072 # definimos primero los pasos temporales
h = 0.01 # longitud temporal entre cada paso (igual que en el paper)

# Ahora vamos a no incluir M_y en los códigos, pues este es nulo en todo t, y como entonces |M_x| = M para todo t, tampoco incluiremos M, pues hay suficiente información en M_x, y así reduciremos costos computacionales 

# Ya no guardaremos snapshots (no haremos simulación)
# save_every = 100  # Guardar cada 100 pasos (cada 1 unidad de tiempo, dado h=0.01)

# Agregamos listas para guardar las componentes de magnetización
Mx_list = []
t_list = []

save_every = 100  # Vamos a guardar cada 100 pasos (cada 1 unidad de tiempo, dado h=0.01) el M_x, para no usar mucho RAM

# Guardaremos solo el snapshot t = 650 de theta y p para graficar la densidad del espacio de fase del QSS
theta_650 = None
p_650 = None
t_650 = None

#Definimos ac como la aceleración y Mx como la componente x de magnetización
ac, M_x = a(theta) # Aquí se calculan la ac y M_x de las condiciones iniciales
@njit
def numba(theta, p, T, h, save_every):
    # Guardamos los datos de magnetización en las 
    for t in range(T):
        if t % save_every == 0: # t = 1, 2, ...
            t_list.append(t*h)
            Mx_list.append(M_x)
        if t_650 is None and (t*h) >= 650: # Aquí solo guardaremos el snapshot t = 650
            theta_650 = theta
            p_650 = p
            t_650 = t*h
        # Leapfrog
        p_m = p + (h/2)*ac
        theta = theta + h*p_m
        ac, M_x = a(theta)
        p = p_m + (h/2) * ac

# Queda guardado el valor final de theta y p

#Convertimos las listas en arrays: 
Mx_array = np.array(Mx_list)
t_array = np.array(t_list)

theta_s = np.array(theta_650) 
p_s = np.array(p_650)

# np.savez('resultados_qss.npz', theta=theta, p=p, N=N, T=T, h=h, t=t_array, Mx = Mx_array , theta_s = theta_s, p_s= p_s, t_s=t_s)
np.savez('resultados_qss.npz', N=N, T=T, h=h, t=t_array, Mx = Mx_array , theta_s = theta_s, p_s= p_s)

# Con N = 1000 y T = 10000 el script se ejecuta en \approx 1s (5538.56 its/s)
# Con N = 100000 y T = 100000 el script se ejecuta en \approx 20s (4772.90 its/s)
# Con N = 100000 y T = 70000 el script se ejecuta en \approx 18s (3808.05 its/s)

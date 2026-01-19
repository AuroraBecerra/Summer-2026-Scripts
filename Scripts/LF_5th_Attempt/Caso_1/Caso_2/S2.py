# Segundo script, donde se ejecuta el ciclo de Leapfrog

from tqdm import trange 
import numpy as np
from S1 import N, theta, p, a 

T = 10000 # definimos primero los pasos temporales
h = 0.01 # longitud temporal entre cada paso (igual que en el paper)

# Ahora vamos a no incluir M_y en los códigos, pues este es nulo en todo t, y como entonces |M_x| = M para todo t, tampoco incluiremos M, pues hay suficiente información en M_x, y así reduciremos costos computacionales 
save_every = 100  # Guardar cada 100 pasos (cada 1 unidad de tiempo, dado h=0.01)

# Agregamos listas para guardar las componentes de magnetización
Mx_list = []
t_list = []

# Listas para los snapshots:
theta_list = [] 
p_list = []
times = []

#Definimos ac como la aceleración, M como la magnetización, y M_x y M_y como las respectivas componentes de magnetización
ac, M_x = a(theta) # Aquí se calculan la ac y M_x de las condiciones iniciales
for t in trange(T):
    #Guardamos los datos en las listas
    t_list.append(t*h)
    Mx_list.append(M_x) 
    if t % save_every == 0: # % es la operpación módulo, devuelve el resto de la división, aquí guarda los t = 1, 2, ...
        theta_list.append(theta)  
        p_list.append(p)
        times.append(t*h)
    # Ciclo
    p_m = p + (h/2)*ac # velocidad a medio tiempo, se usa la aceleración y t iniciales
    theta = theta + h*p_m # spin a tiempo entero (se actualiza theta)
    ac, M_x, = a(theta) 
    p = p_m + (h/2)*ac # velocidad a tiempo entero
    # Aquí ya están actualizados theta y p a tiempo entero, y se vuelve a correr el ciclo.

# Nota: Usar np.savez(f'{t}.npz', theta=theta, p=p, Mx=Mx, My=My) dentro del ciclo resulta muy ineficiente
 
#Convertimos las listas en arrays: 
Mx_array = np.array(Mx_list)
t_array = np.array(t_list)

theta_array = np.array(theta_list) 
p_array = np.array(p_list)
times_array = np.array(times)

# Incluímos los resultados de magnetizacion en cada iteración del ciclo en el archivo final que queremos guardar
np.savez('resultados_qss.npz', theta=theta, p=p, N=N, T=T, h=h, t=t_array, Mx = Mx_array , theta_s = theta_array, p_s= p_array, t_s=times_array)

# Con N = 1000 y T = 10000 el script se ejecuta en \approx 1s (5538.56 its/s)
# Con N = 100000 y T = 100000 el script se ejecuta en \approx 20s (4772.90 its/s)
# Con N = 100000 y T = 70000 el script se ejecuta en \approx 18s (3808.05 its/s)

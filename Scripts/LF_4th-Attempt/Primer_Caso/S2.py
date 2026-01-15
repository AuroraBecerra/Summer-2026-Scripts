# Segundo script, donde se ejecuta el ciclo de Leapfrog

from tqdm import trange 
import numpy as np
from S1 import N, theta, p, a 

T = 10000 # definimos primero los pasos temporales
h = 0.01 # longitud temporal entre cada paso (igual que en el paper)

# Ahora vamos a agregar el código para guardar snapshots de (t, theta, p) a través del ciclo LF, para luego crear una visualización de la evolución temporal del espacio de fases.
save_every = 100  # Guardar cada 100 pasos (cada 1 unidad de tiempo, dado h=0.01)

# Agregamos listas para guardar las componentes de magnetización
M_list = []
Mx_list = []
My_list = []
t_list = []

# Listas para los snapshots:
theta_list = [] 
p_list = []
times = []

#Definimos ac como la aceleración, M como la magnetización, y M_x y M_y como las respectivas componentes de magnetización
ac, M, M_x, M_y = a(theta) # Aquí se calculan la ac, el módulo de M y sus componentes de los parámetros iniciales.

# Realizamos el ciclo:
for t in trange(T):
    #Guardamos los datos en las listas
    M_list.append(M)
    Mx_list.append(M_x) # Guardamos también los datos de las componentes de magnetización (que se irán actualizando)
    My_list.append(M_y)
    t_list.append(t*h)
    # Guardamos los snapshots: 
    if t % save_every == 0: # % es la operpación módulo, devuelve el resto de la división, aquí guarda los t = 1, 2, ...
        theta_list.append(theta)  
        p_list.append(p)
        times.append(t*h)
    # Ciclo
    p_m = p + (h/2)*ac # velocidad a medio tiempo, se usa la aceleración y t iniciales
    theta = theta + h*p_m # spin a tiempo entero (se actualiza theta)
    ac, M, M_x, M_y = a(theta) # Definimos las nuevas aceleraciones y magnetizaciones con theta actualizado a tiempo entero, en esta nueva versión también debemos definir de nuevo M_x y M_y para el siguiente tiempo
    p = p_m + (h/2)*ac # velocidad a tiempo entero
    # Aquí ya están actualizados theta y p a tiempo entero, y se vuelve a correr el ciclo.

# Nota: Usar np.savez(f'{t}.npz', theta=theta, p=p, Mx=Mx, My=My) dentro del ciclo resulta muy ineficiente
 
#Convertimos las listas en arrays: 
M_array = np.array(M_list)
Mx_array = np.array(Mx_list)
My_array = np.array(My_list)
t_array = np.array(t_list)

theta_array = np.array(theta_list) 
p_array = np.array(p_list)
times_array = np.array(times)

# Incluímos los resultados de magnetizacion en cada iteración del ciclo en el archivo final que queremos guardar
np.savez('resultados_qss.npz', theta=theta, p=p, N=N, T=T, h=h, t=t_array, M = M_array, Mx = Mx_array , My = My_array , theta_s = theta_array, p_s= p_array, t_s=times_array)

# Con N = 1000 y T = 10000 el script se ejecuta en \approx 1s (5538.56 its/s)
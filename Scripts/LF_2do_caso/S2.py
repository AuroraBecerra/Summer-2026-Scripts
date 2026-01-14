# Segundo script, donde se ejecuta el ciclo de Leapfrog

# Aquí es imperativo que modifiquemos el ciclo para que en cada iteración se guarden los datos de magnetización para así lograr crear su gráfico en el tiempo

import numpy as np

from S1 import N, theta, p, a

T = 50000 # definimos primero los pasos temporales
h = 0.01 # longitud temporal entre cada paso (igual que en el paper)

# Ahora vamos a agregar el código para guardar snapshots de (t, theta, p) a través del ciclo LF, para luego crear una visualización de la evolución temporal del espacio de fases.
save_every = 100  # Guardar cada 100 pasos (cada 1 unidad de tiempo, dado h=0.01)

# Como primero intento, solo usaremos listas
M_list = []
t_list = []

# Listas para los snapshots:
theta_list = [] 
p_list = []
times = []

# Realizamos el ciclo:
for t in range(T):
    ac, M = a(theta) #Definimos ac como la aceleración y M como la magnetización
    #Guardamos los datos en las listas
    M_list.append(M)
    t_list.append(t * h)
    # Guardamos los snapshots: 
    if t % save_every == 0: # % es la operpación módulo, devuelve el resto de la división 
        theta_list.append(theta.copy())  # El .copy() es una recomendación de Deepseek aunque no veo que sea necesario
        p_list.append(p.copy())
        times.append(t * h)
    # Ciclo
    p_m = p + (h/2)*ac # velocidad a medio tiempo 
    theta = theta + h*p_m # spin a tiempo entero 
    p = p_m + (h/2)*ac # velocidad a tiempo entero

# Nota: Usar np.savez(f'{t}.npz', theta=theta, p=p, Mx=Mx, My=My) dentro del ciclo resulta muy ineficiente
 
#Convertimos las listas en arrays: 
M_array = np.array(M_list)
t_array = np.array(t_list)


theta_array = np.array(theta_list) 
p_array = np.array(p_list)
times_array = np.array(times)

# Incluímos los resultados de magnetizacion en cada iteración del ciclo en el archivo final que queremos guardar
np.savez('resultados_qss.npz', theta=theta, p=p, N=N, T=T, h=h, t=t_array, M=M_array, theta_s= theta_array, p_s= p_array, t_s=times_array)

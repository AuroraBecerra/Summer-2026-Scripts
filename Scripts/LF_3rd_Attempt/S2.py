# Segundo script, donde se ejecuta el ciclo de Leapfrog

# Aquí es imperativo que modifiquemos el ciclo para que en cada iteración se guarden los datos de magnetización para así lograr crear su gráfico en el tiempo

import numpy as np

from S1 import N, theta, p, a

T = 1000 # definimos primero los pasos temporales
h = 0.01 # longitud temporal entre cada paso (igual que en el paper)

# Como primero intento, solo usaremos listas
M_list = []
t_list = []

# Realizamos el ciclo:
for t in range(T):
    ac, M = a(theta) #Definimos ac como la aceleración y M como la magnetización
    #Guardamos los datos en las listas
    M_list.append(M)
    t_list.append(t * h)
    # Ciclo
    p_m = p + (h/2)*ac # velocidad a medio tiempo 
    theta = theta + h*p_m # spin a tiempo entero 
    p = p_m + (h/2)*ac # velocidad a tiempo entero

# Nota: Usar np.savez(f'{t}.npz', theta=theta, p=p, Mx=Mx, My=My) resulta muy ineficiente
 
#Convertimos las listas en arrays: 
M_array = np.array(M_list)
t_array = np.array(t_list)

# Incluímos los resultados de magnetizacion en cada iteración del ciclo en el archivo final que queremos guardar
np.savez('resultados_qss.npz', theta=theta, p=p, N=N, T=T, h=h, t=t_array, M=M_array)

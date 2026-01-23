# Segundo script, donde se ejecuta el ciclo de Leapfrog

from tqdm import trange 
from numba import njit
import numpy as np
import time
from S1 import N, theta, p, a 

# Parámetros
T = 65000 # En los pasos de tiempo solo haremos lo suficiente para llegar a t = 650
h = 0.01 # longitud temporal entre cada paso (igual que en el paper)
save_every = 100 # Guardaremos datos de magnetización cada t = 1, 2, 3 ...

# Creamos una simulación compilada con numba
# Todos los datos deben guardarse dentro del ciclo
@njit
def numba(theta, p, T, h, save_every):
    """
    Devuelve: t_array, Mx_array, theta, p, t
    """
    # Pre-asignamos espacio (vacío) para los arrays
    n_saves = T // save_every + 1 # 651 espacios
    t_array = np.zeros(n_saves)
    Mx_array = np.zeros(n_saves)
    
    # Calculamos los datos de aceleración y magnetización iniciales
    ac, M_x = a(theta)
    save_idx = 0
    
    # Ciclo
    for t in range(T):
        t_real = t * h
        
        # Guardamos los datos de magnetización en los arrays
        if t % save_every == 0: # t_real = 1, 2, ...
            t_array[save_idx]= t_real # Guardamos en la posición save_idx de los respectivos arrays
            Mx_array[save_idx]= M_x
            save_idx += 1 # Pasamos a la siguiente posición en el indicador save_idx (+1)
    
        # Leapfrog
        p_m = p + (h/2)*ac # velocidad a medio tiempo
        theta = theta + h*p_m # posición a medio tiempo
        ac, M_x = a(theta) # calculamos las nuevas aceleraciones y magnetización, dado el dato de la posición a tiempo entero
        p = p_m + (h/2) * ac # velocidad a tiempo entero
        # Se guardan los valores finales de theta y p
    
    return t_array[:save_idx], Mx_array[:save_idx], theta, p

# Método para medir el tiempo (ya que al usar numba ya no tenemos trange )
print("Iniciando simulación con Numba...")
start_time = time.time()

# Ejecutamos la simulación compilada
t_array, Mx_array, theta, p = numba(theta, p, T, h, save_every)

# Medimos el tiempo elapsado en que se ejecute la sumulación
elapsed = time.time() - start_time

# Guardamos los resultados
np.savez('resultados_qss.npz', N=N, T=T, h=h, t = t_array, Mx = Mx_array, theta = theta, p = p)

# Extras
print(f"\n✓ Simulación completada en {elapsed:.1f} segundos")
print(f"✓ Velocidad: {T/elapsed:.0f} iteraciones/segundo")
print(f"✓ Puntos guardados: {len(t_array)}")
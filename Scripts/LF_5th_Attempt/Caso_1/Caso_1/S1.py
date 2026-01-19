# El enfoque de este nuevo intento es ahora trivializar el hecho de que M_y = 0 para todo t, dadas las demostraciones realizadas en tarea y con el profesor
# También, asemejar las figuras y sus formatos a aquellos del paper
# Primer script donde definimos parámetros iniciales y la función aceleración:

# Vamos a usar numba para ver si corre más rápido el código
 
import numpy as np
from numba import njit
import time 

N = 1000000 #1000000
theta_0 = 1.131 
p_0 = 1.39 
#p_0 = 1

# Ahora vamos a usar una distribución inicial random para asimilar los resultados del paper
theta = np.random.uniform(-theta_0, theta_0, N) 
p = np.random.uniform(-p_0, p_0,N) 

#theta = np.linspace(-theta_0, theta_0, N) 
#p = np.linspace(-p_0, p_0,N) 

# theta, p = np.mgrid[-theta_0:theta_0:90j,-p_0:p_0:90j]
# theta= theta.flatten()
# p =p.flatten()

# Aquí haremos que en términos de magnetización solo se devuelva M_x, y quitaremos M_y (pues este es nulo) y M para reducir costos computacionales
@njit # Numba
def a(theta_i): 
    sinth = np.sin(theta_i)
    costh = np.cos(theta_i)
    M_x = np.mean(costh) 
    a = -M_x*sinth
    return a, M_x

# En este script solo definimos funciones y parámetros, si los llamamos en otro script, no es necesario ejecutar este script (solo guardarlo)
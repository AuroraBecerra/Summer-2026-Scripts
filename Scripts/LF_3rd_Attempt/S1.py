# Este es la tercera versión 
# Aquí nos enfocaremos en realizar la tarea 2 del código: crear el gráfico de M vs t

# Primer script donde definimos parámetros iniciales y la función aceleración:

import numpy as np
N = 1000
theta_0 = 1.131 
p_0 = 1.39 

#theta = np.random.uniform(-theta_0, theta_0, N) 

#theta = np.linspace(-theta_0, theta_0, N) 
#p = np.linspace(-p_0, p_0,N) 

theta, p = np.mgrid[-theta_0:theta_0:90j,-p_0:p_0:90j]
theta= theta.flatten()
p =p.flatten()

# Aquí vamos a modificar un poco la función de como la teníamos antes
def a(theta_i): 
    sinth = np.sin(theta_i)
    costh = np.cos(theta_i)
    M_x = np.mean(costh) 
    M_y = np.mean(sinth) 
    #M = (M_x**2 + M_y**2)**0.5
    M = np.hypot(M_x, M_y)
    a = -M_x*sinth + M_y*costh
    return a, M
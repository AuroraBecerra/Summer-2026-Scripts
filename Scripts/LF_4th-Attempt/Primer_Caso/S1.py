# El enfoque de este nuevo intento es ahora incluir los gráficos de las componentes de magnetización junto con su magnitud

# Primer script donde definimos parámetros iniciales y la función aceleración:

import numpy as np
N = 10000
theta_0 = 1.131 
p_0 = 1.39 

#theta = np.random.uniform(-theta_0, theta_0, N) 

#theta = np.linspace(-theta_0, theta_0, N) 
#p = np.linspace(-p_0, p_0,N) 

theta, p = np.mgrid[-theta_0:theta_0:90j,-p_0:p_0:90j]
theta= theta.flatten()
p =p.flatten()

# Aquí vamos a modificar un poco la función para que retorne la aceleración, la magnitud de magnetizaión y las componentes de magnetización
# El profesor recomendó definir los senos y cosenos directamente en la función para luego usar esos resultados, y no repetir cálculos
def a(theta_i): 
    sinth = np.sin(theta_i)
    costh = np.cos(theta_i)
    M_x = np.mean(costh) 
    M_y = np.mean(sinth) 
    #M = (M_x**2 + M_y**2)**0.5
    M = np.hypot(M_x, M_y)
    a = -M_x*sinth + M_y*costh
    return a, M, M_x, M_y

# En este script solo definimos funciones y parámetros, si los llamamos en otro script, no es necesario ejecutar este script (solo guardarlo)
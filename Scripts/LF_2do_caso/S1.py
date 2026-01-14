# Este es el método LF para el segundo caso (no magnetizado)

# Primer script donde definimos parámetros iniciales y la función aceleración:
# Aquí se modifican las condiciones iniciales respecto al caso anterior, seguiremos los mismos parámetros del paper
# El número de partículas y los pasos de tiempo seguirán siendo los mismos por temas de eficiencia

import numpy as np
N = 10000
theta_0 = 1.131 # Me parece que este valor sigue igual
p_0 = 1.90 # Este es diferente

#theta = np.random.uniform(-theta_0, theta_0, N) 

#theta = np.linspace(-theta_0, theta_0, N) 
#p = np.linspace(-p_0, p_0,N) 

theta, p = np.mgrid[-theta_0:theta_0:90j,-p_0:p_0:90j]
theta= theta.flatten()
p =p.flatten()

# Aquí vamos a modificar un poco la función de como la teníamos antes
def a(theta_i): 
    M_x = np.mean(np.cos(theta_i)) 
    M_y = np.mean(np.sin(theta_i)) 
    M = (M_x**2 + M_y**2)**0.5
    a = -M_x*np.sin(theta_i) + M_y*np.cos(theta_i) 
    return a, M
# Este es la segunda versión de la primera tarea en código tras la revisión del profesor.
# También, aquí dividiremos el código en varios scripts para que el computador no deba realizar un mismo proceso cada vez que ejecutamos el código.

# En esta versión, tenemos la opción de crear los parámetros iniciales uniformados mediante np.mgrid

import numpy as np # Biblioteca siempre relevante.
import matplotlib.pyplot as plt # Para graficar

# Primero debemos establecer las condiciones iniciales de los parámetros \theta y p, 
# consideraremos N = 10000 partículas:
N = 500

# El paper menciona que la distribución inicial de la densidad de espacio de fase es de tipo waterbag o steplike. En particular:
theta_0 = 1.131 # valor tope de la distribución en \theta, entre 0 y \pi
p_0 = 1.39 # valor tope de la distribución en p (uno de los ejemplos),

# tal que

#theta = np.random.uniform(-theta_0, theta_0, N) # aquí generamos un array de N valores de \theta diferentes (distribución uniforme) dada la cota \theta_0.
#p = np.random.uniform(-p_0, p_0,N) # análogo a lo anterior pero con p.

#theta = np.linspace(-theta_0, theta_0, N) # aquí generamos un array de N valores de \theta diferentes (distribución uniforme) dada la cota \theta_0.
#p = np.linspace(-p_0, p_0,N) # análogo a lo anterior pero con p.

theta, p = np.mgrid[-theta_0:theta_0:90j,-p_0:p_0:90j]
theta= theta.flatten()
p =p.flatten()

# Ahora definamos la Aceleración (muy importante para el método Leapfrog):
def a(theta_i): # esta corresponde a \ddot{\theta}
    # Primero las magnetizaciones iniciales:
    # en lugar de utilizar una sumatoria como en (3), calcularemos los promedios de las funciones, que representan prácticamente lo mismo que en las ecuaciones
    M_x = np.mean(np.cos(theta_i)) 
    M_y = np.mean(np.sin(theta_i)) # estas son listas al igaul que \theta
    return -M_x*np.sin(theta_i) + M_y*np.cos(theta_i) # función aceleración
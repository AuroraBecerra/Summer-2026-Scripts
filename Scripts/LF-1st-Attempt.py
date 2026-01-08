# Este es el primer script de Python (.py) creado para inicializar el parendizaje de enero 2026 mediante el paper PEFTCOTHMFM.
# En este script tenemos como tarea escribir y ejecutar un código acorde con el algoritmo Leapfrog para resolver las ecuaciones de movimiento (ecuaciones diferenciales) (2) mostradas en el paper.

import numpy as np # Biblioteca siempre relevante.

# Primero debemos establecer las condiciones iniciales de los parámetros \theta y p, 
# consideraremos N = 1000 partículas:
N= 1000

# El paper menciona que la distribución inicial de la densidad de espacio de fase es de tipo waterbag o steplike. En particular:
theta_0 = 1.131 # valor tope de la distribución en \theta, entre 0 y \pi
p_0 = 1.39 # valor tope de la distribución en p (uno de los ejemplos),

# tal que

theta = np.random.uniform(-theta_0, theta_0, N) # aquí generamos un array de N valores de \theta diferentes (distribución uniforme) dada la cota \theta_0.
p = np.random.uniform(-p_0, p_0,N) # análogo a lo anterior pero con p.

# Ahora calculamos las magnetizaciones iniciales:
# en lugar de utilizar una sumatoria como en (3), calcularemos los promedios de las funciones, que representan prácticamente lo mismo que en las ecuaciones
M_x = np.mean(np.cos(theta)) # estas son listas al igaul que \theta
M_y = np.mean(np.sin(theta))

# Este es el primer script de Python (.py) creado para inicializar el parendizaje de enero 2026 mediante el paper PEFTCOTHMFM.
# En este script tenemos como tarea escribir y ejecutar un código acorde con el algoritmo Leapfrog para resolver las ecuaciones de movimiento (ecuaciones diferenciales) (2) mostradas en el paper.

import numpy as np # Biblioteca siempre relevante.
import matplotlib.pyplot as plt # Para graficar

# Primero debemos establecer las condiciones iniciales de los parámetros \theta y p, 
# consideraremos N = 10000 partículas:
N= 10000

# El paper menciona que la distribución inicial de la densidad de espacio de fase es de tipo waterbag o steplike. En particular:
theta_0 = 1.131 # valor tope de la distribución en \theta, entre 0 y \pi
p_0 = 1.39 # valor tope de la distribución en p (uno de los ejemplos),

# tal que

theta = np.random.uniform(-theta_0, theta_0, N) # aquí generamos un array de N valores de \theta diferentes (distribución uniforme) dada la cota \theta_0.
p = np.random.uniform(-p_0, p_0,N) # análogo a lo anterior pero con p.

# Ahora definamos la Aceleración (muy importante para el método Leapfrog):
def a(theta_i): # esta corresponde a \ddot{\theta}
    # Primero las magnetizaciones iniciales:
    # en lugar de utilizar una sumatoria como en (3), calcularemos los promedios de las funciones, que representan prácticamente lo mismo que en las ecuaciones
    M_x = np.mean(np.cos(theta_i)) 
    M_y = np.mean(np.sin(theta_i)) # estas son listas al igaul que \theta
    return -M_x*np.sin(theta_i) + M_y*np.cos(theta_i) # función aceleración

# Ahora iniciaremos el método leapfrog

T = 50000 # definimos primero los pasos temporales
h = 0.01 # longitud temporal entre cada paso (igual que en el paper)

# Realizamos el ciclo:
for t in range(T):
    p_m = p + (h/2)*a(theta) # calculamos la velocidad a medio tiempo dadas las condiciones iniciales,
    theta = theta + h*p_m # se calcula el spin que queremos (primer paso), con la ayuda de la velocidad a tiempo medio anterior,
    p = p_m + (h/2)*a(theta) # calculamos la velocidad a tiempo entero con la posicion en el mismo tiempo calculada en el paso anterior y la velocidad a tiempo medio
    # luego se repite el ciclo con los spins y velocidades actualizadas para obtener los valores del siguiente paso.

# Al finalizar el ciclo, tenemos los valores de \theta y p para el último paso de tiempo, asumiremos que este es el momento en el que el estado es QSS
# ahora graficaremos la densidad de espacio de fase del estado QSS:

plt.figure(figsize=(10,5))
plt.hist2d(theta, p, bins=50, range=[[-50,50], [p.min(), p.max()]], cmap='hot')
plt.colorbar(label='Número de partículas')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$p$')
plt.title(f'Densidad de espacio de fase en t={T*h:.2f}', fontsize=14)
plt.show()
# Aquí va la segunda parte del script original, donde se ejecuta el ciclo de Leapfrog

# Primero, debemos importar los parámetros del script anterior

from LF-2nd-Attempt-S1.py import theta, p, a

T = 1000 # definimos primero los pasos temporales
h = 0.01 # longitud temporal entre cada paso (igual que en el paper)

# Realizamos el ciclo:
for t in range(T):
    p_m = p + (h/2)*a(theta) # calculamos la velocidad a medio tiempo dadas las condiciones iniciales,
    theta = theta + h*p_m # se calcula el spin que queremos (primer paso), con la ayuda de la velocidad a tiempo medio anterior,
    p = p_m + (h/2)*a(theta) # calculamos la velocidad a tiempo entero con la posicion en el mismo tiempo calculada en el paso anterior y la velocidad a tiempo medio
    # luego se repite el ciclo con los spins y velocidades actualizadas para obtener los valores del siguiente paso.

# Al finalizar el ciclo, tenemos los valores de \theta y p para el último paso de tiempo, asumiremos que este es el momento en el que el estado es QSS
# Guardamos estos valores para el siguiente script:
# Al final del primer script:
np.savez('resultados_qss.npz', theta=theta, p=p, N=N, T=T, h=h)

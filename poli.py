import hilbert
import aleatorio  # estrategia de prueba

# El algoritmo pretende poligonizar un conjunto de puntos mediante la curva de
# hilbert (o peano, mas adelante)


def poligonizar(puntos, alg=hilbert):
    '''dada una lista de puntos, poligonizarla segun una curva de alg (por
    defecto hilbert)'''
    alg.Region(puntos)  # generamos el arbol de regiones segun el algoritmo


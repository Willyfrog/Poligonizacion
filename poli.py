import hilbert
import aleatorio  # estrategia de prueba

# El algoritmo pretende poligonizar un conjunto de puntos mediante la curva de
# hilbert (o peano, mas adelante)


def poligonizar(puntos, reg=hilbert.RegionHilbert):
    '''dada una lista de puntos, poligonizarla segun una curva de alg (por
    defecto hilbert)'''
    r = reg(puntos, (0, 0))  # generamos el arbol de regiones

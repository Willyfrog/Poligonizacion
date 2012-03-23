from random import randrange
import poli
import aleatorio


def dame_puntos(max_x=800, max_y=600):
    '''generador de puntos aleatorios'''
    while True:
        yield (randrange(max_x), randrange(max_y))


def genera_lista_puntos(n=100):
    '''genera una lista de n puntos aleatorios'''
    dp = dame_puntos()
    return [dp.next() for i in range(0, n)]

if __name__ == "__main__":
    l = genera_lista_puntos()
    print "hemos generado %d puntos" % len(l)
    #arbol = poli.poligonizar(l, aleatorio.RegionAleatoria)
    arbol = aleatorio.RegionAleatoria(l, (0, 0))
    arbol.mostrar()

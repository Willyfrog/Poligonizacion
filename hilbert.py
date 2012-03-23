# Modulo para utilizar el algoritmo mediante
# la curva de Hilbert
# Numero de divisiones a realizar por region
import region

DIVISION = 4


class Rectangulo(object):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def contenido(self, x, y):
        return x >= self.x1 and x < self.x2 and y >= self.y1 and y < self.y2


class RegionHilbert(region.Region):
    '''implementacion de la region'''
    def dividir(self):
        x2 = self.x + self.ancho / 2
        y2 = self.y + self.largo / 2
        x3 = self.x + self.ancho
        y3 = self.y + self.largo

        print "los calculos son %d, %d, %d %d" % (x2, x3, y2, y3)
        cuads = [
                Rectangulo(self.x, self.y, x2, y2),
                Rectangulo(self.x, y2, x2, y3),
                Rectangulo(x2, self.y, x3, y2),
                Rectangulo(x2, y2, x3, y3)
                ]
        dist = [[], [], [], []]
        for (px, py) in self.pts:
            if cuads[0].contenido(px, py):
                dist[0] += [(px, py)]
            if cuads[1].contenido(px, py):
                dist[1] += [(px, py)]
            if cuads[2].contenido(px, py):
                dist[2] += [(px, py)]
            if cuads[3].contenido(px, py):
                dist[3] += [(px, py)]
        todos = True
        print dist
        reduce(lambda x, y: x and len(y) > 0, dist, todos)
        if todos:
            self.hijos = [
                RegionHilbert(dist[0], self.largo / 2, self.ancho / 2, self.x,
                    self.y),
                RegionHilbert(dist[1], self.largo / 2, self.ancho / 2, self.x,
                    y2),
                RegionHilbert(dist[2], self.largo / 2, self.ancho / 2, x2,
                    self.y),
                RegionHilbert(dist[3], self.largo / 2, self.ancho / 2, x2, y2),
                ]

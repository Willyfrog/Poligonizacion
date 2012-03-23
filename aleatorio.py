from region import Region
import random

DIVISION = 2


class RegionAleatoria(Region):
    '''implementacion de la region, divide los puntos aleatoriamente entre las
    regiones'''

    def __init__(self, puntos, centro):
        self.hijos = []
        super(RegionAleatoria, self).__init__(puntos, centro)

    def dividir(self):
        '''divide los putnos d emanera aleatoria entre las regiones'''
        listas = [[], []]
        for i in self.pts:
            listas[random.randint(0, 1)] += [i]
        self.hijos = [RegionAleatoria(listas[0], (0, 0)),
                RegionAleatoria(listas[1], (0, 0))]


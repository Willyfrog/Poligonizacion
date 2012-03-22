

class Region:
    '''Nodo de arbol de regiones'''
    def __init__(self, puntos, centro):
        '''crea una region'''
        self.pts = puntos
        self.centro = centro
        self.hijos = None
        if len(puntos) > 1:
            self.dividir()
        else:
            self.seleccionar

    def dividir(self):
        pass

    def seleccionar(self):
        '''elige el punto o pone el centro si fuera vacio'''
        if self.pts and self.pts[0]:
            self.sel = self.pts[0]
        else:
            self.sel = centro



class Region(object):
    '''Nodo de arbol de regiones'''
    def __init__(self, puntos, largo, ancho, x, y):
        '''crea una region'''
        self.pts = puntos
        self.largo = largo
        self.ancho = ancho
        self.x = x
        self.y = y
        self.hijos = None
        if len(puntos) > 1:
            self.dividir()

    def __repr__(self):
        return '<Origen %r, Puntos %r>' % ((self.x, self.y), self.pts)

    def mostrar(self):
        print "%r" % self
        if self.hijos:
            for h in self.hijos:
                h.mostrar()

    def dividir(self):
        raise NotImplementedError  # las subclases deberan implementarlas


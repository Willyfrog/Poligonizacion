

class Region(object):
    '''Nodo de arbol de regiones'''
    def __init__(self, puntos, centro):
        '''crea una region'''
        self.pts = puntos
        self.centro = centro
        self.hijos = None
        self.sel = None
        if len(puntos) > 1:
            self.dividir()
        else:
            self.seleccionar()

    def __repr__(self):
        return '<Centro %r, Puntos %r>' % (self.sel, self.pts)

    def mostrar(self):
        print "%r" % self
        if self.hijos:
            for h in self.hijos:
                h.mostrar()

    def dividir(self):
        raise NotImplementedError  # las subclases deberan implementarlas

    def seleccionar(self):
        '''elige el punto o pone el centro si fuera vacio'''
        if self.pts and self.pts[0]:
            self.sel = self.pts[0]
        else:
            self.sel = self.centro

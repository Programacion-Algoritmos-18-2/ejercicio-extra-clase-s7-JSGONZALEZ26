class ordenamientoSeleccion(object):

    def __init__(self, valores):  # Constructor
        self.datos = valores

    def ordenar(self):  # Proceso para organizar los datos
        masPequenio = 0
        for i in range(len(self.datos)-1):
            masPequenio = i
            indice = i + 1
            while(indice < len(self.datos)):
                if (self.datos[indice] < self.datos[masPequenio]):
                    masPequenio = indice
                indice = indice+1
            self.intercambiar(i, masPequenio)
            print(self.__str__())

    def intercambiar(self, primero, segundo):  # Intercambio de la posición de los datos
        temporal = self.datos[primero]
        self.datos[primero] = self.datos[segundo]
        self.datos[segundo] = temporal

    def __str__(self):  # Sobreescritura del metodo toString
        temp = ""
        for i in self.datos:
            temp = "%s %s" % (temp, i)
        temp = "%s%s" % (temp, "\n")
        return temp

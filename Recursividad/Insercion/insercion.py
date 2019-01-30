class ordenamientoInsercion(object):

    def __init__(self, valores):  # Constructor
        self.datos = valores

    def ordenar(self):  # Proceso para ordenar los datos
        i = 1
        while (i < len(self.datos)):
            insercion = self.datos[i]
            moverElem = i
            while ((moverElem > 0) and (self.datos[moverElem-1] > insercion)):
                self.datos[moverElem] = self.datos[moverElem-1]
                moverElem = moverElem - 1
            self.datos[moverElem] = insercion
            print(self.__str__())
            i = i + 1

    def __str__(self):  # Sobreescritura del metodo toString
        temp = ""
        for i in self.datos:
            temp = "%s %s" % (temp, i)
        temp = "%s%s" % (temp, "\n")
        return temp

from ordenamiento import ordenamientoSeleccion as oS  # Se importa la clase ordenamiento

valores = [50, 150, 12, 0, 42, 27]  # Arreglo de datos

arrayOrden = oS(valores)  # Creación de objeto
print("Arreglo Desordenado:\n")
print(arrayOrden)  # Impresión del arreglo desordenado
arrayOrden.ordenar()  # Impresión de las iteraciones del arreglo hasta presentar el arreglo ordenado

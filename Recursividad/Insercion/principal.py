from insercion import ordenamientoInsercion as oI  # Importación de la clase de ordenamiento

valores = [10, 90, 1, 20, 4, 7, 15, 33, 14, 0]

arrayOrden = oI(valores)  # Creación del objeto

print("Arreglo Desordenado:\n")
print(arrayOrden)
arrayOrden.ordenar()

print("Arreglo Ordenado:\n")
print(arrayOrden)

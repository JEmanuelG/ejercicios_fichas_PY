'''
Cargar por teclado dos números enteros. Mostrarlos ordenados de menor a mayor.
'''
#definicion de variables
n1 = n2 = 0

#carga de datos
print("Carga los datos")
n1 = int(input("1er número:"))
n2 = int(input("2do número:"))

#procesos / muestra resultado
if (n1 > n2):
    print("Números de menor a mayor: {}, {}".format(n2, n1))
else:
    print("Números de menor a mayor: {}, {}".format(n1, n2))
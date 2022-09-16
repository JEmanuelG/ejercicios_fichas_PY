'''
Cargar por teclado tres números enteros y determinar y mostrar el mayor de ellos. No 
utilice para el proceso la función max() de la librería estándar de Python: diseñe el algoritmo 
suponiendo que tal función no existe en el lenguaje que usará para el desarrollo del programa
'''

# Define variables
n1 = n2 = n3 = 0
mayor = 0

# Carga de datos por teclado
print("Ingrese 3 números")
n1 = int(input("1er número:"))
n2 = int(input("2do número:"))
n3 = int(input("3er número:"))

# Define funcion para calcular el mayor
def calcula_mayor(a, b, c):
    if (a > b) and (a > c):
        return a
    elif (b > c):
        return b
    else:
        return c

mayor = calcula_mayor(n1, n2, n3)

# Muestra resultado
print("El mayor es:", mayor)

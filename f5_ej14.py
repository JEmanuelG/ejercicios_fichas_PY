'''
 Se cargan por teclado tres números. Se pide mostrarlos en pantalla, ordenados de 
menor a mayor.
'''

# Define variables
n1 = n2 = n3 = 0
menor = medio = mayor = 0

# Carga datos
print("Cargar datos")
n1 = int(input("1er número:"))
n2 = int(input("2do número:"))
n3 = int(input("3er número:"))

# Define el mayor y el menor
if (n1 > n2):
    mayor = n1
    menor = n2
else:
    mayor = n2
    menor = n1

# Define el medio
if (n3 > mayor):
    medio = mayor
    mayor = n3
else:
    if (n3 > menor):
        medio = n3
    else:
        medio = menor
        menor = n3

# Muestra resultado en pantalla
print(menor, medio, mayor)
'''La fuerza de atracción entre dos masas m1 y m2 separadas por una distancia d, está 
dada por la siguiente fórmula de la mecánica clásica: 
F = G*  (m1*m2/d**2)
)
con G = 6.673 * 10**-8
(constante de gravitación universal)
Escribir un programa que cargue las masas m1 y m2 de dos cuerpos y la distancia d entre ellos y 
obtenga y muestre el valor de la intensidad de la fuerza de atracción entre esos cuerpos.
'''

#definicion de variables
fuerza_atraccion = 0
gravedad = 0
distancia = 0
masa1 = masa2 = 0
intensidad = 0

#carga de datos
print("Ingrese los datos")
masa1 = float(input("Masa del 1er cuerpo:"))
masa2 = float(input("Masa del 2do cuerpo:"))
distancia = float(input("Distancia entre los cuerpos:"))

#calculos
gravedad = 6.673 * pow(10, -8)
fuerza_atraccion = (gravedad * masa1 * masa2) / distancia ** 2

#muestra resultados
print("La fuerza de atracción entre los cuerpos:", fuerza_atraccion)
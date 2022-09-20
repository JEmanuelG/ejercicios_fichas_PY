#Dado el valor de los tres lados de un triángulo, calcular el perímetro del triángulo.

#Variables de los lados del triangulo
l1 = l2 = l3 = 0

#carga valores por teclado
l1 = float(input("Ingrese lado 1:"))
l2 = float(input("Ingrese lado 2:"))
l3 = float(input("Ingrese lado 3:"))

#calcula perimetro
perimetro = l1 + l2 + l3

#muetra resultado
print("El perimetro del triangulo es", perimetro)

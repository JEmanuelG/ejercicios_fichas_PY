'''
Cargar por teclado una lista de números enteros que irán llegando uno a uno, y que 
representan cantidades mensuales de automóviles nuevos vendidos en el país durante cierto período. 
Para indicar que la carga de datos debe finalizar, se ingresará el valor -1 (menos uno) (note que el 
valor 0 (cero) puede ser un dato valido: es perfectamente posible que no haya habido ventas en un 
mes determinado). Se pide:
a. Determinar cuántas de esas cantidades fueron mayores o iguales que 0 pero menores que 
10000 unidades, cuántas fueron mayores o iguales a 10000 pero menores que 15000, y 
cuántas fueron mayores o iguales que 15000.
b. Determinar la cantidad total de automóviles nuevos que se vendieron en el país.
c. Determinar si se ingresó al menos una cantidad igual a 0 o no. Informe con un mensaje simple 
en pantalla.
'''

# Define variables y contadores
cant = 0
cero_a_diezk = diezk_a_quincek = mas_quincek = 0
total_vendido = 0
cant_cero = 0

#Carga de datos
cant = int(input("Ingrese cantidad de vehículos vendidos:"))

# procesos, contadores
while (cant != -1):
    if 0 <= cant < 10000:
        cero_a_diezk += 1
        
        if cant == 0:
            cant_cero += 1
    
    elif 10000 <= cant < 15000:
        diezk_a_quincek += 1
    
    elif cant >= 15000:
        mas_quincek += 1
    
    total_vendido += cant

    cant = int(input("Ingrese cantidad de vehículos vendidos:"))
    print("(Finaliza con -1)")

# Muestra resultados
print('''Cantidades vendidas 0 <= Cant < 10k: {}
Cantidades vendidas 10k <= Cant < 15k: {}
Cantidades vendidas 15k <= Cant: {}'''.format(cero_a_diezk, diezk_a_quincek, mas_quincek))

print("Cantidad total vendida:", total_vendido)

# condicion para mostrar si se corgo algun cero
if cant_cero > 0:
    print("Se cargó al menos una cantidad igual a cero.")
else:
    print("no se cargó cantidades igual a cero.")
'''
Un pequeño comercio de papelería cuenta con dos vendedores. Cada vendedor está 
codificado con los números 1 y 2. Considere que la carga de datos se realizará desde teclado, de 
forma que una entrada consta de 3 variables que representan una venta realizada: por cada venta, 
cargar el código del vendedor (1 o 2) que hizo la venta, cantidad de artículos vendida en esa 
operación, e importe de la venta. El fin de datos se indicará con código de vendedor igual a 0 (cero). 
El dueño del comercio desea cierta información estadística y para ello solicita un programa que 
obtenga lo siguiente:
a.) La cantidad de productos vendida por cada vendedor (dos totales).
b.) El importe total vendido por cada vendedor (otros dos totales).
c.) El importe de la menor venta realizada por el vendedor 2. 
d.) El importe promedio de ventas por vendedor (importe total acumulado / 2).
'''

productos_total_uno = productos_total_dos = 0
importe_total_uno = importe_total_dos = 0
importe_total = 0
importe_menor_dos = 0
flag_menor_dos = True
promedio_importe_ventas = 0


cod = 1

while cod != 0:
    print('Ingrese datos de la venta')
    cod = int(input('ingrese código de vendedor(1 o 2, con 0 finaliza):'))
    
    # SI EL COD ES 0 SALTA ESTE PASO PARA FINALIZAR CON EL SCRIPT
    if cod != 0:
        cant_prod = int(input('Cantidad de productos: '))
        importe = float(input('Importe total: '))
    
    # ACUMULA LOS VALORES DEL VENDEDOR 1
    if cod == 1:
        productos_total_uno += cant_prod
        importe_total_uno += importe

    # ACUMULA LOS VALORES DEL VENDEDOR 2
    elif cod == 2:
        productos_total_dos += cant_prod
        importe_total_dos += importe
        
        # POR MEDIO DE LA BANDERA PONE EL PRIMER VALOR CARGADO COMO EL MENOR IMPORTE DE VENTA
        if flag_menor_dos:
            importe_menor_dos = importe
            flag_menor_dos = False
        
        # COMPARA EL VALOR DEL IMPORTE MENOR POR EL VALOR ACTUAL, SI SE CUMPLE REEMPLAZA EL VALOR
        if importe < importe_menor_dos:
            importe_menor_dos = importe
    
# SUMA LOS IMPORTES TOTALES POR VENDEDOR
importe_total = importe_total_uno + importe_total_dos

# CALCULA EL PROMEDIO DEL IMPORTE TOTAL
promedio_importe_ventas = importe_total / 2

# MUESTRA RESULTADOS
print('La cantidad de productos vendida por el vendedor 1:', productos_total_uno)
print('La cantidad de productos vendida por el vendedor 2:', productos_total_dos)

print('El importe total vendido por el vendedor 1:', importe_total_uno)
print('El importe total vendido por el vendedor 2:', importe_total_dos)

print('El importe de la menor venta realizada por el vendedor 2:', importe_menor_dos)

print('El importe promedio de ventas por vendedor:', promedio_importe_ventas)
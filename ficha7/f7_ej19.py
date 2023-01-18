'''
Determinar el mayor valor de una sucesión de valores que se cargan por teclado.
Asuma en primera instancia que la cantidad n de números a procesar se conoce de antemano. Y 
luego de resolverlo con esa suposición, replantee su solución asumiendo que la cantidad n de 
números se desconoce y que la carga de datos terminará cuando se ingrese un 0. 
'''





# 1ra Instancia
def calcular_mayor():
    '''Esta función calcula el número mayor de una serie de valores ingresados por teclado
    con la  cantidad de valores a procesar establecida'''

    cant = 5
    may = 0

    for i in range(cant):
        num = int(input('Ingrese un número entero:'))
        
        # SI ES LA PRIMER VUELTA ASIGNA EL PRIMER VALOR CARGADO COMO EL MAYOR
        if i == 0:
            may = num

        else:
            # COMPARA EL NUEVO VALOR CARGADO CON EL MAYOR REGISTRADO Y REEMPLAZA SU VALOR SI ES QUE
            # SE CUMPLE LA CONDICION
            if num > may:
                may = num

    # MUESTRA EL VALOR MAYOR EN CONSOLA
    print('El valor mayor ingresado es', may)

# 2da Instancia
def calcular_mayor_while():
    n = 1
    flag_primer_valor = True
    may = 0

    while n != 0:
        n = int(input('Ingrese un número entero(Con 0 corta):'))
        
        # SI LA BANDERA QUE CONTROLA EL PRIMER VALOR INGRESADO ES VERDADERA ASIGNA EL PRIMER
        # VALOR COMO EL MAYOR
        if flag_primer_valor:
            may = n
            flag_primer_valor = False

        # COMPARA EL NUEVO VALOR CARGADO CON EL MAYOR REGISTRADO Y REEMPLAZA SU VALOR SI ES QUE
        # SE CUMPLE LA CONDICION
        if n > may:
            may = n

    # MUESTRA EL VALOR MAYOR EN CONSOLA
    print('El valor mayor ingresado es', may)


calcular_mayor()

calcular_mayor_while()
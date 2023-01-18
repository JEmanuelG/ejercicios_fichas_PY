'''
Se pide desarrollar un programa en Python que cargue por teclado un número n y calcule y muestre 
su factorial.
'''

def mostrar_resultado(numero):
    ''' Esta función calcula el factorial de un número pasado por parametro y muestra en consola
    el resultado y las operaciones realizadas'''
    
    factorial = numero 
    num = numero
    
    print('El factorial de ' + str(numero))
    
    if numero > 0:
        print(str(numero) + '!' + '=', end='')

        for n in range(numero):
            # REALIZA LAS MULTIPLICACIONES DEL FACTORIAL EXCLUYENDO LA VUELTA 0
            if n > 0:
                factorial *= n
            
            # MUESTRA EN PANTALLA n-1
            print(num, end='')
            
            # MUESTRA EN PANTALLA EL SIGNO DE MULTIPLICACIÓN SI n != 0, CUANDO n=1 MUESTRA EL
            # SIGNO '=' SEGUIDO DEL RESULTADO
            if num != 1:
                print('*', end='')
            
            else:
                print('=' + str(factorial))
            
            num -= 1
    
    elif numero == 0:
        print(str(numero) + '!' + '=' + str(factorial))


# INGRESA POR TECLADO UN NÚMERO PARA CALCULAR SU FACTORIAL
msj = 'Ingrese un número >= 0 para calcular su factorial:'
num = int(input(msj))
    
mostrar_resultado(num)

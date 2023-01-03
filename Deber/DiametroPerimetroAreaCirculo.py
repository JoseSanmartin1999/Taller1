"""
El siguiente programa tiene com oobjetivo calcular el area y perimetro de una figura de 4 en este 
 caso un trapezoides con los datos que nos proporciona el usuario mediante el teclado

Autores:
Jose Sanmartin
Verisión:
VER.0.1
"""
import os
import math
def APDCirculo():
    """ 
    Es una funcion la cual va a realizar toda la parte matematica 
    de la operacion y nos va a enviar el resultado del perimetro del trapezoide
    Recibe
    ------------
      lado1,lado2,lado3,lado4:Recibe los valores de los lados que se usaran para calcular el perimetro
    ------------
       No retorna nigun parametro
    """
    #Creamos un bucle While para que se repita hasta que los datos ingresados sean validos
    while True:
        #Creamos la condicion para validar datos 
        try:
        #Creamos una funcion que nos permita ingresar la variable dato
            radio=float(input("Ingrese el valor del radio: "))
            #Revisamos que la condicion se cumpla 
        except ValueError:
            #Enviamos un mensaje de advertencia
            print("Debe ser un numero")
            #Continuamos si las condiciones se cumplen
            continue
        #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
        if radio<=0:
            #Evaimos un mensaje de advertencia 
            print("Debe ser un numero positivo y no puede ser 0")
            continue
            #Se crea la condicion para salir del bucle 
            
        else:
            #Salimos del bucle
            break
    diametro=radio*2
    area=math.pi*math.pow(radio,2)
    perimetro=2*math.pi*radio
    

    print("El diametro del circulo es: ", diametro, "unidades")
    print("El perimetro del circulo es: ", perimetro, "unidades")
    print("El Area del circulo es: ", area, "unidades^2")
    reiniciarse()

def reiniciarse():
    """ 
    Es un funcion en la que preguntaremos al usuario si desea volver a ejecutar el 
    programa o si desea salir 
    Recibe
    ------------
      reiniciar:Es una variable en la cual elegiremos si deseamos continuar o si no
    ------------
       saludar(): Retorna la funcion si se cumple la condicion dada
       
    """
    #Se crea un variable que nos preguntara si deseamos volver a realizar el programa
    reiniciar=input("Relizamos otra operacion? si (s) o no(n): ")
    #Se crea la condicion
    if reiniciar=="s":
    #Se regresa al inicio del progrma
        return APDCirculo()
    #Se cre otra condicion
    elif(reiniciar=="n"):
    #Se escribe un mensaje
        print("Hasta Luego")
        return os.system("Pause")
    #Se termina con un condicion por si no es valido
    else:
        #Se pregunta de nuevo
        return reiniciarse()

#Programa principal 
if __name__ == '__main__':
#Mensaje de Bienvenida
    print("---Calcular el Area,Diametro, Perimetro de un Circulo---")
#Se llama la funcion Suma      
APDCirculo()
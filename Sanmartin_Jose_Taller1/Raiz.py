"""
El siguiente programa tiene com oobjetivo calcular el area y perimetro de una figura de 4 en este 
 caso un trapezoides con los datos que nos proporciona el usuario mediante el teclado

Autores:
Jose Sanmartin
Verisión:
VER.0.1
"""
#Se importa la biblioteca necesaria para poder salir del sistema despues 
import os
def raiz():
   
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
            radicando=float(input("Ingrese el valor del radicando: "))
            #Revisamos que la condicion se cumpla 
        except ValueError:
            #Enviamos un mensaje de advertencia
            print("Debe ser un numero")
            #Continuamos si las condiciones se cumplen
            continue     
        else:
            #Salimos del bucle
            break
    while True:
        #Creamos la condicion para validar datos 
        try:
        #Creamos una funcion que nos permita ingresar la variable dato
            radical=float(input("Ingrese el valor del radical: "))
            #Revisamos que la condicion se cumpla 
        except ValueError:
            #Enviamos un mensaje de advertencia
            print("Debe ser un numero")
            #Continuamos si las condiciones se cumplen
            continue
        #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
        if radical==0:
            #Evaimos un mensaje de advertencia 
            print("Debe ser un numero diferente de 0")
            #Se crea la condicion para salir del bucle 
        else:
            #Salimos del bucle
            break
    if (radicando<0 and radical%2==0):
        print("No es posible Intenta de Nuevo")
        return raiz()
    else:
        raizRes=radicando**(1/radical)
        print("La respuesta es: ",raizRes)
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
    reiniciar=input("Reliza otra operacion si (s) o no(n): ")
    #Se crea la condicion
    if reiniciar=="s":
    #Se regresa al inicio del progrma
        return raiz()
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
#Se llama la funcion Suma      
    print("-----CALCULADO DE RADICACION------")
#Se saldra del programa con un click
raiz()
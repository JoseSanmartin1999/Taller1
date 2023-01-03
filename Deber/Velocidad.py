"""
Se busca un programa el cual calcule la velocidad, con los datos ingresados por el usario, tambien le 
daremos la oportunidad de conocer su distancia o el tiempo si asi lo desea 
Autores:
Jose Sanmartin
Verisión:
VER.0.1
"""
#Importamos las bibliotecas que iremos a usar 
import math,os
def velocidad():
    """ 
    La funcion crea la forma de calcular la velocidad, con los datos ingresados por el usuario
    para realizar la operacion correspondiente e imprimir el resultado correcto
    Recibe
    ------------
      No Recibe ningun parametro
    Retorna
    ------------
       No retorna nigun parametro
    """
    #Creamos un bucle While para que se repita hasta que los datos ingresados sean validos
    while True:
        #Creamos la condicion para validar datos 
        try:
        #Creamos una funcion que nos permita ingresar la variable dato
            distancia=float(input("Ingrese el valor de la distancia en Kilometros(Km): "))
            #Revisamos que la condicion se cumpla 
        except ValueError:
            #Enviamos un mensaje de advertencia
            print("Debe ser un numero")
            #Continuamos si las condiciones se cumplen
            continue
        else:
            #Salimos del bucle
            break
        #Creamos un bucle While para que se repita hasta que los datos ingresados sean validos
    while True:
         #Creamos la condicion para validar datos 
        try:
            #Pedimos al usuario que ingrese la altura 
            tiempo=float(input("Ingrese el valor del timepo en horas: "))
            #No nos permite avanzar si la condicion no se cumple
        except:
            #Se imprime la advertencia 
            print("Debe ser un numero")
            #Si se cumplen las condiciones se debe seguir 
            continue
        #Se crea una condicion en la que no podemos tener numeros negativos
        if tiempo<=0:
            #Enviamos una advertencia 
            print("El tiempo no pude ser negativo o 0")
            #Creamos una condicion de salida
        else:
            #Se sale del bucle
            break
        #Se calcula el area lateral
    velocidad=distancia/tiempo
    #Se imprime el resultado
    print("La Velocidad es: ", velocidad,"Km/h")
    reiniciarse()

def Distancia():
    """ 
    La funcion crea la forma de calcular la distancia , con los datos ingresados por el usuario
    para realizar la operacion correspondiente e imprimir el resultado correcto
    Recibe
    ------------
      No recibe ningun parametro
    Retorna
    ------------
       No retorna nigun parametro
    """
    #Creamos un bucle While para que se repita hasta que los datos ingresados sean validos
    while True:
        #Creamos la condicion para validar datos 
        try:
        #Creamos una funcion que nos permita ingresar la variable dato
            velocidad=float(input("Ingrese el valor de la velocidad en km/h (Kilometro sobre hora): "))
            #Revisamos que la condicion se cumpla 
        except ValueError:
            #Enviamos un mensaje de advertencia
            print("Debe ser un numero")
            #Continuamos si las condiciones se cumplen
            continue
        #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
        
        else:
            #Salimos del bucle
            break
        #Creamos un bucle While para que se repita hasta que los datos ingresados sean validos
    while True:
         #Creamos la condicion para validar datos 
        try:
            #Pedimos al usuario que ingrese la altura 
            tiempo=float(input("Ingrese el valor del tiempo en horas: "))
            #No nos permite avanzar si la condicion no se cumple
        except:
            #Se imprime la advertencia 
            print("Debe ser un numero")
            #Si se cumplen las condiciones se debe seguir 
            continue
        #Se crea una condicion en la que no podemos tener numeros negativos
        if tiempo<0:
            #Enviamos una advertencia 
            print("No existe tiempo negativo")
            #Creamos una condicion de salida
        else:
            #Se sale del bucle
            break
        #Se calcula el area total
    distancia=velocidad*tiempo
    #Se imprime el resultado
    print(" La distancia es es: ", distancia, "Km")
    reiniciarse()
def Tiempo():
    """ 
    La funcion crea la forma de calcular el tiempo , con los datos ingresados por el usuario
    para realizar la operacion correspondiente e imprimir el resultado correcto
    Recibe
    ------------
      No recibe ningun parametro
    Retorna
    ------------
       No retorna nigun parametro
    """
    #Creamos un bucle While para que se repita hasta que los datos ingresados sean validos
    while True:
        #Creamos la condicion para validar datos 
        try:
        #Creamos una funcion que nos permita ingresar la variable dato
            distancia=float(input("Ingrese la distanica recorrida en km: "))
            #Revisamos que la condicion se cumpla 
        except ValueError:
            #Enviamos un mensaje de advertencia
            print("Debe ser un numero")
            #Continuamos si las condiciones se cumplen
            continue
        #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
        else:
            #Salimos del bucle
            break
        #Creamos un bucle While para que se repita hasta que los datos ingresados sean validos
    while True:
         #Creamos la condicion para validar datos 
        try:
            #Pedimos al usuario que ingrese la altura 
            velocidad=float(input("Ingrese el valor de la velocidad en km/h: "))
            #No nos permite avanzar si la condicion no se cumple
        except:
            #Se imprime la advertencia 
            print("Debe ser un numero")
            #Si se cumplen las condiciones se debe seguir 
            continue
        #Se crea una condicion en la que no podemos tener numeros negativos
        if velocidad==0:
            #Enviamos una advertencia 
            print("No puede ser 0")
            #Creamos una condicion de salida
        else:
            #Se sale del bucle
            break
        #Se calcula el area lateral
   
    tiempo=distancia/velocidad
    #Se imprime el resultado
    if tiempo>=0:
        print("El tiempo  es: ", tiempo,"en horas")
    elif tiempo<0:
        print("No existe tiempo negativo, prueba de nuevo")
        return Tiempo()
    reiniciarse()

def reiniciarse():
    """ 
    Es un funcion en la que preguntaremos al usuario si desea volver a ejecutar el 
    programa o si desea salir 
    Recibe
    ------------
      reiniciar:Es una variable en la cual elegiremos si deseamos realizar de nuevo otra operaciono si no
    ------------
       Operaciones(): Retorna la funcion si se cumple la condicion dada
       
    """
    #Se crea un variable que nos preguntara si deseamos volver a realizar el programa
    reiniciar=input("Quieres realizar otra operacion si (s) o no(n): ")
    #Se crea la condicion
    if reiniciar=="s":
    #Se regresa al inicio del progrma
        return Operaciones()
    #Se cre otra condicion
    elif(reiniciar=="n"):
    #Se escribe un mensaje
        print("Hasta Luego")
        os.system("Pause")

    #Se termina con un condicion por si no es valido
    else:
            #Se pregunta de nuevo
            return reiniciarse()

def Operaciones():
    print("Desea calcular la velocidad: Opcion 1")
    print("Desea calcular la distancia: Opcion 2")
    print("Desea calcular el tiempo: Opcion 3")
    opciones=["1","2","3"]
    opcion=0
    while (opcion) not in opciones:
        try:
            opcion=input("Elija una opcion: ")
        except:
            print("Opcion no valida")
            
        if opcion == "1":
            return velocidad()
        elif opcion=="2":
            return Distancia()
        elif opcion=="3":
            return Tiempo()
#Programa principal 
if __name__ == '__main__':
#Se llama la funcion Principal    
    Operaciones()
   


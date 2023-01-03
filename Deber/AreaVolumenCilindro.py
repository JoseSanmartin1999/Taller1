"""
Se busca un programa el cual calcule el area de un cilindro, pero tambien integraremos la opcion de 
calcular el volumen de este 
Autores:
Jose Sanmartin
Verisión:
VER.0.1
"""
#Importamos las bibliotecas que iremos a usar 
import math,os
def AreaLateral():
    """ 
    Es una funcion la cual va a realizar toda la parte matematica 
    de la operacion y nos va a enviar el resultado del area lateral
    Recibe
    ------------
      radio: Recibe el valor de radio para poder utilzarlo posteriormente en el calculo del area
      altura: En este nos recibe la variable altura para ser utilizado posteriormente
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
        if radio<0:
            #Evaimos un mensaje de advertencia 
            print("Debe ser un numero positivo")
            #Se crea la condicion para salir del bucle 
        else:
            #Salimos del bucle
            break
        #Creamos un bucle While para que se repita hasta que los datos ingresados sean validos
    while True:
         #Creamos la condicion para validar datos 
        try:
            #Pedimos al usuario que ingrese la altura 
            altura=float(input("Ingrese el valor de la altura: "))
            #No nos permite avanzar si la condicion no se cumple
        except:
            #Se imprime la advertencia 
            print("Debe ser un numero")
            #Si se cumplen las condiciones se debe seguir 
            continue
        #Se crea una condicion en la que no podemos tener numeros negativos
        if altura<0:
            #Enviamos una advertencia 
            print("Debe ser un numero positivo")
            #Creamos una condicion de salida
        else:
            #Se sale del bucle
            break
        #Se calcula el area lateral
    arealateral=2*math.pi*radio*altura
    #Se imprime el resultado
    print("El area lateral es: ", arealateral)
    reiniciarse()

def AreaTotal():
    """ 
    Es una funcion la cual va a realizar toda la parte matematica 
    de la operacion y nos va a enviar el resultado del area lateral
    Recibe
    ------------
      radio: Recibe el valor de radio para poder utilzarlo posteriormente en el calculo del area
      altura: En este nos recibe la variable altura para ser utilizado posteriormente
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
        if radio<0:
            #Evaimos un mensaje de advertencia 
            print("Debe ser un numero positivo")
            #Se crea la condicion para salir del bucle 
        else:
            #Salimos del bucle
            break
        #Creamos un bucle While para que se repita hasta que los datos ingresados sean validos
    while True:
         #Creamos la condicion para validar datos 
        try:
            #Pedimos al usuario que ingrese la altura 
            altura=float(input("Ingrese el valor de la altura: "))
            #No nos permite avanzar si la condicion no se cumple
        except:
            #Se imprime la advertencia 
            print("Debe ser un numero")
            #Si se cumplen las condiciones se debe seguir 
            continue
        #Se crea una condicion en la que no podemos tener numeros negativos
        if altura<0:
            #Enviamos una advertencia 
            print("Debe ser un numero positivo")
            #Creamos una condicion de salida
        else:
            #Se sale del bucle
            break
        #Se calcula el area total
    areatotal=2*math.pi*radio*(altura+radio)
    #Se imprime el resultado
    print("El area lateral es: ", areatotal)
    reiniciarse()
def Volumen():
    """ 
    Es una funcion la cual va a realizar toda la parte matematica 
    de la operacion y nos va a enviar el resultado del area lateral
    Recibe
    ------------
      radio: Recibe el valor de radio para poder utilzarlo posteriormente en el calculo del area
      altura: En este nos recibe la variable altura para ser utilizado posteriormente
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
        if radio<0:
            #Evaimos un mensaje de advertencia 
            print("Debe ser un numero positivo")
            #Se crea la condicion para salir del bucle 
        else:
            #Salimos del bucle
            break
        #Creamos un bucle While para que se repita hasta que los datos ingresados sean validos
    while True:
         #Creamos la condicion para validar datos 
        try:
            #Pedimos al usuario que ingrese la altura 
            altura=float(input("Ingrese el valor de la altura: "))
            #No nos permite avanzar si la condicion no se cumple
        except:
            #Se imprime la advertencia 
            print("Debe ser un numero")
            #Si se cumplen las condiciones se debe seguir 
            continue
        #Se crea una condicion en la que no podemos tener numeros negativos
        if altura<0:
            #Enviamos una advertencia 
            print("Debe ser un numero positivo")
            #Creamos una condicion de salida
        else:
            #Se sale del bucle
            break
        #Se calcula el area lateral
    areabase=math.pi*math.pow(radio,2)
    volumen=areabase*altura
    #Se imprime el resultado
    print("El Volumen  es: ", volumen)
    reiniciarse()

def reiniciarse():
    """ 
    Es un funcion en la que preguntaremos al usuario si desea volver a ejecutar el 
    programa o si desea salir 
    Recibe
    ------------
      reiniciar:Es una variable en la cual elegiremos si deseamos continuar o si no
    ------------
       MenuVolArea(): Retorna la funcion si se cumple la condicion dada
       
    """
    #Se crea un variable que nos preguntara si deseamos volver a realizar el programa
    reiniciar=input("Quieres realizar otra operacion si (s) o no(n): ")
    #Se crea la condicion
    if reiniciar=="s":
    #Se regresa al inicio del progrma
        return MenuVolArea()
    #Se cre otra condicion
    elif(reiniciar=="n"):
    #Se escribe un mensaje
        print("Hasta Luego")
        os.system("Pause")

    #Se termina con un condicion por si no es valido
    else:
            #Se pregunta de nuevo
            return reiniciarse()

def MenuVolArea():
    print("Desea calcular el Area Lateral: Opcion 1")
    print("Desea calcular el Area Total: Opcion 2")
    print("Desea calcular el Volumen: Opcion 3")
    opciones=["1","2","3"]
    opcion=0
    while (opcion) not in opciones:
        try:
            opcion=input("Elija una opcion: ")
        except:
            print("Opcion no valida")
            
        if opcion == "1":
            return AreaLateral()
        elif opcion=="2":
            return AreaTotal()
        elif opcion=="3":
            return Volumen()
#Programa principal 
if __name__ == '__main__':
#Se llama la funcion Principal    
    MenuVolArea()
   


"""
El siguiente programa tiene com oobjetivo calcular el area y perimetro de una figura de 4 en este 
 caso un paralelogramo con los datos que nos proporciona el usuario mediante el teclado

Autores:
Jose Sanmartin
Verisión:
VER.0.1
"""
import os
import math
def PerimetroParaleloLados():
    """ 
    Es una funcion la cual va a realizar toda la parte matematica 
    de la operacion y nos va a enviar el resultado del perimetro del trapezoide
    Recibe
    ------------
      lado1,lado2:Recibe los valores de los lados que se usaran para calcular el perimetro
    ------------
       No retorna nigun parametro
    """
    #Creamos un bucle While para que se repita hasta que los datos ingresados sean validos
    while True:
        #Creamos la condicion para validar datos 
        try:
        #Creamos una funcion que nos permita ingresar la variable dato
            lado1=float(input("Ingrese el valor del lado 1: "))
            #Revisamos que la condicion se cumpla 
        except ValueError:
            #Enviamos un mensaje de advertencia
            print("Debe ser un numero")
            #Continuamos si las condiciones se cumplen
            continue
        #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
        if lado1<=0:
            #Evaimos un mensaje de advertencia 
            print("Debe ser un numero positivo y diferente de 0")
            #Se crea la condicion para salir del bucle 
        else:
            #Salimos del bucle
            break
        #Creamos un bucle While para que se repita hasta que los datos ingresados sean validos
    while True:
         #Creamos la condicion para validar datos 
        try:
            #Pedimos al usuario que ingrese la altura 
            lado2=float(input("Ingrese el valor del lado2:  "))
            #No nos permite avanzar si la condicion no se cumple
        except:
            #Se imprime la advertencia 
            print("Debe ser un numero")
            #Si se cumplen las condiciones se debe seguir 
            continue
        #Se crea una condicion en la que no podemos tener numeros negativos
        if lado2<=0:
            #Enviamos una advertencia 
            print("Debe ser un numero positivo y diferente a 0")
            #Creamos una condicion de salida
        else:
            #Se sale del bucle
            break
    #Creamos un bucle While para que se repita hasta que los datos ingresados sean validos
    
    perimetro=2*(lado1+lado2)
    print("El perimetro es: ",perimetro,"unidades")
    reiniciarse()

def PerimetroMetodoAngulo():
    """ 
    Es una funcion la cual va a realizar toda la parte matematica 
    de la operacion y nos va a enviar el resultado del perimetri conociendo su lado, base 
    y el angulo entre estos 
    Recibe
    ------------
        Angulo: Recibe el valor de Angulo para poder utilzarlo posteriormente en el calculo del area
        Base: En este nos recibe la variable base para ser utilizado posteriormente
        Altura: En este nos recibe la variable altura para ser utilizado posteriormente
    ------------
       No retorna nigun parametro
    """
    #Creamos un bucle While para que se repita hasta que los datos ingresados sean validos
    while True:
        #Creamos la condicion para validar datos 
        try:
        #Creamos una funcion que nos permita ingresar la variable dato
            base=float(input("Ingrese el valor de la base: "))
            #Revisamos que la condicion se cumpla 
        except ValueError:
            #Enviamos un mensaje de advertencia
            print("Debe ser un numero")
            #Continuamos si las condiciones se cumplen
            continue
        #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
        if base<=0:
            #Evaimos un mensaje de advertencia 
            print("Debe ser un numero positivo y diferente de 0")
            #Se crea la condicion para salir del bucle 
        else:
            #Salimos del bucle
            break
    while True:
        #Creamos la condicion para validar datos 
        try:
            #Creamos una funcion que nos permita ingresar la variable dato
            altura=float(input("Ingrese el valor de la altura: "))
                #Revisamos que la condicion se cumpla 
        except ValueError:
                #Enviamos un mensaje de advertencia
            print("Debe ser un numero")
                #Continuamos si las condiciones se cumplen
            continue
            #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
        if altura<=0:
                #Evaimos un mensaje de advertencia 
            print("Debe ser un numero positivo y diferente de 0")
                #Se crea la condicion para salir del bucle 
        else:
                #Salimos del bucle
            break
    while True:
        #Creamos la condicion para validar datos 
        try:
            #Creamos una funcion que nos permita ingresar la variable dato
            angulo=math.radians(float(input("Ingrese el valor del angulo en Grados: ")))
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
    perimetro=2*(base+altura*math.cos(angulo))
    print("El Area es: ",perimetro,"unidades^2")
    reiniciarse()

def AreaMetodoBaseAltura():
    """ 
    Es una funcion la cual va a realizar toda la parte matematica 
    de la operacion y nos va a enviar el resultado del area conociendo sus dos lados 
    y el angulo entre estos 
    Recibe
    ------------
      Base: Recibe el valor de la base
      altura: recibe el valor de la altura para realizar las operaciones 
      
    ------------
       No retorna nigun parametro
    """
    #Creamos un bucle While para que se repita hasta que los datos ingresados sean validos
    while True:
        #Creamos la condicion para validar datos 
        try:
        #Creamos una funcion que nos permita ingresar la variable dato
            base=float(input("Ingrese el valor de la base: "))
            #Revisamos que la condicion se cumpla 
        except ValueError:
            #Enviamos un mensaje de advertencia
            print("Debe ser un numero")
            #Continuamos si las condiciones se cumplen
            continue
        #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
        if base<=0:
            #Evaimos un mensaje de advertencia 
            print("Debe ser un numero positivo y diferente de 0")
            #Se crea la condicion para salir del bucle 
        else:
            #Salimos del bucle
            break
    while True:
        #Creamos la condicion para validar datos 
        try:
            #Creamos una funcion que nos permita ingresar la variable dato
            altura=float(input("Ingrese el valor de la altura: "))
                #Revisamos que la condicion se cumpla 
        except ValueError:
                #Enviamos un mensaje de advertencia
            print("Debe ser un numero")
                #Continuamos si las condiciones se cumplen
            continue
            #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
        if altura<=0:
                #Evaimos un mensaje de advertencia 
            print("Debe ser un numero positivo y diferente de 0")
                #Se crea la condicion para salir del bucle 
        else:
                #Salimos del bucle
            break
    
    area=base*altura
    print("El Area es: ",area,"unidades^2")
    reiniciarse()

def AreaMetodoNoAltura():
    """ 
    Es una funcion la cual va a realizar toda la parte matematica 
    de la operacion y nos va a enviar el resultado del area conociendo sus dos lados 
    y el angulo entre estos 
    Recibe
    ------------
      Angulo: Recibe el valor de Angulo para poder utilzarlo posteriormente en el calculo del area
      lado1: En este nos recibe la variable lado1 para ser utilizado posteriormente
      lado2: En este nos recibe la variable lado2 para ser utilizado posteriormente
    ------------
       No retorna nigun parametro
    """
    #Creamos un bucle While para que se repita hasta que los datos ingresados sean validos
    while True:
        #Creamos la condicion para validar datos 
        try:
        #Creamos una funcion que nos permita ingresar la variable dato
            lado1=float(input("Ingrese el valor del lado 1: "))
            #Revisamos que la condicion se cumpla 
        except ValueError:
            #Enviamos un mensaje de advertencia
            print("Debe ser un numero")
            #Continuamos si las condiciones se cumplen
            continue
        #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
        if lado1<=0:
            #Evaimos un mensaje de advertencia 
            print("Debe ser un numero positivo y diferente de 0")
            #Se crea la condicion para salir del bucle 
        else:
            #Salimos del bucle
            break
    while True:
        #Creamos la condicion para validar datos 
        try:
            #Creamos una funcion que nos permita ingresar la variable dato
            lado2=float(input("Ingrese el valor del lado 2: "))
                #Revisamos que la condicion se cumpla 
        except ValueError:
                #Enviamos un mensaje de advertencia
            print("Debe ser un numero")
                #Continuamos si las condiciones se cumplen
            continue
            #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
        if lado2<=0:
                #Evaimos un mensaje de advertencia 
            print("Debe ser un numero positivo y diferente de 0")
                #Se crea la condicion para salir del bucle 
        else:
                #Salimos del bucle
            break
    while True:
        #Creamos la condicion para validar datos 
        try:
            #Creamos una funcion que nos permita ingresar la variable dato
            angulo=math.radians(float(input("Ingrese el valor del angulo: ")))
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
    area=lado1*lado2*math.sin(angulo)
    print("El Area es: ",area,"unidades^2")
    reiniciarse()

def AreaMetodoDiagonales():
    """ 
    Es una funcion la cual va a realizar toda la parte matematica 
    de la operacion y nos va a enviar el resultado del area conociendo sus dos lados 
    y el angulo entre estos 
    Recibe
    ------------
      Angulo: Recibe el valor de Angulo para poder utilzarlo posteriormente en el calculo del area
      lado1: En este nos recibe la variable lado1 para ser utilizado posteriormente
      lado2: En este nos recibe la variable lado2 para ser utilizado posteriormente
    ------------
       No retorna nigun parametro
    """
    #Creamos un bucle While para que se repita hasta que los datos ingresados sean validos
    while True:
        #Creamos la condicion para validar datos 
        try:
        #Creamos una funcion que nos permita ingresar la variable dato
            diagonal1=float(input("Ingrese el valor de la diagonal: "))
            #Revisamos que la condicion se cumpla 
        except ValueError:
            #Enviamos un mensaje de advertencia
            print("Debe ser un numero")
            #Continuamos si las condiciones se cumplen
            continue
        #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
        if diagonal1<=0:
            #Evaimos un mensaje de advertencia 
            print("Debe ser un numero positivo y diferente de 0")
            #Se crea la condicion para salir del bucle 
        else:
            #Salimos del bucle
            break
    while True:
        #Creamos la condicion para validar datos 
        try:
            #Creamos una funcion que nos permita ingresar la variable dato
            diagonal2=float(input("Ingrese el valor de la diagonal2: "))
                #Revisamos que la condicion se cumpla 
        except ValueError:
                #Enviamos un mensaje de advertencia
            print("Debe ser un numero")
                #Continuamos si las condiciones se cumplen
            continue
            #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
        if diagonal2<=0:
                #Evaimos un mensaje de advertencia 
            print("Debe ser un numero positivo y diferente de 0")
                #Se crea la condicion para salir del bucle 
        else:
                #Salimos del bucle
            break
    while True:
        #Creamos la condicion para validar datos 
        try:
            #Creamos una funcion que nos permita ingresar la variable dato
            angulo=math.radians(float(input("Ingrese el valor del angulo en Grados: ")))
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
    area=(diagonal1*diagonal2*math.sin(angulo))/2
    print("El Area es: ",area,"unidades^2")
    reiniciarse()

def Area():
    """ 
    Es una funcion la cual va a realizar toda la parte matematica 
    de la operacion y nos va a enviar el resultado del area lateral
    Recibe
    ------------
      No Recibe ningun parametro
    ------------
       AreaMetodoDiagonales():Ejecuta la funcion y todos los parametros de este
       AreaMetodoAngulo():Ejecuta la funcion y todos los parametros que este tenga 
       AreaMetodoTriangulos(): Ejecuta la función y todos lo parametros necesarios
    """
    
    print("Que tipo de Datos se conoce?")
    print("Su base y la altura : a")
    print("Sus lados y el angulo entre ellos: b") 
    print("Sus Diagonales y el angulo entre ellas: c")
    opcion=input("Elige una opcion:")
    if opcion=="a":
        return AreaMetodoBaseAltura()
    elif opcion=="b":
        return AreaMetodoNoAltura()
    elif opcion=="c":
        return AreaMetodoDiagonales()
    else:
        return Area()  

def Perimetro():
    """ 
    Es una funcion la cual va a realizar toda la parte matematica 
    de la operacion y nos va a enviar el resultado del area lateral
    Recibe
    ------------
      No Recibe ningun parametro
    ------------
       AreaMetodoDiagonales():Ejecuta la funcion y todos los parametros de este
       AreaMetodoAngulo():Ejecuta la funcion y todos los parametros que este tenga 
       AreaMetodoTriangulos(): Ejecuta la función y todos lo parametros necesarios
    """
    
    print("Que tipo de Datos se conoce?")
    print("Sus lados : a")
    print("altura y lateral y angulo entre estos : b") 
    
    opcion=input("Elige una opcion:")
    if opcion=="a":
        return PerimetroParaleloLados()
    elif opcion=="b":
        return PerimetroMetodoAngulo()
    
    else:
        return Perimetro()
def reiniciarse():
    """ 
    Es un funcion en la que preguntaremos al usuario si desea volver a ejecutar el 
    programa o si desea salir 
    Recibe
    ------------
      reiniciar:Es una variable en la cual elegiremos si deseamos continuar o si no
    ------------
       Menu(): Retorna la funcion si se cumple la condicion dada
       
    """
    #Se crea un variable que nos preguntara si deseamos volver a realizar el programa
    reiniciar=input("Realizar otra operacion? si (s) o no(n): ")
    #Se crea la condicion
    if reiniciar=="s":
    #Se regresa al inicio del progrma
        return Menu()
        
    #Se cre otra condicion
    elif(reiniciar=="n"):
    #Se escribe un mensaje
        print("Hasta Luego")
        return os.system("Pause")
    #Se termina con un condicion por si no es valido
    else:
        #Se pregunta de nuevo
        return reiniciarse()

def Menu():
    """ 
    Es una funcion la cual va a realizar toda la parte matematica 
    de la operacion y nos va a enviar el resultado del area lateral
    Recibe
    ------------
      No Recibe ningun parametro
    ------------
       AreaMetodoDiagonales():Ejecuta la funcion y todos los parametros de este
       AreaMetodoAngulo():Ejecuta la funcion y todos los parametros que este tenga 
       AreaMetodoTriangulos(): Ejecuta la función y todos lo parametros necesarios
    """
    
    print("Que Deseas hacer?")
    print("Area : a")
    print("Perimetros : b") 
    
    opcion=input("Elige una opcion:")
    if opcion=="a":
        return Area()
    elif opcion=="b":
        return Perimetro()
    
    else:
        return Menu()
#Programa principal 
if __name__ == '__main__':
#Mensaje de Bienvenida
        print("---Calcular el Area y Perimetro de un Paralelogramo---")
#Se llama la funcion principal 
Menu()
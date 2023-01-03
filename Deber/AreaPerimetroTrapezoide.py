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
def PerimetroTrapezoide():
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
            print("Debe ser un numero positivo")
            #Creamos una condicion de salida
        else:
            #Se sale del bucle
            break
    #Creamos un bucle While para que se repita hasta que los datos ingresados sean validos
    while True:
        #Creamos la condicion para validar datos 
        try:
        #Creamos una funcion que nos permita ingresar la variable dato
            lado3=float(input("Ingrese el valor del lado 3: "))
            #Revisamos que la condicion se cumpla 
        except ValueError:
            #Enviamos un mensaje de advertencia
            print("Debe ser un numero")
            #Continuamos si las condiciones se cumplen
            continue
        #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
        if lado3<=0:
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
            lado4=float(input("Ingrese el valor del lado 4:  "))
            #No nos permite avanzar si la condicion no se cumple
        except:
            #Se imprime la advertencia 
            print("Debe ser un numero")
            #Si se cumplen las condiciones se debe seguir 
            continue
        #Se crea una condicion en la que no podemos tener numeros negativos
        if lado4<=0:
            #Enviamos una advertencia 
            print("Debe ser un numero positivo")
            #Creamos una condicion de salida
        else:
            #Se sale del bucle
            break
    perimetro=lado1+lado2+lado3+lado4
    print("El perimetro es: ",perimetro,"unidades")
    reiniciarse()
def PerimetroTrapezoideSimetrico():
    """ 
    Es una funcion la cual va a realizar toda la parte matematica 
    de la operacion y nos va a enviar el resultado del Trapezoide si este Simetrico
    Recibe
    ------------
      lado1, lado2: Recibe los valores de los lados para usarlos despúes en el calculo
      del perimetro
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
            print("Debe ser un numero positivo")
            #Creamos una condicion de salida
        else:
            #Se sale del bucle
            break
    
    perimetro=2*(lado1+lado2)
    print("El perimetro es: ",perimetro,"unidades")
    reiniciarse()

def Perimetros():
    """ 
    Es una funcion la cual nos va a dar la opcion de elgir que tipo de Trapezoide es 
    y nos da la forma adecuada de operar 
    ------------
      No Recibe ningun Parametro
    ------------
       PerimetroTrapezoide(): Llama la funcion si esta es llamada
       PerimetroTrapezoideSimetrico(): LLama la funcion si esta es llamada junto con sus parametros
    """
    
    print("Que tipo de Trapezoide es?")
    print("Trapezoide Irregular: a")
    print("Trapezoide Regular: b")
    opcion=input("Elige una opcion:")
    if opcion=="a":
        return PerimetroTrapezoide()
    elif opcion=="b":
        return PerimetroTrapezoideSimetrico()
    else:
        return Perimetros()

def AreaMetodoTriangulos():
    """ 
    Es una funcion la cual va a realizar toda la parte matematica 
    de la operacion y nos va a enviar el resultado del area mediante el metodo de triangulos 
    en loa que se divide al trapezoide en dos triangulos para sacar su area 
    Recibe
    ------------
      diagonal: Recibe el valor de diagonal para poder utilzarlo posteriormente en el calculo del area
      altura1: En este nos recibe la variable altura1 para ser utilizado posteriormente en el area
      altura2: En este nos recibe la variable altura2 para ser utilizado posteriormente en el area
    ------------
       No retorna nigun parametro
    """
    #Creamos un bucle While para que se repita hasta que los datos ingresados sean validos
    while True:
        #Creamos la condicion para validar datos 
        try:
        #Creamos una funcion que nos permita ingresar la variable dato
            diagonal=float(input("Ingrese el valor de la diagonal: "))
            #Revisamos que la condicion se cumpla 
        except ValueError:
            #Enviamos un mensaje de advertencia
            print("Debe ser un numero")
            #Continuamos si las condiciones se cumplen
            continue
        #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
        if diagonal<=0:
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
            altura1=float(input("Ingrese el valor de la altura 1: "))
                #Revisamos que la condicion se cumpla 
        except ValueError:
                #Enviamos un mensaje de advertencia
            print("Debe ser un numero")
                #Continuamos si las condiciones se cumplen
            continue
            #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
        if altura1<=0:
                #Evaimos un mensaje de advertencia 
            print("Debe ser un numero positivo")
                #Se crea la condicion para salir del bucle 
        else:
                #Salimos del bucle
            break
    while True:
        #Creamos la condicion para validar datos 
        try:
            #Creamos una funcion que nos permita ingresar la variable dato
            altura2=float(input("Ingrese el valor de la altura 2: "))
                #Revisamos que la condicion se cumpla 
        except ValueError:
                #Enviamos un mensaje de advertencia
            print("Debe ser un numero")
                #Continuamos si las condiciones se cumplen
            continue
            #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
        if altura2<=0:
                #Evaimos un mensaje de advertencia 
            print("Debe ser un numero positivo")
                #Se crea la condicion para salir del bucle 
        else:
                #Salimos del bucle
            break
    area=((diagonal*altura1)/2)+((diagonal*altura2)/2)
    print("El Area es: ",area,"unidades^2")
    reiniciarse()
def AreaMetodoDiagonales():
    """ 
    Es una funcion la cual va a realizar toda la parte matematica 
    de la operacion y nos va a enviar el resultado del area mediante 
    el metodo de Diagonales en el cual sabiendo las dos diagonales 
    para enviar el resultado adecuado
    Recibe
    ------------
      diagonal1: Recibe el valor de la diagonal1 para poder utilzarlo posteriormente en el calculo del area
      diagonal2: Recibe la variable diagonal2 para ser utilizado posteriormente en el calculo del area
    ------------
       No retorna nigun parametro
    """
    #Creamos un bucle While para que se repita hasta que los datos ingresados sean validos
    while True:
        #Creamos la condicion para validar datos 
        try:
        #Creamos una funcion que nos permita ingresar la variable dato
            diagonal1=float(input("Ingrese el valor de la diagonal 1: "))
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
            diagonal2=float(input("Ingrese el valor de la diagonal 2: "))
                #Revisamos que la condicion se cumpla 
        except ValueError:
                #Enviamos un mensaje de advertencia
            print("Debe ser un numero y diferente de 0")
                #Continuamos si las condiciones se cumplen
            continue
            #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
        if diagonal2<=0:
                #Evaimos un mensaje de advertencia 
            print("Debe ser un numero positivo")
                #Se crea la condicion para salir del bucle 
        else:
                #Salimos del bucle
            break
        
    area=((diagonal1*diagonal2)/2)
    print("El Area es: ",area,"unidades^2")
    reiniciarse()
def AreaMetodoAngulo():
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

def AreaIrregular():
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
    print("Sus dos Diagonales: a")
    print("Sus lados y el Angulo entre ellos: b")
    print("Sus Diagonales y alturas: c")
    opcion=input("Elige una opcion:")
    if opcion=="a":
        return AreaMetodoDiagonales()
    elif opcion=="b":
        return AreaMetodoAngulo()
    elif opcion=="c":
        return AreaMetodoTriangulos()
    else:
        return AreaIrregular()   
def Area():
    """ 
    Es una funcion la cual va a darnos todas las opciones para calcular el area 
    Recibe
    ------------
      opcion: Nos Recibe la variable opcion para poder ejecutar la funcion necesaria
      Retorna
    ------------
       AreaMetodoTriangulos(): Recibe y ejecuta la funcion
       AreaIrregular():Recibe y ejecuta la funcion en la cual nos da las formas de operar este tipo de 
       trapezoides
    """
    
    print("Que tipo de Trapezoide es?")
    print("Trapezoide Irregular: a")
    print("Trapezoide Regular: b")
    opcion=input("Elige una opcion:")
    if opcion=="a":
        return AreaMetodoTriangulos()
    elif opcion=="b":
        return AreaIrregular()
    else:
        return Area()  

def reiniciarse():
    """ 
    Es un funcion en la que preguntaremos al usuario si desea volver a ejecutar el 
    programa o si desea salir 
    Recibe
    ------------
      reiniciar:Es una variable en la cual elegiremos si deseamos continuar o si no
    ------------
       Principal(): Retorna la funcion si se cumple la condicion dada
       
    """
    #Se crea un variable que nos preguntara si deseamos volver a realizar el programa
    reiniciar=input("Realizar otra operacion? si (s) o no(n): ")
    #Se crea la condicion
    if reiniciar=="s":
    #Se regresa al inicio del progrma
        return Principal()
        
    #Se cre otra condicion
    elif(reiniciar=="n"):
    #Se escribe un mensaje
        print("Hasta Luego")
        return os.system("Pause")
    #Se termina con un condicion por si no es valido
    else:
        #Se pregunta de nuevo
        return reiniciarse()

def Principal():
    print("Que vamos a Calcular")
    print("Area: a")
    print("Perimetro: b")
    opcion=input("Elige una opcion: ")
    if opcion=="a":
        return Area()
    elif opcion=="b":
        return Perimetros()
    else:
        return Principal() 


#Programa principal 
if __name__ == '__main__':
#Mensaje de Bienvenida
        print("---Calcular el Area y Perimetro de un Trapezoide---")
#Se llama la funcion principal 
Principal()

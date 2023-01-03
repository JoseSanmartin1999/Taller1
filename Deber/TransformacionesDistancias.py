"""
La transformaciones son basicas en la ingenieria, es normal que tengamos que convertir unidades 
grandes en pequeñas o viceversa para poder utilizar mejor el tiempo pues se reliza este de manera
inmediata
el siguiente programa prentende hacer esto de manera rapida 

Autores:
Jose Sanmartin
Verisión:
VER.0.1
"""
import os
def centimetroMetro():
    """ Es una funcion la cual nos validara ciertos datos y transformara el valor dado en libras
    a kilogramos 
    Recibe:
    ------------
      centimetros: Recibe el valor de centimetros que despues sera transformado a Metros
           
    Retorna:
    ------------
       no retorna ningun parametro
    """
#Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
    while True:
#Se inicia el try para de esta manera comprobar las condiciones 
        try:
#Pedimos que se ingrese  el valor a transformar 
            centimetros = float(input("Escribe el dato en centimetros(cm): "))
#Buscamos que no continue si existe algun tipo de error
        except ValueError:
#Escribir un mensaje en caso de error
            print("Debes escribir un número.")
#Si la condicion se cumple entonces continua con el siguiente paso
            continue
#Comprobar que no se ingresen numeros negativos en este caso
        if centimetros < 0:
#Escribir un mensaje en caso de que el numero no cumpla con la condicion dada
            print("Debes escribir un número positivo.")
#Si la condicion se cumple debe continuar
            continue
#Se escribe la condicion para salir del bucle 
        else:
#Se sale del bucle
            break
#Se da un valor constante a la variable de transformacion
    centiaMetros= float(0.01)
#Calculamos el resultado de la transformacion
    res1=centimetros*centiaMetros
#Se imprimen los resultados
    print(centimetros ,"centimetros(cm) es igual que",res1,"metros(m)")            
    reiniciarse()

def MetrosCentimetros():
    """Es una funcion la cual nos validara ciertos datos y transformara el valor dado en kilos
    a libras
    Recibe:
    ------------
      metros: Recibe el valor en metros y lo almacena para despues transformalo en otro
           
    Retorna:
    ------------
     No retorna nigun parametro 
    """
#Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
    while True:
#Se inicia el try para de esta manera comprobar las condiciones 
        try:
#Pedimos que se ingrese  el valor a transformar 
            metros=float(input("Ingrese el valor en metros(m)"))
#Buscamos que no continue si existe algun tipo de error
        except ValueError:
#Escribir un mensaje en caso de error
            print("Debes escribir un número.")
#Si la condicion se cumple entonces continua con el siguiente paso
            continue
#Comprobar que no se ingresen numeros negativos en este caso
        if metros < 0:
#Escribir un mensaje en caso de que el numero no cumpla con la condicion dada
            print("Debes escribir un número positivo.")
#Si la condicion se cumple debe continuar
            continue
#Se escribe la condicion para salir del bucle 
        else:
#Se sale del bucle
            break
#Se da un valor constante a la variable de transformacion
    metrosacenti=float(100)
#Calculamos el resultado de la transformacion
    res2=metros*metrosacenti
    print(metros,"metros(m) es igual a ", res2 ,"centimetros(cm)")
#Se imprimen los resultados
    reiniciarse()
def kilometrosMetros():
    """ Es una funcion la cual nos validara ciertos datos y transformara el valor dado en libras
    a gramos 
    Recibe:
    ------------
     Kilometros: Recibe el valor en kilometros para despues ser transformado en gramos
           
    Retorna:
    ------------
      No retorna nigun valor 
    """

    while True:
#Se inicia el try para de esta manera comprobar las condiciones 
        try:
#Pedimos que se ingrese  el valor a transformar 
            kilometros=float(input("Ingrese el valor en kilometros(km)"))
#Buscamos que no continue si existe algun tipo de error
        except ValueError:
#Escribir un mensaje en caso de error
            print("Debes escribir un número.")
#Si la condicion se cumple entonces continua con el siguiente paso
            continue
#Comprobar que no se ingresen numeros negativos en este caso
        if kilometros < 0:#Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
#Escribir un mensaje en caso de que el numero no cumpla con la condicion dada
            print("Debes escribir un número positivo.")
#Si la condicion se cumple entonces continua con el siguiente paso
            continue
#Dar la condicion de salida
        else:
#Se sale del bucle
            break
#Se da un valor constante a la variable de transformacion
    kilometrosametros=float(1000)
#Calculamos el resultado de la transformacion
    res6=kilometros*kilometrosametros
#Se imprimen los resultados
    print(kilometros,"kilometros(km) es igual a ", res6 ,"metros(m)")
    reiniciarse()
def metrosKilometros():
    """Es una funcion la cual nos validara ciertos datos y transformara el valor dado en gramos
    a libras
    Recibe:
    ------------
      metros: Recibe un valor en metros que despues se transformara en kilometros
           
    Retorna:
    ------------
     No retorna ningun valor 
    """
    #Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
    while True:
        #Se inicia el try para de esta manera comprobar las condiciones 
        try:
        #Pedimos que se ingrese  el valor a transformar     
            metros=float(input("Ingrese el valor en metros(m)"))
            #Si encuentra algun tipo de error no continua
        except ValueError:
            #Escribir un mensaje de notificacion
            print("Debes escribir un número.")
            #Si se cumplen las condiciones que continue 
            continue
        #Si el numero es negativo emplear un condicion
        if metros < 0:
            #Imprimir un mensaje de advertencia 
            print("Debes escribir un número positivo.")
            #Si todo se cumple continuar 
            continue
        #Crear una condicion de salida 
        else:
            #Salir del bucle
            break
        #Se programa al constante de cambio
    metrosakilo=float(0.001)
    #Se calcula el resultado
    res3=metros*metrosakilo
    #Imprimir los resultados
    print(metros,"gramos es igual a ", res3 ,"gramos")
    reiniciarse()
def kilometroCentimetro():
    """ Es una funcion la cual nos validara ciertos datos y transformara el valor dado en gramos
    a kilogramos 
    Recibe:
    ------------
      kilometros: es el valor que despues transformaremos en centimetros
           
    Retorna:
    ------------
       No retorna ningun parametro
    """
    #Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
    while True:
        #Se inicia el try para de esta manera comprobar las condiciones 
        try:
        #Pedimos que se ingrese  el valor a transformar     
            kilometros=float(input("Ingrese el valor en Kilometros(km)"))
            #Si encuentra algun tipo de error no continua
        except ValueError:
            #Escribir un mensaje de notificacion
            print("Debes escribir un número.")
            #Si se cumplen las condiciones que continue 
            continue
        #Si el numero es negativo emplear un condicion
        if kilometros < 0:
            #Imprimir un mensaje de advertencia 
            print("Debes escribir un número positivo.")
            #Si todo se cumple continuar 
            continue
        #Crear una condicion de salida 
        else:
            #Salir del bucle
            break
        #Se programa al constante de cambio
    kiloacenti=float(100000)
    #Se calcula el resultado
    res4=kilometros*kiloacenti
    #Imprimir los resultados
    print(kilometros,"kilometros(km) es igual a ", res4 ,"centimetros(cm)")
    reiniciarse()

def centimetrosKilometros():
    """ Es una funcion la cual nos validara ciertos datos y transformara el valor dado en kilogramos
    a gramos
    Recibe:
    ------------
    centimetros: Recibe el valor en centimetros para posteriormente transformarse en Kilometros
           
    Retorna:
    ------------
       No retorna ningun parametro
    """
    #Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
    while True:
        #Se inicia el try para de esta manera comprobar las condiciones 
        try:
        #Pedimos que se ingrese  el valor a transformar     
            centimetros=float(input("Ingrese el valor en centimetros(cm)"))
            #Si encuentra algun tipo de error no continua
        except ValueError:
            #Escribir un mensaje de notificacion
            print("Debes escribir un número.")
            #Si se cumplen las condiciones que continue 
            continue
        #Si el numero es negativo emplear un condicion
        if centimetros < 0:
            #Imprimir un mensaje de advertencia 
            print("Debes escribir un número positivo.")
            #Si todo se cumple continuar 
            continue
        #Crear una condicion de salida 
        else:
            #Salir del bucle
            break
        #Se programa al constante de cambio
    centiakilo=float(0.00001)
    #Se calcula el resultado
    res5=centimetros*centiakilo
    #Imprimir los resultados
    print(centimetros,"centimetros(cm) es igual a ", res5 ,"kilometros(km)")           
    reiniciarse()

def TransformacionesDistancias():
    """ Es una funcion la cual tomara todas las funciones antes creadas y validadas para poder realizar las 
    operaciones conrrespondintes e imprimir un resultado
    Recibe:
    ------------
    MetrosCentimetros(): Toma la funcion anteriormente creada para ejecutarla
    metrosKilometros(): Toma la funcion anteriormente creada para ejecutarla
    centimetroMetro()): Toma la funcion anteriormente creada para ejecutarla
    centimetrosKilometros(): Toma la funcion anteriormente creada para ejecutarla
    kilometroCentimetro(): Toma la funcion anteriormente creada para ejecutarla
    kilometrosMetros(): Toma la funcion anteriormente creada para ejecutarla  
    Retorna:
    ------------
      res1,re2,res3,res4,res5,res6:Devuelve los resultados y la variable que se busca en cada 
      funcion.
    """
    #Imprimir lista de opcion
    print("Transformar de metros(m) a centimetros(cm): opcion (1)")
    #Imprimir lista de opcion
    print("Transformar de metros(m) a kilometros(km): opcion (2)")
    #Imprimir lista de opcion
    print("Transformar de centimetros(cm) a metros(m): opcion (3)")
    #Imprimir lista de opcion
    print("Transformar de centimetros(cm) a kilometros(km): opcion (4)")
    #Imprimir lista de opcion
    print("Transformar de kilometros(km) a centimetros(cm): opcion (5)")
    #Imprimir lista de opcion
    print("Transformar de kilometros(km) a metros(m): opcion (6)")
    #Crear la variable opcion para ir a la indicada 
    while True:
    #Se busca un try para que se peude elegir entre las opciones indicadas
        try:
            #Creamos la interaccion con el usuario
            opcion=input("Ingrese la opcion que desea: ")
            #Creamos la excepcion 
        except:
            #Un mensaje para la expecion
            print("Opcion no valida")
            #Si se cumplen las condiciones se corre el programa
            continue
        #Si elgile la opcion 1
        if(opcion=="1"):
            #SE retorna la siguiente funncion
            return MetrosCentimetros()
            #Si elgile la opcion 
        elif(opcion=="2"):
            #SE retorna la siguiente funncion
            return metrosKilometros()
            #Si elgile la opcion 
        elif(opcion=="3"):
            #SE retorna la siguiente funncion
            return centimetroMetro()
            #Si elgile la opcion 
        elif(opcion=="4"):
            #SE retorna la siguiente funncion
            return centimetrosKilometros()
            #Si elgile la opcion 
        elif(opcion=="5"):
            #SE retorna la siguiente funncion
            return kilometroCentimetro()
            #Si elgile la opcion 
        elif(opcion=="6"):
            #SE retorna la siguiente funncion
            return kilometrosMetros()
        else:
            #SE retorna la siguiente funncion
            return TransformacionesDistancias()
        break
    
def reiniciarse():
    """ 
    Es un funcion en la que preguntaremos al usuario si desea volver a ejecutar el 
    programa o si desea salir 
    Recibe
    ------------
      reiniciar:Es una variable en la cual elegiremos si deseamos continuar o si no
    ------------
       TransformacionesDistancias(): Retorna la funcion si se cumple la condicion dada
       
    """
    #Se crea un variable que nos preguntara si deseamos volver a realizar el programa
    reiniciar=input("Relizamos otra operacion? si (s) o no(n): ")
    #Se crea la condicion
    if reiniciar=="s":
    #Se regresa al inicio del progrma
        return TransformacionesDistancias()
    #Se cre otra condicion
    elif(reiniciar=="n"):
    #Se escribe un mensaje
        print("Hasta Luego")
    #Se termina con un condicion por si no es valido
    else:
        #Se pregunta de nuevo
        return reiniciarse()
#Programa principal 
if __name__ == '__main__':
#Se llama la funcion Suma      
    TransformacionesDistancias()
#Se saldra del programa con un click
    os.system("Pause")
              

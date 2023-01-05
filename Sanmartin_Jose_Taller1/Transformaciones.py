"""
La transformaciones son basicas en la ingenieria, es normal que tengamos que convertir unidades 
grandes en pequeñas o viceversa para poder utilizar mejor las unidades o por simple regla
el siguiente programa prentende hacer esto de manera rapida 

Autores:
Jose Sanmartin
Verisión:
VER.0.1
"""
import os
def libras_a_kilos():
    """ Es una funcion la cual nos validara ciertos datos y transformara el valor dado en libras
    a kilogramos 
    Recibe:
    ------------
      libras: Recibe el valor de libras que despues sera transformado
           
    Retorna:
    ------------
       no retorna ningun parametro
    """
#Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
    while True:
#Se inicia el try para de esta manera comprobar las condiciones 
        try:
#Pedimos que se ingrese  el valor a transformar 
            libras = float(input("Escribe el dato en libras: "))
#Buscamos que no continue si existe algun tipo de error
        except ValueError:
#Escribir un mensaje en caso de error
            print("Debes escribir un número.")
#Si la condicion se cumple entonces continua con el siguiente paso
            continue
#Comprobar que no se ingresen numeros negativos en este caso
        if libras < 0:
#Escribir un mensaje en caso de que el numero no cumpla con la condicion dada
            print("Debes escribir un número positivo.")
#Si la condicion se cumple debe continuar
            continue
#Se escribe la condicion para salir del bucle 
        else:
#Se sale del bucle
            break
#Se da un valor constante a la variable de transformacion
    librasKilos= float(0.453592)
#Calculamos el resultado de la transformacion
    resultado=libras*librasKilos
#Se imprimen los resultados
    print(libras ,"libras es igual que",resultado,"Kilos")            
    reiniciarse()
def kilosalibras():
    """Es una funcion la cual nos validara ciertos datos y transformara el valor dado en kilos
    a libras
    Recibe:
    ------------
      kilos: Recibe el valor en kilos 
           
    Retorna:
    ------------
     No retorna nigun parametro 
    """
#Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
    while True:
#Se inicia el try para de esta manera comprobar las condiciones 
        try:
#Pedimos que se ingrese  el valor a transformar 
            kilos=float(input("Ingrese el valor en kilos"))
#Buscamos que no continue si existe algun tipo de error
        except ValueError:
#Escribir un mensaje en caso de error
            print("Debes escribir un número.")
#Si la condicion se cumple entonces continua con el siguiente paso
            continue
#Comprobar que no se ingresen numeros negativos en este caso
        if kilos < 0:
#Escribir un mensaje en caso de que el numero no cumpla con la condicion dada
            print("Debes escribir un número positivo.")
#Si la condicion se cumple debe continuar
            continue
#Se escribe la condicion para salir del bucle 
        else:
#Se sale del bucle
            break
#Se da un valor constante a la variable de transformacion
    kilolibra=float(2.20462)
#Calculamos el resultado de la transformacion
    res=kilos*kilolibra
    print(kilos,"kilos es igual a ", res ,"Libras")
#Se imprimen los resultados
    reiniciarse()
def librasgramos():
    """ Es una funcion la cual nos validara ciertos datos y transformara el valor dado en libras
    a gramos 
    Recibe:
    ------------
     libra: Recibe el valor en libras para despues ser transformado en gramos
           
    Retorna:
    ------------
      No retorna nigun valor 
    """

    while True:
#Se inicia el try para de esta manera comprobar las condiciones 
        try:
#Pedimos que se ingrese  el valor a transformar 
            libras=float(input("Ingrese el valor en libras"))
#Buscamos que no continue si existe algun tipo de error
        except ValueError:
#Escribir un mensaje en caso de error
            print("Debes escribir un número.")
#Si la condicion se cumple entonces continua con el siguiente paso
            continue
#Comprobar que no se ingresen numeros negativos en este caso
        if libras < 0:#Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
#Escribir un mensaje en caso de que el numero no cumpla con la condicion dada
            print("Debes escribir un número positivo.")
#Si la condicion se cumple entonces continua con el siguiente paso
            continue
#Dar la condicion de salida
        else:
#Se sale del bucle
            break
#Se da un valor constante a la variable de transformacion
    gramolibra=float(453.592)
#Calculamos el resultado de la transformacion
    res=libras*gramolibra
#Se imprimen los resultados
    print(libras,"libras es igual a ", res ,"gramos")
    reiniciarse()
def gramos_a_libras():
    """Es una funcion la cual nos validara ciertos datos y transformara el valor dado en gramos
    a libras
    Recibe:
    ------------
      gramos: Recibe un valor en gramos que despues se transformara en libras 
           
    Retorna:
    ------------
     No retorna ningun valor 
    """
    #Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
    while True:
        #Se inicia el try para de esta manera comprobar las condiciones 
        try:
        #Pedimos que se ingrese  el valor a transformar     
            gramos=float(input("Ingrese el valor en gramos"))
            #Si encuentra algun tipo de error no continua
        except ValueError:
            #Escribir un mensaje de notificacion
            print("Debes escribir un número.")
            #Si se cumplen las condiciones que continue 
            continue
        #Si el numero es negativo emplear un condicion
        if gramos < 0:
            #Imprimir un mensaje de advertencia 
            print("Debes escribir un número positivo.")
            #Si todo se cumple continuar 
            continue
        #Crear una condicion de salida 
        else:
            #Salir del bucle
            break
        #Se programa al constante de cambio
    libragramos=float(0.00220462)
    #Se calcula el resultado
    res=gramos*libragramos
    #Imprimir los resultados
    print(gramos,"gramos es igual a ", res ,"gramos")
    reiniciarse()
def gramos_a_kilos():
    """ Es una funcion la cual nos validara ciertos datos y transformara el valor dado en gramos
    a kilogramos 
    Recibe:
    ------------
      gramos: es el valor que despues transformaremos en gramos 
           
    Retorna:
    ------------
       No retorna ningun parametro
    """
    #Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
    while True:
        #Se inicia el try para de esta manera comprobar las condiciones 
        try:
        #Pedimos que se ingrese  el valor a transformar     
            gramos=float(input("Ingrese el valor en gramos"))
            #Si encuentra algun tipo de error no continua
        except ValueError:
            #Escribir un mensaje de notificacion
            print("Debes escribir un número.")
            #Si se cumplen las condiciones que continue 
            continue
        #Si el numero es negativo emplear un condicion
        if gramos < 0:
            #Imprimir un mensaje de advertencia 
            print("Debes escribir un número positivo.")
            #Si todo se cumple continuar 
            continue
        #Crear una condicion de salida 
        else:
            #Salir del bucle
            break
        #Se programa al constante de cambio
    kiloagramo=float(0.001)
    #Se calcula el resultado
    res=gramos*kiloagramo
    #Imprimir los resultados
    print(gramos,"gramos es igual a ", res ,"kilos")
    reiniciarse()

def kilos_a_gramos():
    """ Es una funcion la cual nos validara ciertos datos y transformara el valor dado en kilogramos
    a gramos
    Recibe:
    ------------
     kilogramos: Recibe el valor en kologrmaos para posteriormente transformarse en gramos 
           
    Retorna:
    ------------
       No retorna ningun parametro
    """
    #Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
    while True:
        #Se inicia el try para de esta manera comprobar las condiciones 
        try:
        #Pedimos que se ingrese  el valor a transformar     
            kilos=float(input("Ingrese el valor en kilos"))
            #Si encuentra algun tipo de error no continua
        except ValueError:
            #Escribir un mensaje de notificacion
            print("Debes escribir un número.")
            #Si se cumplen las condiciones que continue 
            continue
        #Si el numero es negativo emplear un condicion
        if kilos < 0:
            #Imprimir un mensaje de advertencia 
            print("Debes escribir un número positivo.")
            #Si todo se cumple continuar 
            continue
        #Crear una condicion de salida 
        else:
            #Salir del bucle
            break
        #Se programa al constante de cambio
    gramoakilos=float(1000)
    #Se calcula el resultado
    res=kilos*gramoakilos
    #Imprimir los resultados
    print(kilos,"kilos es igual a ", res ,"gramos")           
    reiniciarse()

def TransformacionesMasas():
    """ Es una funcion la cual tomara todas las funciones antes creadas y validadas para poder realizar las 
    operaciones conrrespondintes e imprimir un resultado
    Recibe:
    ------------
      libras_a_kilos(): Toma la funcion anteriormente creada para ejecutarla
      kilosalibras(): Toma la funcion anteriormente creada para ejecutarla
      librasgramos(): Toma la funcion anteriormente creada para ejecutarla
      gramos_a_libras(): Toma la funcion anteriormente creada para ejecutarla
      kilos_a_gramos(): Toma la funcion anteriormente creada para ejecutarla
      gramos_a_kilos(): Toma la funcion anteriormente creada para ejecutarla  
    Retorna:
    ------------
       kilo: retorna el valor de la vairable en kilos si es lo que se pidio
       libras = retorna el valor de la variable en libras si es lo que se pidio
       gramos= retorna el valor de la variable en gramos si es lo que se  pidio
    """

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
            return libras_a_kilos()
            #Si elgile la opcion 
        elif(opcion=="2"):
            #SE retorna la siguiente funncion
            return kilosalibras()
            #Si elgile la opcion 
        elif(opcion=="3"):
            #SE retorna la siguiente funncion
            return librasgramos()
            #Si elgile la opcion 
        elif(opcion=="4"):
            #SE retorna la siguiente funncion
            return gramos_a_libras()
            #Si elgile la opcion 
        elif(opcion=="5"):
            #SE retorna la siguiente funncion
            return kilos_a_gramos()
            #Si elgile la opcion 
        elif(opcion=="6"):
            #SE retorna la siguiente funncion
            return gramos_a_kilos()
        else:
            #SE retorna la siguiente funncion
            return TransformacionesMasas()
        break
    
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
        return TransformacionesMasas()
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
    #Imprimir lista de opcion
    print("Transformar de libras a kilos: opcion (1)")
    #Imprimir lista de opcion
    print("Transformar de kilos a libras: opcion (2)")
    #Imprimir lista de opcion
    print("Transformar de libras a gramos: opcion (3)")
    #Imprimir lista de opcion
    print("Transformar de gramos a libras: opcion (4)")
    #Imprimir lista de opcion
    print("Transformar de kilos a gramos: opcion (5)")
    #Imprimir lista de opcion
    print("Transformar de gramos a kilos: opcion (6)")
#Se llama la funcion necesaria     
    TransformacionesMasas()
#Se saldra del programa con un click
    os.system("Pause")
              

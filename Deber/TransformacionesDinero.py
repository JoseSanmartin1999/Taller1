"""
Es comun en mucho tipo de compras, o viajes que se quiera conocer cuanto dinero se deber llevar
en el siguiente programa abordaremos un poco de este tema desarrllando un programa que realize esto
de una manera sencilla y de facil comprension

Autores:
Jose Sanmartin
Verisión:
VER.0.1
"""
import os
def dolaresEuros():
    """ Es una funcion la cual nos validara ciertos datos y transformara el valor dado en dolares
    a Euros
    Recibe:
    ------------
      dolares: Recibe el valor de dolares que despues sera transformado
           
    Retorna:
    ------------
       no retorna ningun parametro
    """
#Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
    while True:
#Se inicia el try para de esta manera comprobar las condiciones 
        try:
#Pedimos que se ingrese  el valor a transformar 
            dolares = float(input("Escribe los dolares que va transformar: "))
#Buscamos que no continue si existe algun tipo de error
        except ValueError:
#Escribir un mensaje en caso de error
            print("Debes escribir un número.")
#Si la condicion se cumple entonces continua con el siguiente paso
            continue
#Comprobar que no se ingresen numeros negativos en este caso
        if dolares < 0:
#Escribir un mensaje en caso de que el numero no cumpla con la condicion dada
            print("Debes escribir un número positivo.")
#Si la condicion se cumple debe continuar
            continue
#Se escribe la condicion para salir del bucle 
        else:
#Se sale del bucle
            break
#Se da un valor constante a la variable de transformacion
    dolareneuro= float(0.94)
#Calculamos el resultado de la transformacion
    resultado=dolares*dolareneuro
#Se imprimen los resultados
    print(dolares ,"dolares es igual que",resultado,"Euros")            

def EuroaDolar():
    """Es una funcion la cual nos validara ciertos datos y transformara el valor dado en Euro
    a Dolar
    Recibe:
    ------------
      euro: Recibe el valor en euros para su conversion en dolares 
           
    Retorna:
    ------------
     No retorna nigun parametro 
    """
#Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
    while True:
#Se inicia el try para de esta manera comprobar las condiciones 
        try:
#Pedimos que se ingrese  el valor a transformar 
            euro=float(input("Ingrese el valor en euros: "))
#Buscamos que no continue si existe algun tipo de error
        except ValueError:
#Escribir un mensaje en caso de error
            print("Debes escribir un número.")
#Si la condicion se cumple entonces continua con el siguiente paso
            continue
#Comprobar que no se ingresen numeros negativos en este caso
        if euro < 0:
#Escribir un mensaje en caso de que el numero no cumpla con la condicion dada
            print("Debes escribir un número positivo.")
#Si la condicion se cumple debe continuar
            continue
#Se escribe la condicion para salir del bucle 
        else:
#Se sale del bucle
            break
#Se da un valor constante a la variable de transformacion
    euroadolar=float(1.06)
#Calculamos el resultado de la transformacion
    res=euro*euroadolar
    print(euro,"Euros es igual a ", res ,"Dolares($)")
#Se imprimen los resultados

def dolarYenes():
    """ Es una funcion la cual nos validara ciertos datos y transformara el valor dado en libras
    a gramos 
    Recibe:
    ------------
     dolar: Recibe el valor en dolares para despues ser transformado en yenes
           
    Retorna:
    ------------
      No retorna nigun valor 
    """

    while True:
#Se inicia el try para de esta manera comprobar las condiciones 
        try:
#Pedimos que se ingrese  el valor a transformar 
            dolar=float(input("Ingrese el valor en Dolares: "))
#Buscamos que no continue si existe algun tipo de error
        except ValueError:
#Escribir un mensaje en caso de error
            print("Debes escribir un número.")
#Si la condicion se cumple entonces continua con el siguiente paso
            continue
#Comprobar que no se ingresen numeros negativos en este caso
        if dolar < 0:#Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
#Escribir un mensaje en caso de que el numero no cumpla con la condicion dada
            print("Debes escribir un número positivo.")
#Si la condicion se cumple entonces continua con el siguiente paso
            continue
#Dar la condicion de salida
        else:
#Se sale del bucle
            break
#Se da un valor constante a la variable de transformacion
    dolarayen=float(133.69)
#Calculamos el resultado de la transformacion
    res=dolar*dolarayen
#Se imprimen los resultados
    print(dolar,"Dolare es igual a ", res ,"yenes")
    
def yenesadolar():
    """Es una funcion la cual nos validara ciertos datos y transformara el valor dado en gramos
    a libras
    Recibe:
    ------------
      yenes: Recibe un valor en yenes que despues se transformara en dolares
           
    Retorna:
    ------------
     No retorna ningun valor 
    """
    #Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
    while True:
        #Se inicia el try para de esta manera comprobar las condiciones 
        try:
        #Pedimos que se ingrese  el valor a transformar     
            yenes=float(input("Ingrese el valor en yenes: "))
            #Si encuentra algun tipo de error no continua
        except ValueError:
            #Escribir un mensaje de notificacion
            print("Debes escribir un número.")
            #Si se cumplen las condiciones que continue 
            continue
        #Si el numero es negativo emplear un condicion
        if yenes < 0:
            #Imprimir un mensaje de advertencia 
            print("Debes escribir un número positivo.")
            #Si todo se cumple continuar 
            continue
        #Crear una condicion de salida 
        else:
            #Salir del bucle
            break
        #Se programa al constante de cambio
    yenadolar=float(0.0075)
    #Se calcula el resultado
    res=yenes*yenadolar
    #Imprimir los resultados
    print(yenes,"yenes es igual a ", res ,"dolares")

def euroayen():
    """ Es una funcion la cual nos validara ciertos datos y transformara el valor dado en euros
    a yenes
    Recibe:
    ------------
      euro: es el valor que despues transformaremos en euros
           
    Retorna:
    ------------
       No retorna ningun parametro
    """
    #Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
    while True:
        #Se inicia el try para de esta manera comprobar las condiciones 
        try:
        #Pedimos que se ingrese  el valor a transformar     
            euro=float(input("Ingrese el valor en euro: "))
            #Si encuentra algun tipo de error no continua
        except ValueError:
            #Escribir un mensaje de notificacion
            print("Debes escribir un número.")
            #Si se cumplen las condiciones que continue 
            continue
        #Si el numero es negativo emplear un condicion
        if euro < 0:
            #Imprimir un mensaje de advertencia 
            print("Debes escribir un número positivo.")
            #Si todo se cumple continuar 
            continue
        #Crear una condicion de salida 
        else:
            #Salir del bucle
            break
        #Se programa al constante de cambio
    euroayenes=float(141.97)
    #Se calcula el resultado
    res=euro*euroayenes
    #Imprimir los resultados
    print(euro,"Euro es igual a ", res ,"yenes")

def yenaeuro():
    """ Es una funcion la cual nos validara ciertos datos y transformara el valor dado en yenes
    a euros
    Recibe:
    ------------
     yenes: se recibe el valor en yenes para su posterior transformacion
           
    Retorna:
    ------------
       No retorna ningun parametro
    """
    #Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
    while True:
        #Se inicia el try para de esta manera comprobar las condiciones 
        try:
        #Pedimos que se ingrese  el valor a transformar     
            yenes=float(input("Ingrese el valor en yenes: "))
            #Si encuentra algun tipo de error no continua
        except ValueError:
            #Escribir un mensaje de notificacion
            print("Debes escribir un número.")
            #Si se cumplen las condiciones que continue 
            continue
        #Si el numero es negativo emplear un condicion
        if yenes < 0:
            #Imprimir un mensaje de advertencia 
            print("Debes escribir un número positivo.")
            #Si todo se cumple continuar 
            continue
        #Crear una condicion de salida 
        else:
            #Salir del bucle
            break
        #Se programa al constante de cambio
    yenesaeuros=float(0.0070)
    #Se calcula el resultado
    res=yenes*yenesaeuros
    #Imprimir los resultados
    print(yenes,"yenes es igual a ", res ,"euros")     
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
    reiniciar=input("Realiza otra operacion?: Reiniciar(r) o no(n): ")
    #Se crea la condicion
    if reiniciar=="r":
    #Se regresa al inicio del progrma
        return Transformacion()
    #Se cre otra condicion
    elif(reiniciar=="n"):
    #Se escribe un mensaje
        print("Hasta Luego")
    #Se termina con un condicion por si no es valido
    else:
        #Se pregunta de nuevo
        return reiniciarse()          

def Transformacion():
    """ Es una funcion la cual tomara todas las funciones antes creadas y validadas para poder realizar las 
    operaciones conrrespondintes e imprimir un resultado
    Recibe:
    ------------
      dolaresEuros(): Toma la funcion anteriormente creada para ejecutarla
      EuroaDolar(): Toma la funcion anteriormente creada para ejecutarla
      dolarYenes(): Toma la funcion anteriormente creada para ejecutarla
     yenesadolar(): Toma la funcion anteriormente creada para ejecutarla
      euroayen(): Toma la funcion anteriormente creada para ejecutarla
      yenaeuro(): Toma la funcion anteriormente creada para ejecutarla  
    Retorna:
    ------------
       Dolar: retorna el valor de la variable en dolares si es lo que se pidio
       Euros: retorna el valor de la variable en euros si es lo que se pidio
       yenes= retorna el valor de la variable en yenes si es lo que se  pidio
    """
    #Imprimir lista de opcion
    print("Transformar de Dolares a Euros: opcion (1)")
    #Imprimir lista de opcion
    print("Transformar de Euro a Dolar: opcion (2)")
    #Imprimir lista de opcion
    print("Transformar de Dolar a Yenes: opcion (3)")
    #Imprimir lista de opcion
    print("Transformar de Yenes a Dolar: opcion (4)")
    #Imprimir lista de opcion
    print("Transformar de Euro a Yen: opcion (5)")
    #Imprimir lista de opcion
    print("Transformar de Yen a Euro: opcion (6)")
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
            return dolaresEuros()
            #Si elgile la opcion 
        elif(opcion=="2"):
            #SE retorna la siguiente funncion
            return EuroaDolar()
            #Si elgile la opcion 
        elif(opcion=="3"):
            #SE retorna la siguiente funncion
            return dolarYenes()
            #Si elgile la opcion 
        elif(opcion=="4"):
            #SE retorna la siguiente funncion
            return yenesadolar()
            #Si elgile la opcion 
        elif(opcion=="5"):
            #SE retorna la siguiente funncion
            return euroayen()
            #Si elgile la opcion 
        elif(opcion=="6"):
            #SE retorna la siguiente funncion
            return yenaeuro()
        else:
            #SE retorna la siguiente funncion
            return Transformacion()   

def transDinero():
    print("*--Bienvenido a tu cambio--*")
    Transformacion()
    print("Pregunta")
    reiniciarse()

#Programa principal 
if __name__ == '__main__':
#Se llama la funcion Suma      
    transDinero()
#Se saldra del programa con un click
    os.system("Pause")
              

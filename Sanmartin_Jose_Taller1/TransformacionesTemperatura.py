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
def celciusFarenheit():
    """ Es una funcion la cual nos validara ciertos datos y transformara el valor dado en celcius
    a Farenheir
    Recibe:
    ------------
      Celcius: Recibe el valor en Celcius que despues sera transformado a Farenheit
           
    Retorna:
    ------------
       no retorna ningun parametro
    """
#Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
    while True:
#Se inicia el try para de esta manera comprobar las condiciones 
        try:
#Pedimos que se ingrese  el valor a transformar 
            celcius = float(input("Escribe el valor en grados Celcius: "))
#Buscamos que no continue si existe algun tipo de error
        except ValueError:
#Escribir un mensaje en caso de error
            print("Debes escribir un número.")
#Si la condicion se cumple entonces continua con el siguiente paso
            continue

#Se escribe la condicion para salir del bucle 
        else:
#Se sale del bucle
            break
#Calculamos el resultado de la transformacion
    celciusaFaren=((9/5)*celcius)+32
    
    
#Se imprimen los resultados
    print(celcius ,"Celcius es igual que",celciusaFaren,"Farenheit")            
    reiniciarse()
def FarenheitCelcius():
    """Es una funcion la cual nos validara ciertos datos y transformara el valor dado en Farenheit
    a Celcius
    Recibe:
    ------------
      Farenheit: Recibe el valor en Farenheit para su conversion en celcius
           
    Retorna:
    ------------
     No retorna nigun parametro 
    """
#Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
    while True:
#Se inicia el try para de esta manera comprobar las condiciones 
        try:
#Pedimos que se ingrese  el valor a transformar 
            faren=float(input("Ingrese el valor en Farenheit: "))
#Buscamos que no continue si existe algun tipo de error
        except ValueError:
#Escribir un mensaje en caso de error
            print("Debes escribir un número.")
#Si la condicion se cumple entonces continua con el siguiente paso
            continue
#Comprobar que no se ingresen numeros negativos en este caso
       
#Se escribe la condicion para salir del bucle 
        else:
#Se sale del bucle
            break
#Se da un valor constante a la variable de transformacion
    farenaCelcius=(faren-32)*(5/9)

    print(faren,"Farenheit es igual a ", farenaCelcius ,"Celcius")
#Se imprimen los resultados
    reiniciarse()

def CelciusKelvin():
    """ Es una funcion la cual nos validara ciertos datos y transformara el valor dado en Celcius
    a Kelvin
    Recibe:
    ------------
     Celcius: Recibe el valor en Celcius para despues ser transformado en Kelvin
           
    Retorna:
    ------------
      No retorna nigun valor 
    """

    while True:
#Se inicia el try para de esta manera comprobar las condiciones 
        try:
#Pedimos que se ingrese  el valor a transformar 
            celcius=float(input("Ingrese el valor en Celcius: "))
#Buscamos que no continue si existe algun tipo de error
        except ValueError:
#Escribir un mensaje en caso de error
            print("Debes escribir un número.")
#Si la condicion se cumple entonces continua con el siguiente paso
            continue

#Dar la condicion de salida
        else:
#Se sale del bucle
            break

#Calculamos el resultado de la transformacion
    celakelv=celcius+273.15
#Se imprimen los resultados
    print(celcius,"Celcius es igual a ", celakelv ,"Kelvin")
    
    reiniciarse()

def KelvinCelcius():
    """Es una funcion la cual nos validara ciertos datos y transformara el valor dado en Kelvin
    a Celcius
    Recibe:
    ------------
      kelvin: Recibe un valor en kelvin que despues se transformara en celcius
           
    Retorna:
    ------------
     No retorna ningun valor 
    """
    #Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
    while True:
        #Se inicia el try para de esta manera comprobar las condiciones 
        try:
        #Pedimos que se ingrese  el valor a transformar     
            kelvin=float(input("Ingrese el valor en kelvin: "))
            #Si encuentra algun tipo de error no continua
        except ValueError:
            #Escribir un mensaje de notificacion
            print("Debes escribir un número.")
            #Si se cumplen las condiciones que continue 
            continue
            
        #Crear una condicion de salida 
        else:
            #Salir del bucle
            break
        #Se programa al constante de cambio
   
    kelacel=kelvin-273
    #Imprimir los resultados
    print(kelvin,"Kelvin es igual a ", kelacel ,"Celcius")
    reiniciarse()

def FarenKelvin():
    """ Es una funcion la cual nos validara ciertos datos y transformara el valor dado en Farenheit
    a Kelvin
    Recibe:
    ------------
      faren: es el valor que despues transformaremos en grados Kelvin con la operacion adecuada
           
    Retorna:
    ------------
       No retorna ningun parametro
    """
    #Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
    while True:
        #Se inicia el try para de esta manera comprobar las condiciones 
        try:
        #Pedimos que se ingrese  el valor a transformar     
            faren=float(input("Ingrese el valor en Farenheit: "))
            #Si encuentra algun tipo de error no continua
        except ValueError:
            #Escribir un mensaje de notificacion
            print("Debes escribir un número.")
            #Si se cumplen las condiciones que continue 
            continue
        #Si el numero es negativo emplear un condicion
       
        #Crear una condicion de salida 
        else:
            #Salir del bucle
            break
        #Se programa al constante de cambio
    
    FarenaKelv=((faren-32)*(5/9))+273
    #Imprimir los resultados
    print(faren,"Faren es igual a ", FarenaKelv ,"Kelvin")
    reiniciarse()

def KelvFaren():
    """ Es una funcion la cual nos validara ciertos datos y transformara el valor dado en Kelvin
    a Faren
    Recibe:
    ------------
     kelv: se recibe el valor en kelvin para su posterior transformacion en Farenheint
           
    Retorna:
    ------------
       No retorna ningun parametro
    """
    #Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
    while True:
        #Se inicia el try para de esta manera comprobar las condiciones 
        try:
        #Pedimos que se ingrese  el valor a transformar     
            kelv=float(input("Ingrese el valor en Kelvin: "))
            #Si encuentra algun tipo de error no continua
        except ValueError:
            #Escribir un mensaje de notificacion
            print("Debes escribir un número.")
            #Si se cumplen las condiciones que continue 
            continue
       
        #Crear una condicion de salida 
        else:
            #Salir del bucle
            break
      
    #Se calcula el resultado
    kelvafaren=((kelv-273.15)*(9/5))+32
    #Imprimir los resultados
    print(kelv,"Kelvin es igual a ", kelvafaren ,"Farenheit")  
    reiniciarse()   
def reiniciarse():
    """ 
    Es un funcion en la que preguntaremos al usuario si desea volver a ejecutar el 
    programa o si desea salir 
    Recibe
    ------------
      reiniciar:Es una variable en la cual elegiremos si deseamos continuar o si no
    ------------
       Transformacion(): Retorna la funcion si se cumple la condicion dada
       
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
    celciusFarenheit(): Toma la funcion anteriormente creada para ejecutarla
    CelciusKelvin(): Toma la funcion anteriormente creada para ejecutarla
    FarenheitCelcius(): Toma la funcion anteriormente creada para ejecutarla
    FarenKelvin(): Toma la funcion anteriormente creada para ejecutarla
     KelvFaren(): Toma la funcion anteriormente creada para ejecutarla
    KelvinCelcius(): Toma la funcion anteriormente creada para ejecutarla  
    Retorna:
    ------------
       Celcius: retorna el valor de la variable en Celcius si es lo que se pidio
       Farenheit: retorna el valor de la variable en Farenheit si es lo que se pidio
       Kelvin= retorna el valor de la variable en Kelvin si es lo que se  pidio
    """
    #Imprimir lista de opcion
    print("Transformar de Celcius(C) a Farenheit(F): opcion (1)")
    #Imprimir lista de opcion
    print("Transformar de Celcius(C) a Kelvin(K): opcion (2)")
    #Imprimir lista de opcion
    print("Transformar de Farenheit(F) a Celcius(C): opcion (3)")
    #Imprimir lista de opcion
    print("Transformar de Farenheit(F) a Kelvin(K) opcion (4)")
    #Imprimir lista de opcion
    print("Transformar de Kelvin(K) a Farenheit(F) opcion (5)")
    #Imprimir lista de opcion
    print("Transformar de Kelvin(K) a Celcius(C): opcion (6)")
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
            return celciusFarenheit()
            #Si elgile la opcion 
        elif(opcion=="2"):
            #SE retorna la siguiente funncion
            return CelciusKelvin()
            #Si elgile la opcion 
        elif(opcion=="3"):
            #SE retorna la siguiente funncion
            return FarenheitCelcius()
            #Si elgile la opcion 
        elif(opcion=="4"):
            #SE retorna la siguiente funncion
            return FarenKelvin()
            #Si elgile la opcion 
        elif(opcion=="5"):
            #SE retorna la siguiente funncion
            return KelvFaren()
            #Si elgile la opcion 
        elif(opcion=="6"):
            #SE retorna la siguiente funncion
            return KelvinCelcius()
        else:
            #SE retorna la siguiente funncion
            return Transformacion()   



#Programa principal 
if __name__ == '__main__':
#Se llama la funcion Suma      
   Transformacion()
#Se saldra del programa con un click
os.system("Pause")
              
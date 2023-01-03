"""
Es comun en mucho tipo de compras, o viajes que se quiera conocer cuanto dinero se deber llevar
en el siguiente programa abordaremos un poco de este tema desarrllando un programa que realize esto
de una manera sencilla y de facil comprension

Autores:
Jose Sanmartin
Verisión:
VER.0.1
"""
#importo la biblioteca que se necesita 
import os
def dolaresYuan():
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
    dolarenyuan= float(0.14)
#Calculamos el resultado de la transformacion
    resultado=dolares*dolarenyuan
#Se imprimen los resultados
    print(dolares ,"dolares es igual que",resultado,"Renminbi")            

def yuanDolar():
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
            yuan=float(input("Ingrese el valor en Renminbi: "))
#Buscamos que no continue si existe algun tipo de error
        except ValueError:
#Escribir un mensaje en caso de error
            print("Debes escribir un número.")
#Si la condicion se cumple entonces continua con el siguiente paso
            continue
#Comprobar que no se ingresen numeros negativos en este caso
        if yuan < 0:
#Escribir un mensaje en caso de que el numero no cumpla con la condicion dada
            print("Debes escribir un número positivo.")
#Si la condicion se cumple debe continuar
            continue
#Se escribe la condicion para salir del bucle 
        else:
#Se sale del bucle
            break
#Se da un valor constante a la variable de transformacion
    yuanadolar=float(6.96)
#Calculamos el resultado de la transformacion
    res=yuan*yuanadolar
    print(yuan,"Yuanes es igual a ", res ,"Dolares($)")
#Se imprimen los resultados

def dolarPesocolombiano():
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
    dolarapeso=float(4773.49)
#Calculamos el resultado de la transformacion
    res=dolar*dolarapeso
#Se imprimen los resultados
    print(dolar,"Dolares es igual a ", res ,"Pesos colombianos")
    
def pesoColadolar():
    """Es una funcion la cual nos validara ciertos datos y transformara el valor dado en gramos
    a libras
    Recibe:
    ------------
      peso: Recibe un valor en yenes que despues se transformara en dolares
           
    Retorna:
    ------------
     No retorna ningun valor 
    """
    #Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
    while True:
        #Se inicia el try para de esta manera comprobar las condiciones 
        try:
        #Pedimos que se ingrese  el valor a transformar     
            peso=float(input("Ingrese el valor en pesosCol: "))
            #Si encuentra algun tipo de error no continua
        except ValueError:
            #Escribir un mensaje de notificacion
            print("Debes escribir un número.")
            #Si se cumplen las condiciones que continue 
            continue
        #Si el numero es negativo emplear un condicion
        if peso < 0:
            #Imprimir un mensaje de advertencia 
            print("Debes escribir un número positivo.")
            #Si todo se cumple continuar 
            continue
        #Crear una condicion de salida 
        else:
            #Salir del bucle
            break
        #Se programa al constante de cambio
    pesoadolar=float(0.00021)
    #Se calcula el resultado
    res=peso*pesoadolar
    #Imprimir los resultados
    print(peso,"Peso Colombiano es igual a ", res ,"dolares")

def yuanaPeso():
    """ Es una funcion la cual nos validara ciertos datos y transformara el valor dado en euros
    a yenes
    Recibe:
    ------------
      yuan: es el valor que despues transformaremos en euros
           
    Retorna:
    ------------
       No retorna ningun parametro
    """
    #Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
    while True:
        #Se inicia el try para de esta manera comprobar las condiciones 
        try:
        #Pedimos que se ingrese  el valor a transformar     
            yuan=float(input("Ingrese el valor en yuanes: "))
            #Si encuentra algun tipo de error no continua
        except ValueError:
            #Escribir un mensaje de notificacion
            print("Debes escribir un número.")
            #Si se cumplen las condiciones que continue 
            continue
        #Si el numero es negativo emplear un condicion
        if yuan < 0:
            #Imprimir un mensaje de advertencia 
            print("Debes escribir un número positivo.")
            #Si todo se cumple continuar 
            continue
        #Crear una condicion de salida 
        else:
            #Salir del bucle
            break
        #Se programa al constante de cambio
    yuanapeso=float(685.44)
    #Se calcula el resultado
    res=yuan*yuanapeso
    #Imprimir los resultados
    print(yuan,"Yuanes es igual a ", res ,"renminbi")

def pesoaYuan():
    """ Es una funcion la cual nos validara ciertos datos y transformara el valor dado en yenes
    a euros
    Recibe:
    ------------
     peso: se recibe el valor en yenes para su posterior transformacion
           
    Retorna:
    ------------
       No retorna ningun parametro
    """
    #Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
    while True:
        #Se inicia el try para de esta manera comprobar las condiciones 
        try:
        #Pedimos que se ingrese  el valor a transformar     
            peso=float(input("Ingrese el valor en peso: "))
            #Si encuentra algun tipo de error no continua
        except ValueError:
            #Escribir un mensaje de notificacion
            print("Debes escribir un número.")
            #Si se cumplen las condiciones que continue 
            continue
        #Si el numero es negativo emplear un condicion
        if peso < 0:
            #Imprimir un mensaje de advertencia 
            print("Debes escribir un número positivo.")
            #Si todo se cumple continuar 
            continue
        #Crear una condicion de salida 
        else:
            #Salir del bucle
            break
        #Se programa al constante de cambio
    pesoayuan=float(0.0015)
    #Se calcula el resultado
    res=peso*pesoayuan
    #Imprimir los resultados
    print(peso,"yenes es igual a ", res ,"renminbi")     
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
    print("Transformar de Dolares a Renminbi(RMB) : opcion (1)")
    #Imprimir lista de opcion
    print("Transformar de Dolares a Pesos Colombianos: opcion (2)")
    #Imprimir lista de opcion
    print("Transformar de Renminbi(RMB) a Pesos Colombianos: opcion (3)")
    #Imprimir lista de opcion
    print("Transformar de Renminbi(RMB) a Dolar: opcion (4)")
    #Imprimir lista de opcion
    print("Transformar de Peso Colombiano a Renminbi(RMB): opcion (5)")
    #Imprimir lista de opcion
    print("Transformar de Peso Colombiano a Dolar: opcion (6)")
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
            return dolaresYuan()
            #Si elgile la opcion 
        elif(opcion=="2"):
            #SE retorna la siguiente funncion
            return dolarPesocolombiano()
            #Si elgile la opcion 
        elif(opcion=="3"):
            #SE retorna la siguiente funncion
            return yuanaPeso()
            #Si elgile la opcion 
        elif(opcion=="4"):
            #SE retorna la siguiente funncion
            return yuanDolar()
            #Si elgile la opcion 
        elif(opcion=="5"):
            #SE retorna la siguiente funncion
            return pesoaYuan()
            #Si elgile la opcion 
        elif(opcion=="6"):
            #SE retorna la siguiente funncion
            return pesoColadolar()
        else:
            #SE retorna la siguiente funncion
            return Transformacion()   

def transDineroRMB():
    print("*--Bienvenido a tu cambio--*")
    Transformacion()
    print("Pregunta")
    reiniciarse()

#Programa principal 
if __name__ == '__main__':
#Se llama la funcion Suma      
    transDineroRMB()
#Se saldra del programa con un click
    os.system("Pause")
              

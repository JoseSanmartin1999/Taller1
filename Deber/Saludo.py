"""
Se busca un programa el cual cree una interaccion simple con el usuario preguntandole algunos datos 
y retornar un saludo para este 

Autores:
Jose Sanmartin
Verisión:
VER.0.1
"""
#Se exporta la libreria os para poder salri des sistema con un click despues 
import os
def edad():
    """ 
    Es un funcion en la que preguntaremos al usuario su edad y definiremos si es 
    mayor o menor de edad, tambien la validad para evitar que ponga alguna caracter
    que no corresponda 
    Recibe
    ------------
      edad:Recibe la  variable edad y la alamcena hasta que se neceiste 
    ------------
       No retorna nigun parametro
    """
    #para que pida que se ingrese un nuevo valor hasta que agregue uno valido
    while True:
        #comprobar si el valor dado es un entero.
        try:
            #Se pide ingresar el valor 
            edad = int(input("¿Cual es Tu edad?: "))
            #Comprobar si el valor ingresado es un entero
        except ValueError:
            #Enviar un mensaje de advertencia
            print("Debes escribir un número.")
            #Si s cumplen la condiciones se continua
            continue
        #Se comprueba que no se pongan valores negaticos
        if edad < 0:
            #Enviar un mensaje de advertencia
            print("Debes escribir un número positivo.")
            #Si se cumple las condiciones se continua 
            continue
        #Se crea una condiccion que salga del bucle
        else:
            #Se sale del bucle 
            break
        #Se crea una condicion si es mayor de edad
    if edad<=17:
        #Se imprime el mensaje
        print("Aun eres menor de edad")
        #Se crea otra condicion para los mayores de edad
    else:
        #Se imprime el mensaje
        print("Eres mayor de edad")

def nombre():
    """ 
    Es un funcion en la que preguntaremos al usuario su nombre para almacernarlo
    y saludarlo despues 
    Recibe
    ------------
      Nombre:Recibe la  variable edad y la alamcena hasta que se neceiste 
    ------------
       No retorna nigun parametro
    """
    #Se pide el nombre del usuario
    nombre=input("Hola como te llamas?: ")
    #Se imprime el saludo con el nombre
    print("Hola",nombre,"Me llamo Jose")

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
    reiniciar=input("Me quieres presentara alguien mas si (s) o no(n): ")
    #Se crea la condicion
    if reiniciar=="s":
    #Se regresa al inicio del progrma
        return saludar()
    #Se cre otra condicion
    elif(reiniciar=="n"):
    #Se escribe un mensaje
        print("Hasta Luego")
    #Se termina con un condicion por si no es valido
    else:
        #Se pregunta de nuevo
        return reiniciarse()

def saludar():
    """ 
    Es un funcion en la que se compilaran todas las funciones para realizar el
    saludo correspondiente
    Recibe
    ------------
      No recibe ningun parametro
      Retorna
    ------------
       nombre():Retorna el saludo con el nombre del usuario
       edad(): Retorna si esl usuario es mayor o menor de edad
       reiniciarse(): Retorna la funcion reiniciar en caso que se quiere volver a ejecutar todo
       
    """
    #Se inicia la interaccion con usuario
    print("Hola vamos a conocernos")
    #Se llama a la funcion adecuada
    nombre()
    #Se crea interaccion
    print("Una Pregunta mas")
    #Se llama a la funcion adecuada
    edad()
    #Interaccion
    print("Una Pregunta mas")
    #Funcion adecuada
    reiniciarse()

#Programa principal 
if __name__ == '__main__':
#Se llama la funcion Suma      
    saludar()
#Se saldra del programa con un click
    os.system("Pause")
"""
El siguiente programa esta diseñado para devolver el valor en años, dias y meses dependiendo
de la variable que se ingrese se van a dar las opciones de transforamcion. Esto puede ayudar 
a calcular periodos de tiempo, y es posible ampliar a otro tipo de unidades

Autores:
Jose Sanmartin
Verisión:
VER.0.1
"""
import os
def Dias():
    """ 
    Es una funcion la cual recibe los dias, y los transforma en años, meses,semanas
    Recibe:
    ------------
     dias: Recibe el valor en dia que despues sera transformado a sus equivalaente en años, meses y semanas
           
    Retorna:
    ------------
       no retorna ningun parametro
    """
#Iniciamos un blucle While para que se repita hasta que las condiciones sean las adecuadas para seguir
    while True:
#Se inicia el try para de esta manera comprobar las condiciones 
        try:
#Pedimos que se ingrese  el valor a transformar 
            dias= float(input("Escribe la cantidad de Dias: "))
#Buscamos que no continue si existe algun tipo de error
        except ValueError:
#Escribir un mensaje en caso de error
            print("Debes escribir un número.")
#Si la condicion se cumple entonces continua con el siguiente paso
            continue
        if dias<0:
            #Evaimos un mensaje de advertencia 
            print("Debe ser un numero positivo")
            #Se crea la condicion para salir del bucle 
        else:
            #Salimos del bucle
            break
#Se sale del bucle
            
#Calculamos el resultado de la transformacion
    años=round(dias/365.256363004)
    meses=round((dias*12)/365.256363004)
    semanas=round(dias/7)
    print("La cantidad en años es: ", años)
    print("La cantidad en meses es: ", meses)
    print("La cantidad en semanas es:", semanas)
    print("La cantidad en dias es:", dias)
    reiniciarse()

def reiniciarse():
    """ 
    Es un funcion en la que preguntaremos al usuario si desea volver a ejecutar el 
    programa o si desea salir 
    Recibe
    ------------
      reiniciar:Es una variable en la cual elegiremos si deseamos continuar o si no
    ------------
       tipoDato(): Retorna la funcion si se cumple la condicion dada
       
    """
    #Se crea un variable que nos preguntara si deseamos volver a realizar el programa
    reiniciar=input("Quieres realizar otra operacion si (s) o no(n): ")
    #Se crea la condicion
    if reiniciar=="s":
    #Se regresa al inicio del progrma
        return tipoDato()
    #Se cre otra condicion
    elif(reiniciar=="n"):
    #Se escribe un mensaje
        print("Hasta Luego")
        os.system("Pause")

    #Se termina con un condicion por si no es valido
    else:
            #Se pregunta de nuevo
            return reiniciarse()
def tipoDato():
    """ 
   Es una funcion que recopila las funciones anteriores y las llama dependiendo de las condidciones 
    que se den, es decir son llamadas por medio de condiciones 
    Recibe
    ------------
      Dias(): Recibe la funcion y la ejecuta si las condiciones se dan
     
      Retorna
    ------------
      
       semanas: Devuelve el valor en semanas de la  númerica 
       meses:Devuelve el valor en meses de la variable númerica 
       años;Devuelve el valor en años de la variable númerica 
       
    """
    print("Que tipo de Dato va ingresar")
    print("Ingresar Dias: Opcion 1")
  
    #Escribe las opciones que tenemos 
    opciones=["1"]
    #Nos da un valor inical de la variable para que se pueda llamar mas tarde 
    opcion=0
    #Creamos un bucle While 
    while (opcion) not in opciones:
        #Se crea la condicion
        try:
            #Se crea la variable opcion
            opcion=input("Elija una opcion: ")
            #Se espera que se cumpla la funcion
        except:
            print("Opcion no valida")
        #Se crea la condición para llamar la varible Dias()   
        if opcion == "1":
            #retorna la funcion necesitada
            return Dias()
     
        else: 
            #retorna la funcion necesitada
            return tipoDato()
#Programa principal 
if __name__ == '__main__':
#Se llama la funcion Principal    
    tipoDato()

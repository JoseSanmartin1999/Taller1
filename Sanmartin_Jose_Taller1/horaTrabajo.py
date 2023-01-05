"""
Se busca un programa el cual calcule de manera sencilla el sueldo de algun trabajador 
ingresando el valor de su hora de trabajo y las horas que este trabajo
esto puede ser util para empresas o personas que trabajan bajo contrato

Autores:
Jose Sanmartin
Verisión:
VER.0.1
"""
#Se importa las bibliotecas necesarias para el programa
import os
def horasTrabajo():
    """ 
    Es un funcion en la cual se reciben las variables y se calcula el sueldo de la persona 
    que se solicita para imprimir estos resultados despúes o cuando sea necesario
    Recibe
    ------------
      horas: Recibe las horas que se trabaja
      sueldo: Recibe el costo de la hora trabajada
    ------------
       sueldototal: Imprime el Sueldo total tomando en cuenta los datos ingresados
       
    """
    while True:
            #comprobar si el valor dado es un entero.
            try:
                #Se pide ingresar el valor 
                horas = float(input("Ingresar las horas de trabajo : "))
                #Comprobar si el valor ingresado es un entero
            except ValueError:
                #Enviar un mensaje de advertencia
                print("Debes escribir un número.")
                #Si s cumplen la condiciones se continua
                continue
            #Se comprueba que no se pongan valores negaticos
            if horas < 0:
                #Enviar un mensaje de advertencia
                print("Debes escribir un número positivo.")
                #Si se cumple las condiciones se continua 
                continue
            #Se crea una condiccion que salga del bucle
            else:
                #Se sale del bucle 
                break
            #Se crea una condicion si es mayor de edad
    while True:
            #comprobar si el valor dado es un entero.
            try:
                #Se pide ingresar el valor 
                sueldo = float(input("Ingresar el costo de la hora de trabajo en dolares($): "))
                #Comprobar si el valor ingresado es un entero
            except ValueError:
                #Enviar un mensaje de advertencia
                print("Debes escribir un número.")
                #Si s cumplen la condiciones se continua
                continue
            #Se comprueba que no se pongan valores negaticos
            if horas <= 0:
                #Enviar un mensaje de advertencia
                print("Debes escribir un número positivo y no puede ser 0")
                #Si se cumple las condiciones se continua 
                continue
            #Se crea una condiccion que salga del bucle
            else:
                #Se sale del bucle 
                break
            #Se crea una condicion si es mayor de edad
    sueldototal=horas*sueldo
    print("Las horas de trabajo total son: " ,horas)
    print("El costo por hora es $: ", sueldo)
    print("El Sueldo a pagar es  $", sueldototal)
    reiniciarse()

def reiniciarse():
    """ 
    Es un funcion en la que preguntaremos al usuario si desea volver a ejecutar el 
    programa o si desea salir 
    Recibe
    ------------
      reiniciar:Es una variable en la cual elegiremos si deseamos continuar o si no
    ------------
       horasTrabajo(): Retorna la funcion si se cumple la condicion dada
       
    """
    #Se crea un variable que nos preguntara si deseamos volver a realizar el programa
    reiniciar=input("Quieres calcular otra sueldo? si (s) o no(n): ")
    #Se crea la condicion
    if reiniciar=="s":
    #Se regresa al inicio del progrma
        return horasTrabajo()
    #Se cre otra condicion
    elif(reiniciar=="n"):
    #Se escribe un mensaje
        print("Hasta Luego")
        return os.system("Pause")
    #Se termina con un condicion por si no es valido
    else:
        #Se pregunta de nuevo
        return reiniciarse()

#Programa principal 
if __name__ == '__main__':
#El programa saluda 
    print("Hola Bienvenido por favor ingresa los siguiente datos")
#Se llama la funcion Suma      
horasTrabajo()

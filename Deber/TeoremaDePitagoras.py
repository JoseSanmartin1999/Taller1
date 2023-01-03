"""
El teorema de Pitagoras nos permite encontrar el lado faltaante de un triangulo rectangulo sea este 
hipotenusas o alguno de sus catetos. Para ello es necesario saber al menos dos datos de este, en el 
siguiente programa buscamos simular esto para encontar mediante operaciones matematicas el lado faltante

Autores:
Jose Sanmartin
Verisión:
VER.0.1
"""
#Importamos math para poder utilizar posteriormente las funciones como pi y potencia 
import math
import os 
#Creamos un bluce While en el cual nos pedira ingresar los datos hasta que estos sean los adecuados
while True:
#Esta palabra reservada comprueba que los datos ingresados sean correctos 
        try:
#Creamos la interaccion con el usuario
#Le pedimos que ingrese un primer dato o nos indique el dato faltante 
            catetoa=float(input("Escriba el valor de un cateto o 0 si se desconoce el valor: "))
#Le pedimos que ingrese un segundo dato o nos indique el dato faltante 
            catetob=float(input("Escriba el valor del otro cateto o 0 Si se desconoce el valor: "))
#Le pedimos que ingrese un dato para la hipotenusa o nos indique el dato faltante 
            hipotenusa=float(input("Escriba el valor de la hipotenusa o 0 si se desconoce el valor: "))
#Creamos la expecion la cual nos pedira volver a poner un valor si este no es numero
        except ValueError: 
#Creamos un mensaje por si no se cumple    
            print("No es posible")
            continue
#Creamos una condicion en la cual los valroes ingresados deben ser mayores a 0
        if catetoa<0:
            print("Debe ser mayor a 0")
#Creamos una condicion en la cual los valroes ingresados deben ser mayores a 0           
        elif catetob<0:
            print("Debe ser mayor a 0")
#Creamos una condicion en la cual los valroes ingresados deben ser mayores a 0            
        elif hipotenusa<0:
            print("Debe ser mayor a 0")
#Terimanos el bucle while si las condiciones se cumplen         
        else:
            break
            
def calcularPitagoras():
    """ Es una funcion la cual ejecutara toda la parte matematica en cuanto a lo que se refiere al
    teorema de pitagoras 
    Recibe:
    ------------
      catetoa: Recibe el valor de una cateto
      catetob: Reibe el valor del otro cateoo 
      hipotenusa: Recibe el valor de la hipotenusa
           
    Retorna:
    ------------
       cata
       catb
       hip
    """
    #Creamos una condicion para calcular solo el dato faltante y conservar los otros (Cateto A)
    if catetoa==0 and catetob<hipotenusa:
    #Calculamos lo que se estas buscando 
        cata=math.pow(math.pow(hipotenusa,2)-math.pow(catetob,2),0.5)
    #Imprimimos los valores que se hallaron 
        print("El cateto es: ", cata)
    #Imprimimos los valores que se hallaron 
        print("El cateto es:", catetob)
    #Imprimimos los valores que se hallaron 
        print("La hipotenusa es:", hipotenusa)
    #Creamos una condicion para calcular solo el dato faltante y conservar los otros (Cateto b)
    elif catetob==0 and catetoa<hipotenusa:
    #Calculamos lo que se estas buscando 
        catb=math.pow(math.pow(hipotenusa,2)-math.pow(catetoa,2),0.5)
    #Imprimimos los valores que se hallaron 
        print("El cateto es:", catetoa)
    #Imprimimos los valores que se hallaron 
        print("El cateto es: ", catb)
    #Imprimimos los valores que se hallaron 
        print("La hipotenusa es:", hipotenusa)
    #Creamos una condicion para calcular solo el dato faltante y conservar los otros (Hipotenusa)
    elif hipotenusa==0:
    #Calculamos lo que se estas buscando 
        hip=math.pow(math.pow(catetob,2)+math.pow(catetoa,2),0.5)
    #Imprimimos los valores que se hallaron 
        print("El cateto es:", catetoa)
    #Imprimimos los valores que se hallaron 
    
        print("El cateto es:", catetob)
    #Imprimimos los valores que se hallaron 
    
        print("La hipotenusa es: ", hip)
    else:
        print("Error")
    otra_vez=input("Escriba r si se quieres realizar otra accion o s para salir: ")
    while True:
        if  otra_vez =="r":
            return calcularPitagoras()
        elif otra_vez=="s":
            print("Gracias")
            os.system("Pause")
        else:
            break
            

#Programa principal 
if __name__ == '__main__':
#Mensaje de Bienvenida
    print("---Calcular el Teorema de Pitagoras---")
#Se llama la funcion Suma      
calcularPitagoras()


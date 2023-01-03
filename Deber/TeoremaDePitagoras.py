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
       cata: El valor del cateto a 
       catb El valo del Catetob
       hip  El valor de la hipotenusa 
    """
    while True:
        #Creamos la condicion para validar datos 
        try:
        #Creamos una funcion que nos permita ingresar la variable dato
            catetoa=float(input("Ingrese el valor del primer cateto o 0 si es el lado que se busca: "))
            #Revisamos que la condicion se cumpla 
        except ValueError:
            #Enviamos un mensaje de advertencia
            print("Debe ser un numero")
            #Continuamos si las condiciones se cumplen
            continue
        #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
        if catetoa<0:
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
            #Pedimos al usuario que ingrese un dato
            catetob=float(input("Ingrese el valor del otro cateto o 0 si es el lado que se busca:  "))
            #No nos permite avanzar si la condicion no se cumple
        except:
            #Se imprime la advertencia 
            print("Debe ser un numero")
            #Si se cumplen las condiciones se debe seguir 
            continue
        #Se crea una condicion en la que no podemos tener numeros negativos
        if catetob<0:
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
            hipotenusa=float(input("Ingrese el valor de la hipotenusa o 0 si es el lado que se busca: "))
            #Revisamos que la condicion se cumpla 
        except ValueError:
            #Enviamos un mensaje de advertencia
            print("Debe ser un numero")
            #Continuamos si las condiciones se cumplen
            continue
        #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
        if hipotenusa<0:
            #Evaimos un mensaje de advertencia 
            print("Debe ser un numero positivo")
            #Se crea la condicion para salir del bucle 
        else:
            #Salimos del bucle
            break
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
        #Crear un condicion por si se llenan todos los espacios
    elif catetoa!=0 and catetob!=0 and hipotenusa!=0:
        #Se crea un mensaje
        print("Error Datos completos")
        #Se crea un condcion por si existe algun error
    else:
        #Se imprime un mensaje 
        print("Error revise los datos")
        # Se llama a la funcion 
    reiniciarse()

    
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
        return calcularPitagoras()
        
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
#Mensaje de Bienvenida
    print("---Calcular el Teorema de Pitagoras---")
#Se llama la funcion Suma      
    calcularPitagoras()





"""
Se busca un programa el cual calcule una operacion basica de suma con variables preguntandonos cuantas son
el grado y el valor de estas variables 

Autores:
Jose Sanmartin
Verisión:
VER.0.1
"""
#Importamos la Bilbiolteca Necesaria 
import os
def calcularEcuacion(grado,numvariables):
    """ 
    Es una funcion la cual va a realizar toda la parte matematica 
    de la operacion y nos va a enviar el resultado
    Recibe
    ------------
      grado: Recibe el valor de grado para poder utilzarlo posteriormente
      numvariables: En este nos recibe el numero de variables a operar
    ------------
       No retorna nigun parametro
    """
    #Le damos un valor inicial a la respuesta que no afecte al resultado final
    respuesta=0
    #Se crea un for para que se ingresen el numero de valores igual al numero de variables
    for i in range(1,numvariables+1):
    #imprimimos la cantidad de variables
        print(i)
        #Se crea un variable que nos permita ingresar los valores de las variables
        variable=int(input("Esriba el valor de la variable: "))
        #Se calcula la respuesta 
        respuesta=variable**grado+respuesta
    #Regresa la variable respuesta
    return respuesta

        
#Programa principal 
if __name__ == '__main__':
#Se crea un ciclo While para ver que se cumplan las condiciones       
    while True:
#Se pide al usuario que ingrese el grado de la Ecuacion
        try:
            grado=int(input("Ingrese el grado de la ecuacion: ")) 
        except ValueError:
            print("Debe ser numero")
            continue
        #Se crea un bucle while para comprobar los datos 
        while True:
            #comprobar si el valor dado es un entero.
            try:
                #Se pide el numero de variables a ingresar
                numvariables=int(input("Ingrese el numero de variables: "))
                #Comprobbar si es un valor valido
            except ValueError:
                #Esribir un mensaje si el valor es incorrecto
                print("Debe ser un numero")
                #Si se cumplen lo parametros se continua 
                continue
            #Se crea un condicion para que el numero de variables no sea menor a 1 
            if numvariables<1:
                #Se crea un mensaje para indicar esto
                print("No puede ser menor a 1")
            #Se crea la condicion de salida del bucle
            else:
            #Se sale del bucle 
                break
                


        print("La respuesta es")
        print(calcularEcuacion(grado,numvariables))    
                #Se saldra del programa con un click
        os.system("Pause")
        


       
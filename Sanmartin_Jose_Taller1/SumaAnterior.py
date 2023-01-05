"""
La adición o suma es la operación matemática de composición que consiste en combinar o añadir 
dos números o más para obtener una cantidad final o total. La suma también ilustra el proceso 
de juntar dos colecciones de objetos con el fin de obtener una sola colección. 
Por otro lado, la acción repetitiva de sumar uno, es la forma más básica de contar.

Autores:
Jose Sanmartin
Verisión:
VER.0.1
"""
#importamos la biblioteca os 
import os


def suma():
    """
    Es una funcion la recibira la parametros para la realizacion posterior de la adicion como veremos 
    Parametros:
    ------------
       numero (int): Es la cantidad de sumando que se va a ingresar 
       repeticion: Es quien se va a envacargar de repetir la operacion hasta que usuario lo decida
           
    Retorna:
    ------------
       totalSum: Devuelve el resultado de la operacion 
    """
    while True:
            try:
        #Creamos una variable que nos permita ingresar el numero de elementos a sumar 
                numero=int(input("Ingrese la cantidad  de elementos a Sumar: "))
            except ValueError:
                print("Debe ser un numero")
                continue
        #Inicializamos una variable sum con valor 0 para que sea la base de la suma 
            sum=0
                # Comando try nos permitira que el usuario no ponga otra variable que no sea un int 
            
                #El for no permitira ingresar una cierta cantidad de sumandos que se haya dispuesto antes
            for sumandos in range(numero):
                #Nos pide empezar a ingresar los valores a sumar 
                try:
                    sum += float(input("Ingrese un numero: "))
                    #Ponemos lo que se realizara si se llega a poner una letra en vez de un numero
                except ValueError:
                    print("No valido debe ser un numero")
                #Nos da el resultado de la suma 
                    continue
                totalSum= print("El resultado de la suma es: ", sum)
                #Ponemos lo que se realizara si se llega a poner una letra en vez de un numero
            
                #Imprimos un mensaje de advertencia al usuario
                    
                #Ponemos un return para regresar a la variable que necesitamos 
                    
                #Creamos una variable que nos permite repetir la funcion otra vez 
            repeticion=input("Ingrese r para volver a iniciar o cualquie tecla para salir: ")
                #Un ciclo While para tomar en cuenta las repeticiones 
            while(True):
                #Creamos una condicion, Si repeticion es igual a r se reinicia     
                        if (repeticion=="r" or repeticion=="R"):
                #Regresar al inicio de la funcion suma 
                            return suma()
                #Detener el programa 
                        else:
                            (repeticion=="s"or repeticion=="S")
                #De esta manera se terminara el programa al dar Click
                            print("Gracias por Usar esta Calculadora")
                            return os.system("Pause")
        
        
      
#Programa principal 
if __name__ == '__main__':
#Mensaje de Bienvenida
    print("Bienvenido a tu calculadora de SUMAS")
#Se llama la funcion Suma 
suma()


   
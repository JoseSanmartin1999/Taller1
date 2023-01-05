"""
El siguiente programa tiene com oobjetivo calcular el area y perimetro de una figura de 4 
lado con los datos que nos proporciona el usuario mediante el teclado

Autores:
Jose Sanmartin
Verisión:
VER.0.1
"""
import os
def areaPerimetroCuadran():
    """
    Es una funcion la recibira la parametros para calcular el area y perimetro de una figura cudrilatera
    Recibe 
    ------------
       base(float):Nos pide ingresar el valor de la base de la figura 
       altura(float): Nos pide ingresar el valor de la altura de la figura 
       otrasuma:Nos pregunta si deseamos ejecutar la funcion otra vez 
           
    Retorna:
    ------------
       area: Devuelve el resultado de la operacion area 
       perimetro:Devuelve el resultado de la operacion perimetro
    """
    #Iniciamos la interaccion con el Usuario
    print("Hola Vamos a calcular el area y perimetro de la figura")

    while True :
        try:
            #Pedimaos al usuario ingresar la longitud de la base
            base=float(input("Ingrese la longitud de la base: "))
            #Pedmos al usuario ingresar la longitud de la altura
            altura=float(input("Ingrese la longitud de la altura: "))
                
        except ValueError:
            print("El valor introducido no es un número. Intenta de nuevo")
            return areaPerimetroCuadran()
        area= (base*altura)
        perimetro=(2*base+2*altura)
        print("El area de la figura es: ", (area), "unidades^2")
        print("El perimetro de la figura es: ", perimetro, "unidades")
        reiniciar=input("Desea Realizar otra vez la misma operacion? Presiones r para si o cualquier tecla para salir: ")
        if reiniciar=="r":
            return areaPerimetroCuadran()
        else:
            print("Hasta la proxima")
            return os.system("Pause")

            

#Programa principal 
if __name__ == '__main__':
#Mensaje de Bienvenida
    print("---Calcular el Area y Perimetro de un Cuadrilatero---")
#Se llama la funcion Suma      
areaPerimetroCuadran()

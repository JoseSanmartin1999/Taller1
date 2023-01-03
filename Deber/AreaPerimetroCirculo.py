"""
El siguiente programa tiene com oobjetivo calcular el area y perimetro de una figura de 4 
lado con los datos que nos proporciona el usuario mediante el teclado

Autores:
Jose Sanmartin
Verisión:
VER.0.1
"""
#Importamos las librerias que vamos a utilizar durante el programa 
import os, math

def areaPerimetroCirculo():
    """
    Es una funcion la recibira la parametros para calcular el area y perimetro de una circunferencia 
    Recibe 
    ------------
       diametro(float):Nos pide ingresar el valor del diametro  de la figura  y lo tranforma en radio
       radio(float): Nos pide ingresar el valor del radio de la figura 
       otro_ciruculo:Nos pregunta si deseamos ejecutar la funcion otra vez 
           
    Retorna:
    ------------
       areadiam: Devuelve el resultado de la operacion area  usadno el diametro
       perimetrodiam:Devuelve el resultado de la operacion perimetro usando el diametro
        arearadio: Devuelve el resultado de la operacion area  usando el radio
       perimetroradui:Devuelve el resultado de la operacion perimetro usando el radio
    """
    #Iniciaamos la interaccion con el usuario 
    print("Hola vamos a calcular el area y perimetro de la Circunferencia ")
    #Se elige si se ingresara el diametro o el radio de la circunferencia 
    tipo_dato=input("Usted va a ingresar un diametro(d) o radio(r): ")
    #Creamos un bucle while para que se repita si no se dan las condidciones adecuadas 
    while(tipo_dato=="d" or tipo_dato=="r"):
    #Hacemos que compruebe las condidciones validas
        try:
    # Creamos una condicion por si se ingresa un diametro 
            if(tipo_dato=="d"):
    #Pedimos al usuario que ingrese el diametro
                diametro=float(input("Ingrese el diametro"))
    #Calculamos el radio del diametro ingresado
                radio1= diametro/2
    #Calculamos el area con ayuda del diametro ingresado
                areadiam=math.pi*math.pow(radio1,2)
    #Calculamos el perimetro con el diametro ingresado
                perimetrodiam=2*math.pi*radio1
    #Imprimimos la respueta del area 
                resultadiametroarea=print("El area es: ", areadiam)
    #Imprimimos la respuesta del perimetro
                resultadiametroperimetro=print("El perimetro es: ", perimetrodiam)
        # Creamos una condicion por si se ingresa un radio        
            elif(tipo_dato=="r"):
    #Perimos al usuario que ingrese el radio
                radio2=float(input("Ingrese el radio de la circunferencia"))
    #Calculamos el area con ayuda del radio ingresado
                arearadio=math.pi*math.pow(radio2,2)
    #Calculamos el perimetro con ayuda del radio ingresado
                perimetroradio=2*math.pi*radio2
    #Imprimimos la respueta del area 
                resultadiametroarea=print("El area es: ", arearadio)
    #Imprimimos la respueta del perimetro
                resultadiametroperimetro=print("El perimetro es: ", perimetroradio)
    #Creamos otra condicions en caso de que no se cumpla lo anterior
            else:
                return areaPerimetroCirculo()
    #Si encuentra un error en los datos ingresados nos devuelve hasta ingresar correcatament los datos    
        except ValueError:
    #Eviamos un mensaje previo a ingresar de nuevo los datos 
                        print("Dato no valido")
                        return areaPerimetroCirculo()
        break
    otro_circulo=input("Desea volver a hacer la operacion Si(s) o No(n)")
    if(otro_circulo=="s"):
        return areaPerimetroCirculo()
    else:
        return os.system("Pause")

#Programa principal 
if __name__ == '__main__':
#Mensaje de Bienvenida
    print("---Calcular el Area y Perimetro de un Circulo---")
#Se llama la funcion Suma      
areaPerimetroCirculo()
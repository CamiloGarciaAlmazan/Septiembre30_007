#
import os

def Numeros():
    print("**** opcion 1 de numeros*****")
    pos=0
    neg=0
    cero=0
    veces= int(input("Cuantos números desea ingresar?: "))
    for x in range(veces): 
        nume=int(input("Ingrese un número: "))
        if (nume>0):
            pos=pos+1
        elif(nume<0):
            neg=neg+1
        else:
            cero=cero+1

    print("Cantidad de números positivos: " + str(pos)+
    "\n Cantidad de números negativos : "+ str(neg)+ 
    "\n Cantidad de números iguales a cero: " + str(cero))    
         
    pausa=input("presione una tecla para continuar")


def Datos():
    print("**** opcion 2 de datos de personas****")
    #ingresar para n personas donde n es un numero ingresado
    #por teclado el nombre y edad
    # cantidad de mayores de edad y cantidad de menores de edad
    # luego subir la modificacion a github
    # "se programo la opcion 2 del menu"
    nombre="carlos"
    edad=0
    mayoresEdad=0
    menoresEdad=0
    veces= int(input("Cuantas numero de personas desea ingresar?: ")) 
    for x in range(veces): 
        nombre=str(input("Ingrese un nombre: "))
        edad=int(input("Ingrese un edad: "))
        if (edad>=18):
            mayoresEdad=mayoresEdad+1
        elif(edad<18):
            menoresEdad=menoresEdad+1

    print("Cantidad de personas mayores de edad: " + str(mayoresEdad)+
    "\n Cantidad de personas menores de edad : "+ str(menoresEdad))
     
    pausa=input("presione una tecla para continuar")





seguir=True
while (seguir):
    os.system('cls')
    print("1.opcion numeros")
    print("2.opcion datos personas")
    print("3. finalizar")
    op= int(input("ingrese opcion 1,2,3:"))
    if (op==1):
        Numeros()
    if (op==2):
        Datos()
    if (op==3):
        seguir=False
        break



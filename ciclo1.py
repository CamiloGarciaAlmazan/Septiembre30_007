# crear un ciclo for que permita ingresar n temperaturas
# donde n es un numero ingresado por teclado
#mostras cuantas temperaturas sobre cero y cuantas bajo cerro o iguala cero
sobreCero=0
bajoCero=0
veces= int(input("¿cuantas temperaturas quiere ingresar?"))
for i in range(veces):
    temple= float(input("ingrese la temperatura:"))
    if (tempe>0):
        sobreCero= sobreCero+1
    else:
        bajoCero=bajoCero+1
#mostrar datos 
print("la cantidad de temperatura mayores a cero"+str(sobreCero))
print("la cantidad de temperatura es menor o igual a cero"+str(bajoCero))



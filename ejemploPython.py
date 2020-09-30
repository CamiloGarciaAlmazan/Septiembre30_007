#ingresar dos numreos como int
a=int (input("digite el primer numero"))
b=int (input("digite el segundo numero"))
#operaciones matematicas
suma=a+b
multi=a*b
#mostramos los resultados
print(" al sumar"+str(a)+"con el numero"+str(b)+" el resultado es: "+str(suma))
print("Al mutiplicar " + str(a) + " Con el numero " + str(b) + " El resultado sera: " + str(multi))
#implementamos una condicion
if(a>b):
   print("el numero "+str(a)+ "es  mayor que "+str(b))
elif a<b:
    print("el numero "+str(b)+ "es  mayor que "+str(a))
else:
    print("los numeros son iguales")

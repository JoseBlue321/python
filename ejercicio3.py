#pedir el ingreso de 2 numeros
#mostrar el mayor de los 2 numeros
n1 = int(input("numero 1: "))
n2 = int(input("numero 2: "))
if n1 > n2 :
    print("el mayor es: ",n1)
else:
    if n2 > n1 :
        print("el mayor es:  ", n2)
    else:
        print("son iguales")
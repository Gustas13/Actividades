import math
def limite (a:int)->int:
    n = 0
    e = 0
    while n < a:
	    e += 1/(math.factorial(n))
	    n = n + 1
    return e

while True:
    print('1) Calcular e')
    print('0) Salir')
    op = input()

    if op =="1":
        a=int(input("¿Cuál es el límite del ciclo?: "))
        print("El valor de e real es: ",math.e, "el valor calvculado con: ",a," como limite es: ",limite(a))
    elif op == "0":
        break
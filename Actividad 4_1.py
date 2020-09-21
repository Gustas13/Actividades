from math import pi
def cuadrado (a:float)->float:
    area=a**2
    return area
def triangulo (a:float,b:float)->float:
    area=(a*b)/2
    return area
def circulo (a:float)->float:
    area = pi*(a**2)
    return area  

print("Elija una opción para calcular el área")
while True:
    print('1) Cuadrado')
    print('2) Triangulo')
    print('3) Círculo')
    print('0) Salir')
    op = input()

    if op =="1":
     a = float(input("Tamaño de un lado: "))
     print("Área: ",cuadrado(a))
    elif op =="2":
     a = float(input("Base: "))
     b = float(input("Altura: "))
     print("Área: ",triangulo(a,b))

    elif op =="3":
     a = float(input("Radio: "))
     print("Área: ",circulo(a))
    
    elif op == "0":
        break
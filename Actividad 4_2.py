print("Elija una opción para calcular el área")
while True:
    print('\n1) Signo Zodiacal')
    print('0) Salir')
    op = input()
    if op =="1":
        
        
        
        d=int(input("\n¿Cuál es el día de nacimiento?: "))
        print("\n¿Cuál es el mes de nacimiento?: ")
        mes = input()
        print("\n")
        print(mes,"\n")

        if mes == "Enero":
         if d>=20:
          print ("Acuario")
         else :
          print ("Capricornio") 
        
        elif mes == "Febrero":
         if d>=19:
          print("Piscis")
         else :
          print("Acuario")

        elif mes == "Marzo":
         if d>=20:
          print("Aries")
         else :
          print ("Piscis")

        elif mes == "Abril":
         if d>=20:
          print("Tauro")
         else:
          print("Aries")

        elif mes == "Mayo":
         if d>=21: 
          print("Géminis")
         else:
          print("Tauro")

        elif mes == "Junio":
         if d>=21:
          print("Cáncer")
         else:
          print("Géminis")

        elif mes == "Julio":
         if d>=23:
          print("Leo")
         else:
          print ("Cáncer")
    
        elif mes == "Agosto":
         if d>=23:
          print("Virgo")
         else:
          print("Leo")

        elif mes == "Septiembre":
         if d>=23:
          print("Libra")
         else:
          print("Virgo")

        elif mes == "Octubre":
         if d>=23:
          print("Escorpio")
         else:
          print("Libra")

        elif mes == "Noviembre":
         if d>=22:
          print("Sagitario")
         else:
          print("Escorpio")

        elif mes == "Diciembre":
         if d>=21:
          print("Capricornio")
         else:
          print("Sagitario")
        else:
          break
    elif op =="0":
        break
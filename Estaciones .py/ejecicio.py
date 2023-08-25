mes= input("Digite la estacion del mes: ")
dia= int(input("Digite el dia del mes a cosnultar: "))

if  mes== "enero" and dia<=31:
    print(f"{mes} {dia} es Invierno")
elif  mes== "febrero" and dia<=28:
    print(f"{mes} {dia} es Invierno")  
elif mes== "marzo" and dia<=31:
    print(f"{mes} {dia} es Invierno")   
elif mes== "abril" and dia<=30:
    print(f"{mes} {dia} es Verano")
elif mes== "mayo" and dia>=31:
    print(f"{mes} {dia} es verano")
elif mes== "junio" and dia>=20:
    print(f"{mes} {dia} es verano") 
elif mes=="junio" and dia<=21 and dia<=30:
    print(f"{mes} {dia} es Otono") 
elif mes== "julio" and dia<=31:
    print(f"{mes} {dia} es Otono")
elif mes== "Agosto" and dia<=31:
    print(f"{mes} {dia} es Otono")
elif mes== "Septiembre" and dia<=31:
    print(f"{mes} {dia} es Otoño")  
elif mes== "Octubre" and dia<=31:
    print(f"{mes} {dia} es Primavera")
elif mes== "Noviembre" and dia<=30:
    print(f"{mes} {dia} es Primavera")
elif mes== "Diciembre" and dia<=31:
    print(f"{mes} {dia} es Primavera")        

else:
    print("Dato Invalido")
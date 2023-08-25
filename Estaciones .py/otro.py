mes = input("Digite el nombre del mes: ").lower()
dia = int(input("Digite el día del mes a consultar: "))

if (mes == "enero" and 1 <= dia <= 31) or (mes == "febrero" and 1 <= dia <= 28):
    estacion = "Invierno"
elif (mes == "marzo" and 1 <= dia <= 31) or (mes == "abril" and 1 <= dia <= 30):
    estacion = "Primavera"
elif (mes == "mayo" and 1 <= dia <= 31) or (mes == "junio" and 1 <= dia <= 20):
    estacion = "Primavera"
elif (mes == "junio" and 21 <= dia <= 30) or (mes == "julio" and 1 <= dia <= 31):
    estacion = "Verano"
elif (mes == "agosto" and 1 <= dia <= 31) or (mes == "septiembre" and 1 <= dia <= 30):
    estacion = "Otoño"
elif (mes == "octubre" and 1 <= dia <= 31) or (mes == "noviembre" and 1 <= dia <= 30):
    estacion = "Otoño"
elif (mes == "diciembre" and 1 <= dia <= 31):
    estacion = "Invierno"
else:
    estacion = "Inválida"

print(f"{mes} {dia} es {estacion}")
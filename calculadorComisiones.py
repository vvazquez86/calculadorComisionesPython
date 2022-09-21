nombre = input("Cual es tu nombre? ")
ventas = input("Cuales fueron tus ventas este mes: ")
comisiones = int(ventas)*0.13
comisiones = round(comisiones,2)
print(f"Ok {nombre}, tus ingresos este mes son: {comisiones}")
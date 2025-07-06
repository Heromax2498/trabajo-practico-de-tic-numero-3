horas=float(input("introduce la cantidad de horas "))
tarifa=float(input("introduce la tarifa "))
if horas<=40:
    total1= horas * tarifa
    print("el pago seria de", total1)
else:
    exedente=horas-40
    total2=tarifa+exedente(tarifa * 5)
    print("el pago seria de ",total2)
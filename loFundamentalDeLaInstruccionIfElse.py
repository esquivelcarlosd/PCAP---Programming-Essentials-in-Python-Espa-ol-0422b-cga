#Variables
impuesto = 0
ingresoSuperior = 85528
ingreso=float(input("Ingrese el ingreso anual:"))
valorTotal1 = round(ingreso * 0.18 - 556.02)
valorTotal2 = round(14839 + (ingreso-ingresoSuperior)*0.32)
# Coloca tu código aquí.
if ingreso < ingresoSuperior:
    impuesto = valorTotal1
#    print ("Tu impuesto es de: " + impuesto)
elif ingreso > ingresoSuperior:
    impuesto = valorTotal2
#    print ("Tu ingreso es de: " + impuesto)

if impuesto <= 0:
    impuesto = 0
impuesto=float(round(impuesto, 0))
print("El impuesto es: ", impuesto, "pesos")
#Fin de código

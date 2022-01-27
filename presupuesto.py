


print("PRESUPUESTO DE INGREOSS Y GASTOS FAMILIAR")
print("_________________________________________"
print("")

print("INGRESOS")
print("_________")
print("")

print(" A continuacion agregue los datos de sus ingresos")

print("")


salario=float(input("ingrese su salario: $"  ))

inversiones=float(input("ingrese las ganancias de sus inversiones: "))

otros=float(input("Ingrese el total de sus entradas adicionales de dinero: "))


total_ingresos= salario+inversiones+otros


print("el total de sus ingresos es: $", total_ingresos)



print("GASTOS")
print("______")

print("")
print("")

print(" Ahora agregue todo sus gastos, si alguno de los item no tiene gasto puede agregar al mismo 0")

print("")
print("")

alquiler=float(input("ingrese su gasto de alquiler: $ "))

comida=float(input("ingrese su gasto de comida: $ "))

escuela=float(input("ingrese su gasto de escuela: $ "))

transporte=float(input("ingrese su gasto de transporte:$  "))

diversion=float(input("ingrese su gasto en diversion :$ "))

servicios=float(input("ingrese su gasto de servicios:$ "))

ahorro=float(input("ingrese su dinero destinado a ahorro:$ "))

emergencias=float(input("ingrese su dinero destinado a emergencias:$ "))


gastos= alquiler, escuela, comida, transporte, diversion, servicios, ahorro, emergencias


 
total_gastos= alquiler++escuela+comida+transporte+diversion+servicios+ahorro+emergencias

print("")
print("")

print("EL RESUMEN DE TUS GASTOS ES:$ ")

print("")

if total_gastos >0 :
    print("alquiler= $", alquiler)
    print("comida =$ ", comida)
    print("escuela=$", escuela)
    print("transporte=$", transporte)
    print("diversion=$", diversion)
    print("servicios=$", servicios)
    print("ahorro=$", ahorro)
    print("emergencias=$", emergencias)
    
else:
    print("ud no tiene gastos")

print("")


print("su total de gastos es:$", total_gastos)

diferencia=total_ingresos-total_gastos

print("")

if total_ingresos > total_gastos :
    print("uds tiene una utilidad de :",diferencia)
    print("FELICITACIONES")
elif total_ingresos < total_gastos:
    print("uds tiene una perdida de :",diferencia)
    print("DEBE REVISAR SUS GASTOS")
else:
    print("usted no tiene ni ganancia ni perdida")
    print(" rervise sus gastos para que logre una utilidad o mejore sus ingresos")



    





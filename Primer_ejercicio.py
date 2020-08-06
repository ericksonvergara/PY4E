'''
Escriba un programa para solicitar al usuario horas y tarifas por hora utilizando la entrada para calcular el pago bruto.
Use 35 horas y una tasa de 2.75 por hora para probar el programa (el pago debe ser 96.25). Debe usar input para leer una cadena
y float () para convertir la cadena en un número. No se preocupe por la verificación de errores o los datos incorrectos del usuario
'''
hrs = input("Ingresar horas: ")
tarifa = input("Ingrese la tarifa: ")
total = float(hrs) * float(tarifa)
print("Pago:", total)

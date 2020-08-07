'''
Escriba un programa para solicitar al usuario las horas y la tarifa por hora utilizando la entrada para calcular el pago bruto.
Pague la tarifa por hora por las horas hasta 40 y 1.5 veces la tarifa por hora por todas las horas trabajadas por encima de las 40 horas.
Use 45 horas y una tasa de 10.50 por hora para probar el programa (el pago debe ser 498.75). Debe usar input para leer una cadena
y float () para convertir la cadena en un número. No se preocupe por el error al verificar la entrada del usuario;
suponga que el usuario escribe los números correctamente.
'''
hrs = input("Ingrese horas: ")
tarifa = input("ingrese tarifa: ")
h = float(hrs)
t = float(tarifa)
if h > 40.0:
    reg = h * t
    otp = (h - 40.0) * (t * 0.5)
    total = reg + otp
else:
    total = h * t

print(total)

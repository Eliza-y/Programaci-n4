##Ejercicio1
for i in range(1,11):
    print(i)

i = 0
while i < 11:
    print(1)
    i += 1

##Ejercicio2
frase = "Tres tigres"
j = 1
for i in frase:
    if i == "Tres tigres":
        j += 1

print(f"La cantidad de palabras totales es:{j}")

##Ejercicio3
PIN_SECRETO = "1234"
i = 3
while i > 0:
    INGRESO = str(input("Ingrese la contraseña:"))
    if PIN_SECRETO == INGRESO:
        print("Bienvenido a su sistema")
        break
    elif i < 0:
        print("Llamando a la policia")
        break
    else:
        i -= 1
        print(f"Error, intente nuevamente, restan {i} intentos")

##Ejercicio4
print("Esta funcion calcula la hipotenusa de un triangulo rectangulo")
##Solicito los valores al usuario
CatetoA = float(input("Dame el valor de A:"))
CatetoB = float(input("Dame el valor de B:"))

while CatetoA <= 0 or CatetoB <= 0:
    print("Error, Catetos deben ser mayor que creo")
    CatetoA = float(input("Dame el valor de A:"))
    CatetoB = float(input("Dame el valor de B:"))

if CatetoA > 0:
    if CatetoB > 0:
        print(f"El valor de la hipotenusa es: {(CatetoA**2+CatetoB**2)**1/2}")
    else:
        print("B es menor o igual a Cero, esto es un error")
else:
    print("A es menor o igual a Cero, esto es un error")
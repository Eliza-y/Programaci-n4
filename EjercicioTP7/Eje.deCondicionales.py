##Ejercicio1
edad = int(input('Decime tu edad y te diga si podes pasar'))
acompañado = str(input('Indica si esta acompañado con si o no:'))
if edad >= 18:
    print("podes pasar")
else:
    if acompañado == "si":
        print("podes pasar")
    else:
        print("no podes pasar")

##Ejercicio2
a = int(input("Dame un numero"))
b = int(input("Dame otro numero"))
Hipotenusa = (a**2 + b**2)**1/2
if a <= 0:
    print('Error')
else:
    if b <= 0:
        print('Error')
print(Hipotenusa)


##Ejerciio3
a = str(input('introduzca contraseña'))
if a == 'liz5678':
    print("correcto")
else:
    print("incorrecto")    

##Ejercicio4

##Ejercicio5
seleccion = str(input("Bienvenido a Bella Napoli, ¿Quiere una pizza vegetariana? SI/NO"))
if seleccion == "SI":
    ingrediente = str(input("Selecciono Vegetariano, elija su ingrediente; Tofu o Pimiento"))
    if ingrediente == "Pimiento":
        print("Usted eligio Vegetarlano con Pimiento")
    else:
        print("Usted eligio Vegetarlano con Tofu")
else:
    ingrediente =  str(input("Selecciono NO Vegetariano, elija su ingrediente; Peperoni, Jamon o Salmon"))
    if ingrediente == "Peperoni":
        print(f"Usted eligio No Vegetariano con {ingrediente}")
    elif ingrediente == "Jamon":
        print(f"Usted eligio No Vegetariano con {ingrediente}")
    else:
        print(f"Usted eligio No Vegetariano con {ingrediente}")
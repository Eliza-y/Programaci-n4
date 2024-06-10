##Ejercicio 1

a = str(input('Dame una parabra'))

for _ in range(10):
    print(a)



##Ejercicio 2

a = int(input('Ingresa tu edad'))

for i in range(1,a+1):
    print(i)



##Ejercicio 3

a = int(input('Introduzca un número entero positivo'))
if a <= 0:
    print('incorrecto')
else:
    for i in range(1,a+1):
        print(i,end=',')



##Ejercicio 4

a = int(input('Introduzca un número entero positivo'))

for i in range(a,-1,-1):
    print(i,end=',')

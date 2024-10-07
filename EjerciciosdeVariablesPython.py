##Ejercicio1
print('Hola mundo')

##Ejercicio2
num_a = 4
int(num_a)
res = (num_a*2)/1.5
print(num_a,type(num_a))

a = 2
a = a * 2
a = a / 1.5
a = int(a)
print(a)
print(type(a))


##Ejercicio3
##paso1
ci = 100000
cf = ci*(1+0.02)**10
print(cf)
##paso2
ci = float(input("monto inicial"))
i = float(input("tasa de interes(Ingresar salor con coma;Ejemplo 0,n con n igual al valor del porcentaje sin el signo %)"))
n = float(input("Años"))
print("Monto final sera",ci*(1+1)**n)

##

ci = 100000
Interes = 0.02
ciclos = 10

ICompuesto = ci *(1+Interes)**ciclos
print(f"El valor final, con un capital de {ci}, un interes de {Interes} con la cantidad de años {ciclos} es ")
print(ICompuesto)

##Ejercicio4
res = 3
intens = 4
volt = intens * res 
print(volt)

##Ejercicio6
cli = 120
imp = 20
CTR = (cli/imp)*100
print(CTR) 


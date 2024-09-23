#Defino la función
def mult2(a,b=2):
    return print(a*b)
#Ejecuta el Codigo
x = float(input("Dame el valor a y te la multiplicario por 2"))
y = float(input("Si queres, puedo nmultiplicarlo por otro valor:"))
#Llamo a la función mult2
mult2(x,y)
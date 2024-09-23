def suma(a,b):
    return print(a+b)
def resta(a,b):
    return print(a-b)
def mult(a,b):
    return print(a*b)
def div(a,b):
    return print(a/b)
def poten(a,b):
    return print(a**b)
def raiz (a,b):
    return print(a**(1/b))


##este espacio es para crear la funcion calculadora
x = float(input("Dame el valor a"))
y = float(input("Dame el volor B"))
print("Si queres sumar ingresa A")
print("Si queres restar ingresa B")
print("Si queres multiplar ingresa C")
print("Si queres dividir ingresa D")
fun = str(input("Selecciona la opcion deseada"))
match fun:
    case "A":
        print(suma(x,y))
    case "B":
        print(resta(x,y))
    case "C":
        print(mult(x,y))
    case "D":
        print(div(x,y))
            

##Actividada1

a = int(input('Introduzca un valor de temperatura'))
if a < 10 :
    print('nivel azul')
elif a > 30:
    print('nivel rojo') 
else:
    print('nivel verde')



##otra forma
temperatura = int(input('Dame el volar de temperatura'))

match temperatura:
    case n if n < 10:
        print('nivel zaul')
    case n if n > 20:
        print('nivel verde')
    case n if n > 30:
        print('nivel rojo')        




##Actividad2
a = 53
if a == 20:
    print('recargar')
elif a >80:
    print('full')
elif a >50:
    print('oprimo') 
else:
    print('normal')
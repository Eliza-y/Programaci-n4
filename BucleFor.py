##Mi primer bucle
a = "Tres tristes tigres"
for i in a:
    print(i)

for i in range(10):
    print(i)

a = 2
for i in range (1,11):
    print(f"{a}*{i}=")
    print(i*a)


b = 1
while b != 0:
    b =int(input('Dame el valor y te devuelvo la tabla de multiplicar'))
    if a == 0:
        break
    else:
        for i in range(1,11):
            print(f"{i}*{b} = ")
            print(i*b)
print('programa finalizado')


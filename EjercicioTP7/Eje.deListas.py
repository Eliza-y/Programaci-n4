##Ejercicio1
import random

VidaA = 100
AtaqueA = 25
VidaB = 100
AtaqueB = 25

inicia = random.randrange(1,10,1)

while VidaA >0 and VidaB > 0:
    if inicia >= 5:
        #Ataque de A hacia B
         VidaB -= AtaqueA
         print(f"El Jugador A ataco a B""\n"f"a el jugador B le retan{VidaB}")
    else:
        #Ataque de B hacia A
         VidaA -= AtaqueB
         print(f"El Jugador B ataco a A""\n"f"a el jugador A le retan{VidaA}")

    inicia = random.randrange(1,10,1)
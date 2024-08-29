import random

sisalla = 0
kerrat = 1
yht = int(input("Kuinka monta pistettä suoritetaan randomilla: "))
while kerrat <= yht:
    x = random.random()
    y = random.random()
    if (x**2)+(y**2)<1:
        sisalla = sisalla + 1
    kerrat = kerrat + 1
print("Algoritmi laski piin likiarvoksi " + str((4*sisalla)/yht))
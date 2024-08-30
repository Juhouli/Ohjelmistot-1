luvut = []
a = input("Anna minulle lukuja. Tyhjä merkki lopettaa kyselyn ja tulostaa pienimmän sekä suurimman syötetyn luvun ")
while True:
    a = input("Anna seuraava luku: ")
    if a!="":
            luvut.append(float(a))
    else:
        print("Syötetyistä luvuista pienin on " + str(min(luvut)) + " ja suurin on " + str(max(luvut)))
        break

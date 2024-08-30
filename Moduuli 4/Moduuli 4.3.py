luvut = []
while True:
    a = input("Anna minulle lukuja. Tyhjä merkki lopettaa kyselyn "
                    "ja tulostaa pienimmän sekä suurimman syötetyn luvun ")
    if a!="":
            luvut.append(float(a))
    else:
        print("Syötetyistä luvuista pienin on " + str(min(luvut)) + " ja suurin on " + str(max(luvut)))
        break

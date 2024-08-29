luvut = []
while True:
    a = input("Anna minulle lukuja. Tyhjä merkki lopettaa kyselyn "
                    "ja tulostaa pienimmän sekä suurimman syötetyn luvun ")
    if isinstance(a, float) or isinstance(a, int):
            luvut.append(float(a))
    else:
        if a != "":
            print("Syötetyistä luvuista pienin on " + str(min(luvut)) + " ja suurin on " + str(max(luvut)))
            break
        else:
            a = input("Anna luku")

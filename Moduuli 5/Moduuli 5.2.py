luvut = []
a = input("Anna minulle lukuja. Tyhjä merkki lopettaa kyselyn ja tulostaa\nviisi suurinta syötettyä lukua järjestyksessä suurimmasta pienimpään: ")
while True:
    a = input("Anna seuraava luku: ")
    if a!="":
            luvut.append(float(a))
    else:
        luvut.sort(reverse=True)
        print("Viisi suurinta syötettyä lukua järjestyksessä suurimmasta pienimpään ovat:")
        print(luvut[0:5])
        break
luvut = []
a = input("Anna minulle lukuja. Tyhjä merkki lopettaa kyselyn ja tulostaa\nviisi suurinta syötettyä lukua järjestyksessä suurimmasta pienimpään: ")
while True:
    a = input("Anna seuraava luku: ")
    if a!="":
            luvut.append(float(a))
    else:
        luvut.sort(reverse=True)
        break
print("Syötetyistä luvuista viisi suuritna suurimmasta pienimpään ovat:")
for isoimmat in range(0,5):
    print(luvut[isoimmat])
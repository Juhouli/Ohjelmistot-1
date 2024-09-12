def listan_muutos(lista):
    summa = sum(lista)
    return summa

lista = []
luku = input("Anna kokonaislukuja niin lasken niiden summan. Tyhjä merkki lopettaa ohjelman: ")
while luku != "":
    lista.append(int(luku))
    luku = input("Anna seuraava luku: ")

summa = listan_muutos(lista)
print(f"Syötettyjen numeroiden summa on {summa:.0f}.")

#def listasumma (lista1):
    #summa = 0
    #for i in lista1:
        #summa += i
    #return summa
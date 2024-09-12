def kaksi_listaa(lista_a):
    lista_b = []
    for i in lista_a:
        if i%2 != 0:
            lista_b.append(int(i))

    #print("Alkuperäinen lista: ")
    #print(lista_a)
    print("Lista ilman parillisia numeroita: ")
    print(lista_b)
    return

lista1 = []
luku = input("Anna kokonaislukuja. Palautan annetut numerot listana, \nmistä on poistettu parilliset numerot. Tyhjä merkki lopettaa ohjelman: ")
while luku != "":
    lista1.append(int(luku))
    luku = input("Anna seuraava luku: ")

kaksi_listaa(lista1)

#def vain_parilliset(lista):
    #parilliset = []
    #for luku in lista:
        #if luku % 2 == 0:
            #parilliset.append(luku)
    #return parilliset

#luvut = [5, 2, 4, 10, 12, 1000, 8]
#uusi_lista = vain_parilliset(luvut)
#print(uusi_lista)
#print(luvut)
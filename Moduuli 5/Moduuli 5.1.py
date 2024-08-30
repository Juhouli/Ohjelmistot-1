from random import randint

lista = []
maara = int(input("Anna noppien lukumäärä: "))
for heitot in range(maara):
    noppa = randint(1,6)
    lista.append(noppa)
print(f"Heitettyjen {maara:.0f}:n nopan silmälukujen summa on {sum(lista):}")

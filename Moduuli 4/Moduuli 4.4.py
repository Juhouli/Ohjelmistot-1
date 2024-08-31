from random import randint

a = randint(1,10)
arvaus = int(input("Tietokone arpoo kokonaisluvun väliltä 1-10. Arvaa oikea luku: "))
while a!= arvaus:
    if arvaus > a:
        print("Liian suuri arvaus")
    elif arvaus < a:
        print("Liian pieni arvaus")
    arvaus = int(input("Arvaa uudestaan: "))
print("Oikein!")
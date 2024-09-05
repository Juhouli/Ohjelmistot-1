import math

def pizza_kustannus(halk_cm,arvo):
    halk_m = halk_cm/100
    ala = math.pi*(halk_m**2)
    kustannus = arvo/ala
    return kustannus

def parin_vertailu(a,b):
    if a < b:
        print("Ensimmäinen pizza on fiksumpi ostos!")
    elif a > b:
        print("Toinen pizza on fiksumpi ostos!")
    else:
        print("Molemmat pizzat ovat ihan yhtä fiksuja vaihtoehtoja (paitsi, jos toinen sisältää ananasta)!")
    return

print("Ohjelma kysyy kahden pizza halkaisijaa senttimetreinä sekä hintaa, laskee pizzan vastineen rahalle \njakamalla hinnan pinta-alalla, ja kertoo kumpi pizza on suhteessa halvempi.")
pizza1 = float(input("Anna ensimmäisen pizzan halkaisija senttimetreinä: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta euroina: "))
pizza2 = float(input("Anna toisen pizzan halkaisija senttimetreinä: "))
hinta2 = float(input("Anna toisen pizzan hinta euroina: "))

eka_pizza = pizza_kustannus(pizza1,hinta1)
toka_pizza = pizza_kustannus(pizza2,hinta2)
print("")
parin_vertailu(eka_pizza,toka_pizza)
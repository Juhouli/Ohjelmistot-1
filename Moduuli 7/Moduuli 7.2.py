nimilista = set()
nimi = str(input("Anna nimiä listaan. Tyhjä merkkijono lopettaa ohjelman: "))
while nimi != "":
    if nimi in nimilista:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
    nimilista.add(nimi)
    nimi = str(input("Anna seuraava nimi: "))

for p in nimilista:
    print(p)
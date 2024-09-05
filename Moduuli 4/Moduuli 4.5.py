kayttaja = "python"
salasana = "rules"
kirjaudu_kayttaja = input("Anna käyttäjänimi: ")
kirjaudu_salasana = input("Anna salasana: ")
kerrat = 1
while kerrat < 5:
    if kirjaudu_kayttaja != kayttaja or kirjaudu_salasana != salasana:
        kerrat = kerrat + 1
        kirjaudu_kayttaja = input("Väärät tiedot\nAnna käyttäjänimi: ")
        kirjaudu_salasana = input("Anna salasana: ")
    elif kirjaudu_kayttaja == kayttaja and kirjaudu_salasana == salasana:
        print("Tervetuloa")
        break
if kerrat >= 5:
    print("Pääsy evätty")
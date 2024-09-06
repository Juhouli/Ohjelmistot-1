lentoasemat = {"KBED":"Laurence G Hanscom Fld",
               "KBOS":"General Edward Lawrence Logan Intl",
               "KFIT":"Fitchburg Muni",
               "KACK":"Nantucket Meml",
               "KEWB":"New Bedford Rgnl"}



print("Ohjelmassa on lista Massachutesin osavaltion suurista lentokentistä.\nHaluatko"
                " syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa?")
kysymys = input("Syötä yksi seuraavista: uusi, haku, lopeta: ")
while kysymys != "lopeta":
    if kysymys == "uusi":
        uusi_icao = input("Anna uuden lentokentän ICAO-koodi: ")
        uusi_nimi = input("Anna lentokentän nimi: ")
        lentoasemat.update({uusi_icao:uusi_nimi})
        print("Syötetty lentokenttä lisätty tietokantaan!\n")
        kysymys = input("Syötä yksi seuraavista: uusi, haku, lopeta: ")
    elif kysymys == "haku":
        haku_icao = input("Anna haettavan lentokentän ICAO-koodi: ")
        if haku_icao in lentoasemat:
            print(f"{haku_icao} vastaa lentoasemaa {lentoasemat[haku_icao]}.\n")
            kysymys = input("Syötä yksi seuraavista: uusi, haku, lopeta: ")
        else:
            print("Syötettyä ICAO-koodia ei löytynyt tietokannasta")
            kysymys = input("Syötä yksi seuraavista: uusi, haku, lopeta: ")
    elif kysymys == "lopeta":
        break
    else:
        print("Virheellinen komento.")
        kysymys = input("Syötä yksi seuraavista: uusi, haku, lopeta: ")



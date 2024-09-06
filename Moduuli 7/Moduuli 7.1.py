vuodenajat = ("Talvi","Talvi","Kevät","Kevät","Kevät","Kesä","Kesä","Kesä","Syksy","Syksy","Syksy","Talvi")
kk = int(input("Anna kuukauden numero, tulostan kyseisen kuukauden vuodenajan: "))
while kk < 1 or kk > 12:
    kk = int(input("Virheellinen luku. Syötä joku kokonaisluku 1-12: "))
print("")
print(vuodenajat[kk-1])
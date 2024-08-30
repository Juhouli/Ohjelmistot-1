#kaverit = []
#kaveri = input("Syötä yksitellen viiden kaverin nimet: ")
#kaverit.append(kaveri)
#lukumaara = 1
#while lukumaara != 5:
#    kaveri = input(f"Syötä seuraava kaveri: ")
#    kaverit.append(kaveri)
#    lukumaara = lukumaara + 1
#print(kaverit)

kaverit = []
for luku in range (10):
    nimi = input("Anna kaverin nimi: ")
    kaverit.append(nimi)

for kaveri in kaverit:
    print(kaveri)
kaupungit = []
for a in range(0,5):
    kaupunkisyotto = input(f"Anna viiden eri kaupungin nimet. Kaupunki {a+1}: ")
    kaupungit.append(kaupunkisyotto)
print("Listaamasi kaupungit järjestyksessä olivat:")
for kaupunki in kaupungit:
    print(kaupunki)
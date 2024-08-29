vuosi = int(input("Anna vuosiluku niin kerron, onko se karkausvuosi: "))
if vuosi % 100 == 0:
    if vuosi % 400 == 0:
        print("Vuosi " + str(vuosi) + " on karkausvuosi.")
    else:
        print("Vuosi " + str(vuosi) + " ei ole karkausvuosi.")
else:
    if vuosi % 4 == 0:
        print("Vuosi " + str(vuosi) + " on karkausvuosi.")
    else:
        print("Vuosi " + str(vuosi) + " ei ole karkausvuosi.")
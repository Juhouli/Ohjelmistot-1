def gallonat_litroiksi(maara):
    gl = maara * 3.785
    return gl

gallonat = float(input("Anna bensan määrä gallonoina niin muutan sen litroiksi: "))
while gallonat >= 0:
    muutos = gallonat_litroiksi(gallonat)
    print(f"{gallonat:.3f} gallonaa on {muutos:.3f} litraa")
    gallonat = float(input("Anna seuraava bensan määrä: "))

if gallonat < 0:
    print("Syötit negatiivesen luvun. Ohjelma loppuu.")
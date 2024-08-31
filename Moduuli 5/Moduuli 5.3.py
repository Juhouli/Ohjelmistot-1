#Mikäli p on alkuluku ja a on kokonaisluku:
#niin (a^p)-a on jaollinen luvulla p (Fermat'n pieni lause)
a = 2
p = int(input("Anna positiivinen kokonaisluku niin kerron onko se alkuluku: "))
if (a**p - a) % p == 0:
    print(f"{p:.0f} on alkuluku.")
else:
    print(f"{p:.0f} ei ole alkuluku.")
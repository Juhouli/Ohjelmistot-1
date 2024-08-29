sp = input("Anna biologinen sukupuolesi: ")
hemo = float(input("Anna hemoglobiiniarvosi (g/l): "))
if sp == "Mies" or sp == "MIES" or sp == "mies":
    if 134 <= hemo <= 195:
        print("Hemoglobiinisi on normaali.")
    elif hemo < 134:
        print("Hemoglobiinisi on alhainen.")
    elif hemo > 195:
        print("Hemoglobiinisi on korkea.")
elif sp == "Nainen" or sp == "NAINEN" or sp == "nainen":
    if 117 <= hemo <= 175:
        print("Hemoglobiinisi on normaali.")
    elif hemo < 117:
        print("Hemoglobiinisi on alhainen.")
    elif hemo > 175:
        print("Hemoglobiinisi on korkea.")
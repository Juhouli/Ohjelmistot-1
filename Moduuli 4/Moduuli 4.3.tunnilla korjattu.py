lukustr = input("Anna luku: ")
if lukustr != "":
    lukuint = int(lukustr)
else:
    lukuint = 0

isoin = lukuint
pienin = lukuint

while lukustr != "":
    lukustr = input("Anna luku: ")
    if lukustr != "":
        lukuint = int(lukustr)
    if lukuint > isoin:
        isoin = lukuint
    if lukuint < pienin:
        pienin = lukuint

print(f"Suurin luku on {isoin:.0f} ja pienin on {pienin:.0f}")
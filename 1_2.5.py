lei = float(input("Anna leiviskät"))
nau = float(input("Anna naulat"))
luo = float(input("Anna luodit"))
lei_g = lei*20*32*13,3
nau_g = nau*32*13,3
luo_g = luo*13,3
summa = lei_g + nau_g + luo_g
print("Massa nykymittojen mukaan:")
print(str(summa) + " grammaa.")

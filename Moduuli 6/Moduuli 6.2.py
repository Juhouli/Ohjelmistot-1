from random import randint

def noppailu(nopan_tahkot):
    heitto = 0
    kerrat = 0
    print(f"Heitetään noppaa, jossa on {nopan_tahkot:.0f} tahkoa niin pitkään, että saadaan suurin mahdollinen silmäluku ({nopan_tahkot:.0f}):")
    while heitto != nopan_tahkot:
        heitto = randint(1,nopan_tahkot)
        kerrat = kerrat +1
        print(f"Heiton {kerrat:.0f} silmäluku on {heitto:.0f}")
    return

tahkot = int(input("Anna nopan tahkojen lukumäärä: "))
noppailu(tahkot)
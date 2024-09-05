from random import randint

def noppailu():
    heitto = 0
    kerrat = 0
    while heitto != 6:
        heitto = randint(1,6)
        kerrat = kerrat +1
        print(f"Heiton {kerrat:.0f} silmäluku on {heitto:.0f}")
    return

noppailu()


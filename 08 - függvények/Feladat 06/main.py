import random
import os
import time

start: int = None # kitalalando szam kezdőértéke
end: int = None # kitalalando szam vegerteke
titkos: int = None # kitalálandó szám

def hiba(uzenet: str) -> None:
    print("HIBA")
    print(uzenet)
    time.sleep(3)
    os.system("cls")

# szam beolvasasa határértékek közt
def szamBeolvasasa(kezdoErtek: int, vegErtek: int) -> int:
    eredmeny: int = None

    while (eredmeny == None):
        data: str = input(f"Kérem adjon meg eggy számot [{kezdoErtek} - {vegErtek}]: ")
        if (data.isnumeric() and int(data) >= kezdoErtek and int(data) <= vegErtek):
            eredmeny = int(data)
            return eredmeny
        elif (data.isnumeric() and (int(data) >= kezdoErtek and int(data) <= vegErtek)):
            hiba("A megadott szám nincs a határértékek közt!")
        else:
            hiba("Nem pozitív számot adott meg!")

# a kitalalando szam generálása
def kitalalandoSzam(kezdoErtek: int, vegertek: int) -> int:
    return random.randint(kezdoErtek, vegertek)

# tipp bekérése
def tippBeolvasasa() -> int:
    eredmeny: int = None

    while (eredmeny == None):
        data: str = input("Kérem a tippet: ")
        if (data.isnumeric()):
            eredmeny = int(data)
            return eredmeny
        else:
            hiba("Nem pozitív számot adott meg!")

# kitalalt tipp eseten a kiiras
def sikeresTipp(probalkozasokSzama: int, szam: int) -> None:
    print(f"Probálkozások száma: {probalkozasokSzama}.")
    print(f"A kitalálandó szám a {szam}.")

# tippek kozbeni kiiras
def sikertelenTipp(tipp: int, szam: int) -> None:
    if (tipp > szam):
        print(f"A kitalálandó szám kisebb.")
    else:
        print(f"A kitalálandó szám nagyobb.")



def jatek(szam: int) -> None:
    probalkozasokSzama: int = 0
    tipp: int = None

    while (tipp != szam):
        tipp: int = tippBeolvasasa()
        probalkozasokSzama += 1
        if (tipp == szam):
            sikeresTipp(probalkozasokSzama, szam)
        else:
            sikertelenTipp(tipp, szam)

# főprogram
start = szamBeolvasasa(0, 9)
end= szamBeolvasasa(40, 50)
titkos = kitalalandoSzam(start, end)

jatek(titkos)
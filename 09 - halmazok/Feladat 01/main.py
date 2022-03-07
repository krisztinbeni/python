# Töltsünk fel egy listát a felhasználó által megadott elemű random számokkal:
from typing import *
import random
import time
import os

halmaz: List[int] = []
elemekSzama: int = None
osszeg: int = None
ketjegyuSzamok: int = None
paratlanSzamokOsszegei: int = None
nullaraVegzodoSzamokSzamainakSzama: int = None
max: int = None
minIndex: int = None


def hiba(uzenet: str) -> None:
    print(uzenet)
    time.sleep(3)
    os.system("cls")

def halmazKiirasa(kiirandoHalmaz: List[int]) -> None:
    for item in kiirandoHalmaz:
        print(f"{item}", end="\t")

def halmazKiirasaForditottSorrendben(kiirandoHalmaz: List[int]) -> None:
    max: int = len(kiirandoHalmaz) - 1
    for index in range(max, -1, -1):
        print(f"{kiirandoHalmaz[index]}", end="\t")

def parosSzamokKiirasa(kiirandoHalmaz: List[int]) -> None:
    for item in kiirandoHalmaz:
        if (item % 2 == 0):
            print(f"{item}", end="\t")

def egyjegyuSzamokKiirasa(kiirandoHalmaz: List[int]) -> None:
    for item in kiirandoHalmaz:
        if (abs(item) < 10):
            print(f"{item}", end="\t")

def elemSzamBekerese() -> int:
    eredmeny: int = None

    while (eredmeny == None or eredmeny < 2):
        temp: str = input("Kérem adja meg a halmaz elemeinek a számát: ")

        if (temp.isdigit()):
            eredmeny = int(temp)

            if (eredmeny < 2):
                hiba("A halmaz elemeinek számának legalább 2-nek kell, hogy legyen.")
                eredmeny = None
        else:
            hiba("NEm számot adott meg!")

    return eredmeny

def listaFeltolteseRandomSzamokkal(elem: int) -> List[int]:
    eredmeny: List[int] = []

    for i in range(elem):
        eredmeny.append(random.randint(-10, 10))
        time.sleep(0.005)

    return eredmeny

def sum(osszeadandoHalmaz: List[int]) -> int:
    eredmeny: int = 0

    for item in osszeadandoHalmaz:
        eredmeny += item

    return eredmeny

def ketjegyuSzamokSzama(keresesHalmaza: List[int]) -> int:
    eredmeny: int = 0

    for item in keresesHalmaza:
        if(abs(item) > 9 and abs(item) < 100):
            eredmeny += 1

    return eredmeny

def paratlanSzamokOsszege(keresesHalmaza: List[int]) -> int:
    eredmeny: int = 0

    for item in keresesHalmaza:
        if (item % 2 == 1):
            eredmeny += item

    return eredmeny

def nullaraVegzodoSzamokSzama(keresesHalmaza: List[int]) -> int:
    eredmeny: int = 0

    for item in keresesHalmaza:
        if (item % 10 == 0):
            eredmeny += 1

    return eredmeny

def novekvoSorrend(keresesHalmaza: List[int]) -> int:
    temp: int = None

    for i in range(0, len(keresesHalmaza) - 1, 1):
        for j in range(i + 1, len(keresesHalmaza), 1):
            if (keresesHalmaza[j] < keresesHalmaza[i]):
                temp = keresesHalmaza[i]
                keresesHalmaza[i] = keresesHalmaza[j]
                keresesHalmaza[j] = temp

    return keresesHalmaza

def legnagyobbErtek(keresesHalmaza: List[int]) -> int:
    maximum: int = keresesHalmaza[0]

    for index in range(1, len(keresesHalmaza)):
        if (keresesHalmaza[index] > maximum):
            maximum = keresesHalmaza[index]

    return maximum

def legkisebbErtekIndexe(keresesHalmaza: List[int]) -> int:
    index: int = 0
    minimum: int = keresesHalmaza[index]

    for i in range(1, len(keresesHalmaza)):
        if (keresesHalmaza[i] < minimum):
            minimum = keresesHalmaza[i]
            index = i

    return minimum

# főprogram
elemekSzama = elemSzamBekerese()
halmaz = listaFeltolteseRandomSzamokkal(elemekSzama)

os.system("cls")
print("\nA halmaz elemei: ")
halmazKiirasa(halmaz)

# Írassuk ki a tartalmát fordított sorrendben
halmazKiirasaForditottSorrendben(halmaz)
print("\nA halmaz elemei fordított sorrendben: ")

# Számítsuk ki az elemek összegét
osszeg = sum(halmaz)
print(f"\nA halmaz elemeinek összege: {osszeg}")

# Átlagoljuk a tömbelemeket
print(f"\nA halmaz elemeinek átlaga: {osszeg / elemekSzama}")

# Írassuk ki a páros elemeket
parosSzamokKiirasa(halmaz)
print(f"\nA halmaz páros elemei: ")

# Számoljuk meg, hogy hány két jegyű szám van a tömbben
ketjegyuSzamok = ketjegyuSzamokSzama(halmaz)
print(f"\nA halmazban {ketjegyuSzamok} kétjegyű szám van.")

# Írassuk ki az egyjegyű számokat
egyjegyuSzamokKiirasa(halmaz)
print(f"\nA halmaz egy elemű elemei: ")

# Számítsuk ki a páratlan számok összegét
paratlanSzamokOsszegei = paratlanSzamokOsszege(halmaz)
print(f"\nA halmaz páratlan számú elemeinek az összege: {paratlanSzamokOsszegei}")

# Számoljuk meg hány nullára végződő szám van a tömbben
nullaraVegzodoSzamokSzamainakSzama = nullaraVegzodoSzamokSzama(halmaz)
print(f"\nA halmazban {nullaraVegzodoSzamokSzamainakSzama}db 10-el osztható szam van.")


# Rakjuk sorba a tömböt növekvő/csökkenő sorrendbe
# halmaz rendezése növevő sorrendbe
rendezettHalmaz: List[int] = novekvoSorrend(halmaz)
print(f"\nA halmaz elemei növekvő sorrendben: {rendezettHalmaz}")

# keressük ki a legnagyobb számot
max = legnagyobbErtek(halmaz)
print(f"\nA halmaz legnagyobb eleme: {max}")

# keressük ki a legkisebb számot
minIndex = legkisebbErtekIndexe(halmaz)
print(f"\nA halmaz legkisebb elemnek indexe: {minIndex}")

# linq for python
# for qrrow for python
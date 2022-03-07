# Töltsünk fel egy listát véletlenszerű 3 jegyű egész számokkal
# Számítsuk ki az elemek összegét
# Számítsuk ki az elemek átlagát
# Számoljuk meg hány szám van 500 felett!

# 1. Lista feltöltése
# 2. Halmaz elemeinek kiírása(nem írja, de lehet)
# 3. Halmaz elemeinek összege
# 4. Átlagszámítás kiírása   <---- nem függvény    atlag = elemek összege/ elemek szama
# 5. 500 feletti elemek számának meghatározása

from typing import *
import random

halmaz: List[int] = []
elemSzam: int = random.randint(10, 20)
osszeg: int = None
atlag: float = None
otszazfelettiSzamokSzama = 0

# halmaz generalasa
def halmazFeltoltese(elem: int) -> List[int]:
    eredmeny: List[int] = []
    szorzo: int = 1
    szam: int = None

    for i in range(0, elem, 1):
        szam = random.randint(100, 999)
        eredmeny.append(szam * szorzo)
        szorzo *= -1    # váltakozva írja ki a pozitív és a negatív számokat

    return eredmeny

def sum(bejarandoHalmaz: List[int]) -> int:
    eredmeny: int = 0

    for szam in bejarandoHalmaz:
        eredmeny += szam

    return eredmeny

def otszazfelettiSzamokSzamanakMeghatarozasa(bejarandoHalmaz: List[int]) -> int:
    eredmeny: int = 0

    for szam in bejarandoHalmaz:
        if (szam > 500):
            eredmeny += 1

    return eredmeny

# halmaz kiirasa
def halamzKiirasa(kiirandohalmaz: List[int]) -> None:

    for szam in kiirandohalmaz:
        print(f"{szam}", end="\t")

# főprogram
halmaz = halmazFeltoltese(elemSzam)
halamzKiirasa(halmaz)
osszeg = sum(halmaz)
print(f"\nA halmaz elemeinek összege: {osszeg}")
print(f"\nA halmaz elemeinek átlaga: {osszeg / elemSzam}")

otszazfelettiSzamokSzama = otszazfelettiSzamokSzamanakMeghatarozasa(halmaz)
print(f"\nAz 500 feletti számok száma: {otszazfelettiSzamokSzama}")
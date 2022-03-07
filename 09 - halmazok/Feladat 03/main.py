# Dobjunk egy dobókockával egymás után 7-szer, az eredményeket tároljuk el!
#   Számoljuk ki a dobások átlagát
#   Számoljuk meg hány hatos dobás történt
#   Számoljuk meg hány dobás volt páratlan
# Bónusz melyik számból volt a legtöbb?

# 1. Lista feltöltése 7 db számmal (1 - 6 közt)
# 2. 7 dobás számainak kiiratása
# 3.1 dobások összege
# 3.2 átlag számítás
# 4. 6-os dobások száma
# 5. páratlan dobasok szama

from typing import *
import random

halmaz: List[int] = []
elemSzam: int = random.randint(7, 7)
osszeg: int = None
hatosDobasokSzamainakSzama = 0
paratlanDobasokSzama = 0

def halmazFeltoltese(elem: int) -> List[int]:
    eredmeny: List[int] = []
    szam: int = None

    for szam in range(0, elem, 1):
        szam = random.randint(1, 6)
        eredmeny.append(szam)

    return eredmeny

def halmazKiirasa(kiirandoHalmaz: List[int]) -> None:
    
    for szam in kiirandoHalmaz:
        print(f"{szam}", end="\t")

def sum(bejarandoHalmaz: List[int]) -> int:
    eredmeny: int = 0

    for szam in bejarandoHalmaz:
        eredmeny += szam

    return eredmeny

def hatosDobasokSzama(bejarandoHalmaz: List[int]) -> int:
    eredmeny: int = 0

    for szam in bejarandoHalmaz:
        if (szam == 6):
            eredmeny += 1

    return eredmeny

def paratlanDobasok(paratlanSzamok: List[int]) -> int:
    eredmeny: int = 0

    for szam in paratlanSzamok:
        if (szam % 2 != 0):
            eredmeny += 1

    return eredmeny

# Bónusz
def legnagyobbKulcsErteke(szotar: Dict[int, int]) -> List[int]:
    kulcs: int = None
    ertek: int = 0
    eredmeny: List[int] = []

    # a legnagyobb ertek kikeresese a szotarbol
    for key, value in szotar.items():      # vegiglepkedunk a szotar osszes elemen kulcs-ertek parokkal

        if (szotar[key] > ertek):
            kulcs = key
            ertek = szotar[key]

    # kikeressuk azokat a kulcsokat melyeknek az erteke egyenlo az ertek valtozoval,
    # mivel azok a kulcsok (dobasok) szama fordil elo a legtobbszor
    for key, value in szotar.items():
        if (szotar[key] == ertek):
            eredmeny.append(key)

    return eredmeny

def legtobbetEloforduloSzam(lista: List[int]) -> List[int]:
    szotar: Dict[int, int] = {}     # Dict[kulcs -> szam, value -> szam elofordulasi szama]

    # meghatározzuk az előfordulási számokat
    for szam in lista:
        if (szam in szotar):
            szotar[szam] += 1       # szotar[szam] -> a kulcshoz tartozó értéket adja vissza
        else:
            szotar[szam] = 1

    # lista = [2, 4, 1, 1, 6, 3, 5]
    # szotar = {1: 2, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}

    eredmeny: List[int] = legnagyobbKulcsErteke(szotar)
    return eredmeny

# főprogram
halmaz = halmazFeltoltese(elemSzam)
halmazKiirasa(halmaz)

osszeg = sum(halmaz)
print(f"\nA dobott számok összege: {osszeg}")

print(f"\nA dobott számok átlaga: {osszeg / elemSzam}")

hatosDobasokSzamainakSzama = hatosDobasokSzama(halmaz)
print(f"\nA 6-os dobások száma: {hatosDobasokSzamainakSzama}")

paratlanDobasokSzama = paratlanDobasok(halmaz)
print(f"\nA páratlan dobások száma: {paratlanDobasokSzama}")

# Bónusz
legtobbetEloforduloSzamok: List[int] = legtobbetEloforduloSzam(halmaz)
print(f"\nA legtöbbet előfordult szám / számok: ")
print(legtobbetEloforduloSzamok)
# Töltsünk fel egy listát [-100, 100 közt] a felhasználó által megadott elem számmal. 
# E listából távolítsuk el a negatív előjelű elemeket. 
# Ezen elemekből (eltávolítottak) készítsünk egy új listát.

# 1. Halmaz feltöltése random számú elemmel -> List[int] + kiirasa
# 2. List[int] -> Negatív számok eltávolítása a listából -> List[int] (új lista)
# 3. List[int] (új lista) -> lista kiiratása

from typing import *
import random

# valtozok
elemekSzama: int = random.randint(10, 20)
halmaz: List[int] = []
pozitivHalmaz: List[int] = []

def halmazFeltoltese(elemszam: int) -> List[int]:
    eredmeny: List[int] = []

    for item in range(0, elemszam, 1):
        eredmeny.append(random.randint(-100, 100))

    return eredmeny

def kiiras(halmaz: List[int]) -> None:

    for szam in halmaz:
        print(f"{szam}", end="  ")

def pozitivHalmazFeltoltese(halmaz: List[int]) -> List[int]:
    eredmeny: List[int] = []

    for szam in halmaz:
        if (szam >= 0):
            eredmeny.append(szam)
    return eredmeny

# főprogram
halmaz = halmazFeltoltese(elemekSzama)

# kiiras
print("\nA generált halmaz: ")
kiiras(halmaz)

pozitivHalmaz = pozitivHalmazFeltoltese(halmaz)
print(f"\nA generált pozitív halmaz: ")
kiiras(pozitivHalmaz)
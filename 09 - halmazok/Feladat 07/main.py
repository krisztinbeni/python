# Feladat:
# Két számokat tartalmazó listát töltsünk fel random számokkal, úgy hogy a program kezelője a program elején megadja, hogy hány elemre lehet számítani (1<n<5)  az első lista még a második (5<n<10) ellem közt rendelkezik. 
#   Fűzzük össze őket, rakjuk növekvő sorrendbe és írjuk ki. 
#   Határozzuk meg az összefűzött lista átlagát és írjuk ki.

# 1. számbeolvasása (kezdőérték, végérték)
# 2. halmazok feltoltese
# 3. létrehozott halmazok kiirasa
# 4. halmazok összefűzése
#    sorbarakás
#    kiirás
# 5. összeg meghatározása
#    átlag meghatározása

import random
from typing import *
import time
import os

kisHalmaz: List[int] = []
nagyHalmaz: List[int] = []
atlag: float = None
osszefuzotthalmaz: List[int] = []
sorbarendezetthalmaz: List[int] = []
elemSzam: int = None

def szamBeolvasasa(kezdoErtek: int, vegErtek: int) -> int:
    eredmeny: int = None
    temp: str =""

    while (eredmeny == None):
        temp = input("Kérem adja meg a számot (először 1-5, másodszor 5-10)!")

        if (temp.isdigit()):
            if(int(temp) >= kezdoErtek and int(temp) <= vegErtek):
                eredmeny = int(temp)
                return eredmeny
            else:
                print("Az adott szám nem a megadott értékek között van!")
                time.slepp(2)
                os.system("cls")
        else:
            print("Nem számot adott meg!")
            time.slepp(2)
            os.system("cls")

def halmazFeltoltese(elemekSzama: int) -> List[int]:
    eredmeny: List[int] = []

    for i in range(0, elemekSzama, 1):
        eredmeny.append(random.randint(1, 10))

    return eredmeny

def listaOsszeFuzese(halmaz1: List[int], halmaz2: List[int]) -> List[int]:
    eredmeny: List[int] = halmaz1.copy()

    for item in halmaz2:
        eredmeny.append(item)

    # eredmeny: List[int] = halmaz1.copy()
    # eredmeny += halmaz2.copy()

    return eredmeny

def novekvoSorrend(osszefuzotthalmaz: List[int]) -> None:
    temp: int = None

    for i in range(0, len(osszefuzotthalmaz) -1, 1):
        for j in range(i + 1, len(osszefuzotthalmaz), 1):
            if(osszefuzotthalmaz[j] > osszefuzotthalmaz[i]):
                temp = osszefuzotthalmaz[i]
                osszefuzotthalmaz[i] = osszefuzotthalmaz[j]
                osszefuzotthalmaz[j] = temp

    return osszefuzotthalmaz

def osszeadas(bejarandoHalmaz: List[int]) -> int: 
    eredmeny: int = 0

    for szam in bejarandoHalmaz:
        eredmeny += szam

    return eredmeny

# főprogram
elemSzam = szamBeolvasasa(1, 5)
kisHalmaz = halmazFeltoltese(elemSzam)
print(kisHalmaz)

elemSzam = szamBeolvasasa(5, 10)
nagyHalmaz = halmazFeltoltese(elemSzam)
print(nagyHalmaz)

osszefuzotthalmaz = listaOsszeFuzese(kisHalmaz, nagyHalmaz)
print(f"A két halmaz összefűzése: {osszefuzotthalmaz}")

novekvoSorrend(osszefuzotthalmaz)
print(f"A elemei sorrendbe: {osszefuzotthalmaz}")

atlag = osszeadas(osszefuzotthalmaz) / len(osszefuzotthalmaz)
print(f"Ahalmaz elemeinek átlaga: {atlag}")
#Töltsünk fel egy listát a felhasználó által megadott elemszámmal (min 10). 
# A lista elemei legyenek véletlen számok -100 és 100 közt. Hozzunk létre két új halmazt, ahol:
# - az A halmaz elemei azok a halmaz elemek melyek oszthatóak 3-al
# - a B halmaz elemei azok a halmaz elemek melyek oszthatóak 5-el, de nem oszthatóak 3-al
# Mely halmaz (A vagy B) átlaga a nagyobb?
# A képernyőre írassuk ki az eredeti listát, az A, illetve B halmazt is.

from typing import *
import random

halmaz: List[int] = []
elemSzam: int = random.randint(-100, 100)
halmazA: List[int] = []
halmazB: List[int] = []
# halmazAharom: List[int] = []
# halmazBot: List[int] = []

def szamBeolvasasa() -> int:
    eredmeny: int = None
    temp: str =""

    while (eredmeny == None):
        temp = input("Kérem adja meg az A és a B halmaz elemeit(min 10): ")

        if (temp.isdigit()):
            if(int(temp) >= 10):
                eredmeny = int(temp)
                return eredmeny
            else:
                print("Az adott szám nem a megadott értékek között van!")
        else:
            print("Nem számot adott meg!")

def halmazFeltoltese(elemekszama: List[int]) -> List[int]:
    eredmeny: List[int] = []

    for i in range(0, elemekszama, 1):
        eredmeny.append(random.randint(-100, 100))

    return eredmeny

def harommalOszthatoHalmaz(halmazA: List[int]) -> List[int]:
    eredmeny: List[int] = []

    for szam in halmazA:
        if(szam % 3 == 0):
            print(szam)
        else:
            print()

    return eredmeny

def ottelOszthatoHalmaz(halmazB: List[int]) -> List[int]:
    eredmeny: List[int] = []

    for szam in halmazB:
        if(szam % 5 == 0):
            print(szam)
        else:
            print()

    return eredmeny

# főprogram
elemSzam = szamBeolvasasa()

halmazA = halmazFeltoltese(elemSzam)
print(f"\nAz A halmaz: {halmazA}")

halmazB = halmazFeltoltese(elemSzam)
print(f"\nA B halmaz: {halmazB}")

halmazA = harommalOszthatoHalmaz(halmaz)
print(f"\nAz A halmaz: {halmazA}")

halmazB = ottelOszthatoHalmaz(halmaz)
print(f"\nA B halmaz: {halmazB}")
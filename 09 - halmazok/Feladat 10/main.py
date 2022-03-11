# Töltsünk fel két listát a felhasználó által megadott elemszámmal. 
# A lista elemei legyenek véletlen számok -100 és 100 közt. Hozzunk létre egy új halmazt a megadott minta szerint:
#	A = [4, 6, -2, 2]
#	B = [-8, 5, 3, 10]
#	AB = [4, -8, 6, 5, -2, 3, 2, 10]

# 1. elem szám bekérése
# 2. halmaz feltöltése elem számmal x2 (A, B)
# 3. új halmaz létrehozása
# 4. főprogram :
#       - A halmaz kiirása
#       - B halmaz kiirása
#       - AB halmaz kiirása

from typing import *
import random

halmazA: List[int] = []
halmazB: List[int] = []
halmazAB: List[int] = []
elemSzam: int = random.randint(-100, 100)
osszefuzotthalmaz: List[int] = []
    
def szamBeolvasasa() -> int:
    eredmeny: int = None
    temp: str =""

    while (eredmeny == None):
        temp = input("Kérem adja meg az A és a B halmaz elemeit(ugyan annyi szám legyen bennük): ")

        if (temp.isdigit()):
            if(int(temp) >= 2):
                eredmeny = int(temp)
                return eredmeny
            else:
                print("Az adott szám nem a megadott értékek között van!")
        else:
            print("Nem számot adott meg!")

def halmazFeltoltese(elemekSzama: int) -> List[int]:
    eredmeny: List[int] = []

    for i in range(0, elemekSzama, 1):
        eredmeny.append(random.randint(-100, 100))

    return eredmeny

def listaOsszefuzese(A: List[int], B: List[int]) -> List[int]:
    eredmeny: Lista[int] = []

    for i in range(0, len(A), 1):

        eredmeny.append(A[i])
        eredmeny.append(B[i])

    return eredmeny

# főprogram
elemSzam = szamBeolvasasa()

halmazA = halmazFeltoltese(elemSzam)
print(halmazA)

halmazB = halmazFeltoltese(elemSzam)
print(halmazB)

osszefuzotthalmaz = listaOsszefuzese(halmazA, halmazB)
print(f"\nA két halmaz összefűzése: {osszefuzotthalmaz}")
# Töltsünk fel egy listát a felhasználó által megadott elemszámmal. 
# A lista elemei legyenek véletlen számok -100 és 100 kozt. Hozzunk létre két új halmazt az eredetiből. 
# Az első elemei az eredeti halmaz pozitív számai legyenek, a második halmaz elemei pedig az eredeti halmaz negatií számai.

# 1. elem számok beolvasása -> int
# 2. elemek szétválasztása -> Dict[str, List[int]]:
#  str --> pozitivHalmaz [1, 4, 6, 14]
#          negativhalmaz [-2, -53, -3 -43]

from typing import *
import random

halmaz: List[int] = []
elemSzam: int = None
eredmenyszotar: Dict[str, List[int]] = []

def halmazKiirasa(kiirandoHalmaz: List[int]) -> None:
    for item in kiirandoHalmaz:
        print(f"{item}", end="\t")

def elemSzamBekerese() -> int:
    eredmeny: int = None

    while (eredmeny == None or eredmeny < 2):
        temp: str = input("Kérem adja meg a halmaz elemeinek a számát: ")

        if (temp.isdigit()):
            eredmeny = int(temp)

            if (eredmeny < 2):
                print("A halmaz elemeinek számának legalább 2-nek kell, hogy legyen.")
                eredmeny = None
        else:
            print("Nem számot adott meg!")

    return eredmeny

def listaFeltolteseRandomSzamokkal(elem: int) -> List[int]:
    eredmeny: List[int] = []

    for i in range(elem):
        eredmeny.append(random.randint(-100, 100))

    return eredmeny

def elemekSzetvalasztasa(feldolgozandohalmaz: List[int]) -> Dict[str, List[int]]:
    szotar: Dict[str, List[int]] = {
        "pozitivszamokhalmaza" : [],
         "negativszamokhalmaza" : []
    }

    for szam in feldolgozandohalmaz:
        if (szam < 0):
            szotar["negativszamokhalmaza"].append(szam)
        else:
            szotar["pozitivszamokhalmaza"].append(szam)

    return szotar

# főprogram
elemSzam = elemSzamBekerese()
halmaz = listaFeltolteseRandomSzamokkal(elemSzam)

print("\nA generált halmaz elemei: ")
halmazKiirasa(halmaz)

eredmenyszotar = elemekSzetvalasztasa(halmaz)
print(f"\nPozitív számok halmaza: ")
print(eredmenyszotar["pozitivszamokhalmaza"])

print(f"\nNegatív számok halmaza: ")
print(eredmenyszotar["negativszamokhalmaza"])
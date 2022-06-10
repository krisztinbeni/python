from varosio import VarosIO
from varos import Varos
from varosok import Varosok
from typing import *

varosok: List[Varos] = VarosIO.read("adatok.txt")

# 1.f Írjuk ki a képernyőre az össz adatot
print("A városok adatai: \n")
for varos in varosok:
    print(f"{varos}\n")

# 2.f Keressük ki a megyeszékhely megyei jogú városokat és mentsük el a megyejoguvarosok.txt állományba
Varosok.megyejoguVarosok(, )
print(f"A megyei jogú városok exportja megtörtént!")

# 3.f Az nepesseg.txt állományba mentsük el azokat a településeket és a hozzájuk tartozó adatokat, ahol a népesség 50.000 és 100.000 közt van
Varosok.nepessegErtekekkozott(, )
print(f"A népesség szerinti városok exportja megtörtént!")

# 4.f Keressük ki azokat a településeket, melyek területei meghaladják az 200-at  és a  nagyteruletek.txt állományba mentsük el.
Varosok.nagyteruletuVarosok(, )
print(f"A  exportja megtörtént!")

# 5.f Keressük ki Békés megye össz települését és a bekes.txt állományba mentsük el.
Varosok.bekesmegyeTelepules(, )
print(f"A  exportja megtörtént!")

# 6.f megyeterületek.txt állományba mentsük el a megye nevét és területének nagyságát.
Varosok.megyeEsTerulet(, )
print(f"A  exportja megtörtént!")
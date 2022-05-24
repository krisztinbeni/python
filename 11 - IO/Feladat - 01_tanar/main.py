from xmlrpc.client import Boolean, boolean
from diak import Diak
from typing import *
from diakio import DiakIO
from osztaly import Osztaly

diakok: List[Diak] = DiakIO.read("adatok.txt")

# 1 - Írjuk ki minden diák adatát a képernyőre!
print("A diakok adatai: \n")
for diak in diakok:
    print(f"{diak}\n")

# 2 - Hány diák jár az osztályba?
print (f"Az osztályba {len(diakok)} diák jár.\n")

# 3 - Mennyi az osztály átlaga?
atlag: float = Osztaly.atlag(diakok)
print(f"Az osztályban az átlag: {atlag: 1.2f}.\n")

# 4 - Keressük a legnagyobb átlagot elért érettségizőt és írjuk ki az adatait a képernyőre.
print(f"Az osztály legjobb diákjai: \n")
joDiakok: List[Diak] = Osztaly.legjobbak(diakok)
for diak in joDiakok:
    print(f"{diak}")

# 5 - atlagfelett.txt allományba keressük ki azon tanulókat kiknek pontjai meghaladják az átlagot!
Osztaly.atlagfelettiek(diakok, atlag)
print(f"Az osztály átlag feletti diákjainak exportja megtörtént!")

# 6 - Van e kitünő tanulónk?
vanE: boolean = Osztaly.vanEkitunotanulo(diakok)
if (vanE):
    print(f"Az osztályban van kitűnő tanuló!")
else:
    print(f"Az osztályban nincs kitűnő tanuló!")

# 7 - Hány elégtelen, elégséges, jó, jeles és kitünő tanuló van az osztályban?
    #    Értékhatárok:
    #	- elégtelen, ha: 0.00 - 1.99
    #	- elégséges, ha: 2.00 - 2.99
    #	- jó, ha: 3.00 - 3.99
    #	- jeles, ha: 4.00 - 4.99
    #	- kitünő, ha: 5.00

diakAtlagok: Dict[str, int] = Osztaly.atlagertekhatarok(diakok)

print(f"Az osztályban átlag szerint a következő eredményt érték el a diákok:")

for (key, value) in diakAtlagok.items():
    print(f"\t- {key} : {value}\n")
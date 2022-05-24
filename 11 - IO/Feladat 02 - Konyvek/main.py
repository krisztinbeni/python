from cmath import inf
from konyvio import *
from konyv import *
from konyvtar import *
from typing import *

konyvek: List[Konyv] = KonyvIO.read("adatok.txt")

print("A könyvek adatai: \n")
for konyv in konyvek:
    print(f"{konyv}\n")

Konyvtar.informatika(konyvek, inf)
print(f"A könyvtár informatikai könyveinek exportja megtörtént!")
# játékos: név(str), tippek(List[int]), találatok száma(kihúzott számok(List[int]))

from Jatekos import *
from typing import *
import random

tippek: Set = {10, 13, 26, 29, 55}
kihuzottSzamok: Set[int] = set()
talalatokSzama: int = None

jatekos: Jatekos = Jatekos("János")

print(jatekos)
print(f"Tippek: {tippek}")

while(len(kihuzottSzamok) < 5):
    kihuzottSzamok.add(random.randint(1, 99))

for i in kihuzottSzamok:
    print(f"{i}", end="  ")
print()

talalatokSzama = len(tippek.intersection(kihuzottSzamok))
print(f"Találatok száma: {talalatokSzama}")
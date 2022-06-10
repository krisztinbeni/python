from jatekosio import *
from jatekos import *
from jatekosok import *
from typing import *

jatekosok: List[Jatekos] = JatekosIO.read("adatok.txt")

#1. Írjuk ki a képernyőre az össz adatot
print("A játékosok adatai: \n")
for jatekos in jatekosok:
    print(f"{jatekos}\n")

#2. Keressük ki az ütő játékosokat az utok.txt állömányba
print(f"A csapat ütői: \n")
utok: List[Jatekos] = Jatekosok.uto(jatekosok)
for jatekos in utok:
    print(f"{jatekos}")

#3. A csapattagok.txt állományba mentsük a csapatokat és a hozzájuk tartozó játékosokat a következő formában:
#   Telekom Baku: Yelizaveta Mammadova,Yekaterina Gamova,
print(f"A csapatok játékosai: ")
csapat: List[Jatekos] = Jatekosok.csapat(jatekosok)
for jatekos in csapat:
    print(f"{jatekos}")

#4. Rendezzük a játékosokat magasság szerint növekvő sorrendbe és a magaslatok.txt állományba mentsük el.
print(f"Sorrend magasság szerint: \n{jatekos}")

#5. Mutassuk be a nemzetisegek.txt állományba, hogy mely nemzetiségek képviseltetik magukat a röplabdavilágban mint játékosok és milyen számban.
print(f"A nemzetiseg szerint a jatekosok\n{nemzetisegek}")

#6. atlagnalmagasabbak.txt állományba keressük azon játékosok nevét és magasságát akik magasabbak mint az „adatbázisban” szereplő játékosok átlagos magasságánál.
Jatekosok.atlagmagassag(jatekosok)
print(f"A játékosok átlag feletti magasságának exportja megtörtént!")

#7. Állítsa növekvő sorrendbe a posztok szerint a játékosok ösz magasságát
"""
print(f"A játékosok posztonként magassági sorrend: \n")
poszt: List[Jatekos] = Jatekosok.jatekos(jatekosok)
for jatekos in poszt:
    print(f"{jatekos}")
"""

novekvoSorrend: List[Jatekos] = Jatekosok(jatekos)
print(f"\nA játékosok posztonként magassági sorrend: {novekvoSorrend}")

#8. Egy szöveges állományba, „alacsonyak.txt” keresse ki a játékosok átlagmagasságától alacsonyabb játékosokat. Az állomány tartalmazza a játékosok nevét,  magasságát és hogy mennyivel alacsonyabbak az átlagnál, 2 tizedes pontossággal.
print(f"Alacsony jatekosok:\n{kisebbMagassag}")
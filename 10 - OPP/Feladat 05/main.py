# roplabda csapat: -> neve(str), játékosok(list[jatekos]), székhely() 
# játékos: -> vezetéknév, keresztnév, mezszám, poszt, (str, kivéve a mezszám)
# székhely: -> telepules(szt), irányító szám(int), cím(str(utca)), megye(str)
# bónusz feladat: a játékosoknak legyen pontszáma és kinek van a legtöbb pontszáma
# mez szám szerint növekvő sorrend

from csapat import *

szekhely: Szekhely = Szekhely("Szeged", 6786, "Petőfi utca", "Csongrád-Csanád")
beni: Jatekos = Jatekos("Krisztin", "Benedek", 1, "négyes ütő", 51)
gergo: Jatekos = Jatekos("Krisztin", "Gergő", 3, "négyes ütő", 32)
vicus: Jatekos = Jatekos("Krisztin", "Viktória", 2, "center", 52)
encsi: Jatekos = Jatekos("Krisztin", "Enikő", 4, "center", 83)
gyula: Jatekos = Jatekos("Hatházi", "Gyula", 6, "feladó", 53)
gyorgy: Jatekos = Jatekos("Nagy", "György", 5, "kettes ütő", 42)
tibor: Jatekos = Jatekos("Kis", "Tibor", 7, "feladó (csere)", 72)
csapat: Csapat = Csapat("Röplabda csapat", szekhely, [ beni, gergo, vicus, encsi, gyula, gyorgy, tibor])

print(csapat)
print("A legtöbb pontszámmal rendelkező játékos: \n")
print(csapat.legjobbJatekos())
print("Mez számok alapján növekvő sorrendben a játékosok: \n")
print(csapat.novekvoMezSorrend())
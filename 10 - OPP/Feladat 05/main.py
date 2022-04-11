# roplabda csapat: -> neve(str), játékosok(list[jatekos]), székhely() 
# játékos: -> vezetéknév, keresztnév, mezszám, poszt, (str, kivéve a mezszám)
# székhely: -> telepules(szt), irányító szám(int), cím(str(utca)), megye(str)

from csapat import *

szekhely: Szekhely = Szekhely("Szeged", 6786, "Petőfi utca", "Csongrád-Csanád")
beni: Jatekos = Jatekos("Krisztin", "Benedek", 1, "négyes ütő")
gergo: Jatekos = Jatekos("Krisztin", "Gergő", 2, "négyes ütő")
vicus: Jatekos = Jatekos("Krisztin", "Viktória", 3, "center")
encsi: Jatekos = Jatekos("Krisztin", "Enikő", 4, "center")
gyula: Jatekos = Jatekos("Hatházi", "Gyula", 5, "feladó")
gyorgy: Jatekos = Jatekos("Nagy", "György", 6, "kettes ütő")
tibor: Jatekos = Jatekos("Kis", "Tibor", 7, "feladó (csere)")
csapat: Csapat = Csapat("Röplabda csapat", [szekhely, beni, gergo, vicus, encsi, gyula, gyorgy, tibor])

print(csapat)
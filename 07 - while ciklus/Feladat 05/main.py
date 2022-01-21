import os
import time

szam: int = 0
osszeg: int = 0
probalkozasokSzama: int = 0
hatarErtek: int = 0
hatarErtekInput: str = ""
szamInput: str = ""

while(hatarErtek < 100):
    hatarErtekInput = input("Adja meg a határértéket amely minimum 100 legyen: ")
    if (hatarErtekInput.replace("-", "").isnumeric()):
        hatarErtek = int(hatarErtekInput)
        if (hatarErtek < 100):
            print("100 vagy annál nagyobb legyen a határérték!")
    else:
        print("Nem számot adott meg!")

while(hatarErtek > osszeg):
    szamInput = input("Kérem a számot: ")
    if (szamInput.replace("-", "").isnumeric()):
        szam = int(szamInput)
        osszeg += szam
        probalkozasokSzama += 1
        print(f"{probalkozasokSzama} próbálkozás, összeg: {osszeg}")
    else:
        print("Nem számot adott meg!")

print(f"Összes próbálkozás: {probalkozasokSzama}, szamok összege: {osszeg}")
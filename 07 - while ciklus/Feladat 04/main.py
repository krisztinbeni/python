import os
import time

szam: int = 0
osszeg: int = 0
probalkozasokSzama: int = 0
temp: str = ""

while(osszeg < 100):
    temp = input("Kérem a számot: ")
    if (temp.replace("-", "").isnumeric()):
        szam = int(temp)
        osszeg += szam
        probalkozasokSzama += 1
        print(f"{probalkozasokSzama} próbálkozások, összeg: {osszeg}")
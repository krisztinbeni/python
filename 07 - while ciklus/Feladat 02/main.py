# 1. név nem lehet üres string
# 2. szóközök (1 vagy több)
# 3. a név hossza (min 3 karakter)


import os
import time

nev: str = ""

while(nev == "" or nev.isspace() or len(nev) < 3 ):
    nev = input("Írja be a nevét: ")
    if (nev == ""):
        print(f"\n Nem jó nevet adott meg!")
        time.sleep(3)
        os.system("cls")

    elif (nev.isspace()):
        print(f"\n Sok space van a névben!")
        time.sleep(3)
        os.system("cls")

    elif (len(nev) < 3):
        print(f"\n Túl kevés karakterből áll a név!")
        time.sleep(3)
        os.system("cls")

print(f"Üdvözöllek! {nev}")
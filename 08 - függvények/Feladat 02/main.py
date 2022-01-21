import time
import os

#belehet rakni az inputLib-be
#   from inputLib import *   (Ez az első feladatban van.)

def nevBekeres() -> str:
    nev: str = None

    while (nev == None):
        data: str = input("Kérem a nevét: ")

        #len = név hosszúsága
        if (len(data) < 3):
            print("Túl rövid a név, min 3 karakter.")
            time.sleep(3)
            os.systel("cls")
        else:
            nev = data
    return nev

def udvozles(nev: str) -> None:
    print(f"Üdvözlöm {nev}!")

felhasznalo: str = nevBekeres()
udvozles(felhasznalo)
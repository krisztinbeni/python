import time
import os

def tizedesSzamBeolvasasa(szoveg: str) -> float:
    szam: float = None

    while(szam == None):
        data: str = input(szoveg)
        if (data.replace("-", "").replace(".", "").isnumeric()):
            szam = float(data)
            return szam       
        else:
            print("\n Nem számot adott meg!")
            time.sleep(2)
            os.system("cls")

def egeszSzamBeolvasasa(szoveg: str) -> int:
    szam: int = None

    while(szam == None):
        data: str = input(szoveg)
        if (data.replace("-", "").replace(".", "").isnumeric()):
            szam = int(data)
            return szam       
        else:
            print("\n Nem számot adott meg!")
            time.sleep(2)
            os.system("cls")
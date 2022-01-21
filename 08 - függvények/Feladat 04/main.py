# vastag.atila.@vasvari.org

import os
import time

celsius: float = None
atvaltasMertekegysege: str = None
atvaltottMennyiseg: float = None

# hiba kiirasa
def hiba(szoveg: str) -> None:
    print(szoveg)
    time.sleep(3)
    os.system("cls")

# homerseklet bekerese celsiusban
def homersekletBekerese() -> float:
    eredmeny: float = None

    while (eredmeny == None):
        data: str = input("Kérem adja meg a hőmérsékletet C-ban! ")
        if (data.replace(".", "").replace("-", "").isdigit()):
            eredmeny = float(data)
            return eredmeny
        else:
            hiba("Nem jó a bemenő adat!")

# F vagy K legyen a valtas modja
def valtasValasztas() -> str:
    eredmeny: str = None

    while (eredmeny == None):
        data: str= input("Kérem a váltás módját [F vagy K]: ")
        if (data.capitalize() == "K" or data.capitalize() == "F"):
            eredmeny = data.capitalize()
            return eredmeny
        else:
            hiba("Ilyen opció nincs!")

# atvaltas
def atvaltas(fokCelsius: float, mire: str) -> float:
    if (mire == "K"):
        return fokCelsius + 273.15
    elif (mire == "F"):
        return 9 / 5 * fokCelsius + 32

# kiiras
def kiiras(fokCelsius: float, atvaltottFok: float, mertekegyseg: str) -> None:
    print(f"{fokCelsius}C = {atvaltottFok}{mertekegyseg}.")

# főprogram
celsius = homersekletBekerese()
atvaltasMertekegysege = valtasValasztas()
atvaltottMennyiseg = atvaltas(celsius, atvaltasMertekegysege)
kiiras(celsius, atvaltottMennyiseg, atvaltasMertekegysege)
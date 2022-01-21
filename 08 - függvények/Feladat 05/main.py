import os
import time

HUF: float = None
atvaltasMertekegysege: str = None
atvaltottMennyiseg: float = None

# hiba kiirasa
def hiba(szoveg: str) -> None:
    print(szoveg)
    time.sleep(3)
    os.system("cls")

# bemenő összeg
def osszegBekerese() -> float:
    eredmeny: float = None

    while (eredmeny == None):
        data: str = input("Kérem adja meg az összeget [HUF]: ")
        if (data.replace(".", "").isdigit()):
            eredmeny = float(data)
            return eredmeny
        else:
            hiba("Nem jó a bemenő adat!")

# kimenő összeg
def valtasValasztas() -> str:
    eredmeny: str = None

    while (eredmeny == None):
        data: str = input("Kérem a váltás módját [EUR vagy JPY vagy USD vagy CHF]: ")
        if (data.upper() == "EUR" or data.upper() == "JPY" or data.upper() == "USD" or data.upper() == "CHF"):
            eredmeny = data.upper()
            return eredmeny
        else:
            hiba("Ilyen opció nincs!")

# atvaltas
def atvaltas(penzOsszeg: float, penzNem: str) -> float:
    if (penzNem == "EUR"):
        return penzOsszeg * 356,36

    elif (penzNem == "JPY"):
        return (penzOsszeg * 356,36) * 0.75

    elif (penzNem == "USD"):
        return (penzOsszeg * 356,36) * 0.8

    elif (penzNem == "CHF"):
        return (penzOsszeg * 356,36) * 0.55

# kiiras
def kiiras(penzOsszeg: float, atvaltottHuf: float, mertekegyseg: str) -> None:
    print(f"{penzOsszeg}C = {atvaltottHuf}{mertekegyseg}.")

# főprogram
HUF = osszegBekerese()
atvaltasMertekegysege = valtasValasztas()
atvaltottMennyiseg = atvaltas(HUF, atvaltasMertekegysege)
kiiras(HUF, atvaltottMennyiseg, atvaltasMertekegysege)


import time
import os

osszeg: float = None
kulombseg: float = None
szorzat: float = None
hanyados: float = None

x: float = None
y: float = None

def osszeadas(a: float, b: float) -> float:
    eredmeny: float = a + b
    return eredmeny

def kivonas(a: float, b: float) -> float:
    eredmeny: float = a - b
    return eredmeny

def szorzas(a: float, b: float) -> float:
    eredmeny: float = a * b
    return eredmeny

def osztas(a: float, b: float) -> float:

    if (b == 0):
        return 0

    eredmeny: float = a / b
    return eredmeny

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
        
x = tizedesSzamBeolvasasa("Kérem az X értéket: ")
y = tizedesSzamBeolvasasa("Kérem az Y értéket: ")

osszeg = osszeadas(x, y)
kulombseg = kivonas(x, y)
szorzat = szorzas(x, y)
hanyados = osztas(x, y)

print(f"\n{x} + {y} = {osszeg}")
print(f"\n{x} - {y} = {kulombseg}")
print(f"\n{x} * {y} = {szorzat}")
print(f"\n{x} / {y} = {hanyados}")
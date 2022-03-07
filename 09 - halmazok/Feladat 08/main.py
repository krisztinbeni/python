#Egy egész számokat tartalmazó listát töltsünk fel billentyűzetről oly módon, hogy a listába nem kerülhet be ugyanazon szám többször is!
#   - Ha a program kezelője olyan számot írna be, amely már volt, akkor a program ezt jelezze ki!
#   - A bevitelt a kezelő akkor fejezheti be, ha sikerült neki egymás után háromszor is olyan értéket beírni, 
#     amely még nem szerepelt korábban (amit a program elfogad).
#   - A program a bevitel végén írja vissza az adatokat a képernyőre, a számokat egymás mellé írva, vesszővel elválasztva.

# 1. függvény ami egész számot kér be
# 2. számok bekérése:
#    - addig amíg 3 olyan számot nem adunk meg amely nincs a listában

from typing import *
from xmlrpc.client import boolean

halmaz: List[int] = []

def szamBeolvasasa() -> int:
    eredmeny: int = None
    temp: str = None

    while(eredmeny == None):
        temp = input("Kérem írjon be egy számot: ")
        if(temp.isdigit()):
            eredmeny = int(temp)
        else:
            print("Nem számot adott meg!")

    return eredmeny

def listaFeltoltese() -> List[int]:
    lista: List[int] = []
    ujElemekSazama: int = 0
    szam: int = None
    letezikE: boolean = False

    while(ujElemekSazama < 3):
        szam = szamBeolvasasa()     

        # magvizsgálom, hogy a szam szerepel-e a listában
        letezikE = True if(lista.count(szam) == 1)  else False    

        # ha a szám nem létezik, akkor a listába kerul
        # # uj elemek szamat is meg kell növelni eggyel
        if(not letezikE):   
            lista.append(szam)
            ujElemekSazama += 1
        # ha nem új számról van szó, akkor az uj számmokat szamolo valtozoujra 0-ra kell állítani
        else:
            ujElemekSazama = 0      
            print(f"{szam} már szerepel a listában!")

    return lista

# főprogram
halmaz: List[int] = listaFeltoltese()
print(halmaz)
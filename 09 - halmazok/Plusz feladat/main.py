import random
from typing import *

nevek: List[str] = [
    "Nagy János",
    "Kis Elek",
    "Farkas Tibor",
    "Krisztin László",
    "Varga Tivadar",
    "Kis Luca",
    "Földeák Zalán",
    "Benedek Elek",
    "Szent Mária",
    "Krisztin Benedek",
]

#szabanNap: List[int] = []
szabadnapok: List[int] = []
csokkenoHalmaz: List[str] = []

def nevekBekerese() -> str:

def szabadnapokBekerese() -> int:
    eredmeny: int = None
    
    while (eredmeny == None or eredmeny < 0 or eredmeny > 50):
        temp: str= input("Adja meg a szabadnapokat: ")
        if (temp.isdigit()):
            eredmeny = int(temp)
            if (eredmeny < 0):
                print("Nagyobb szám kell!")
                eredmeny = None
            elif (eredmeny > 50):
                print("Kisebb számot kell megadni!")
                eredmeny = None
        else:
            print("Nem számot adott meg!")

    #for i in range(0, 10, 1):
    #    eredmeny.append(random.randint(0, 50))

    return eredmeny

def szabadnapokFeltoltese(elem: int) -> List[int]:
    eredmeny: List[int] = []

    for i in range(0, 10, 1):
        eredmeny.append(random.randint(0, 50))
    
    return eredmeny

def szabadnapokKiirasa(szemelyek: List[int], szabadnapok: List[int]) -> None:  #Tuple[str]

    for index in range(0, 10, 1):
        print(f"{szemelyek[index]} - {szabadnapok[index]} db")

def csokkenoSorrend(csokkenoHalmaz: List[int]) -> None:
    eredmeny: int = None
    temp: int = None

    for i in range(0, len(csokkenoHalmaz), 1):
        for j in range(i + 1, len(csokkenoHalmaz), 1):
            if (csokkenoHalmaz[j] < csokkenoHalmaz[i]):
                temp = csokkenoHalmaz[i]
                csokkenoHalmaz[i] = csokkenoHalmaz[j]
                csokkenoHalmaz[j] = temp

    return eredmeny

# főprogram
szabadnapok = szabadnapokBekerese()
szabadnapokKiirasa(nevek, szabadnapok)


#print(f"\nLegtöbb szabadnap: {}")

#csokkenoSorrend(csokkenoHalmaz)
#print(f"\nCsökkenő sorrend: {csokkenoHalmaz}")

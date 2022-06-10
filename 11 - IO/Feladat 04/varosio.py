from statistics import mode
from varos import Varos
from typing import *
import os

class VarosIO:

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def read(fileName: str) -> List[Varos]:
        oneLine:str = None
        allLines:List[str]=[]
        
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)

            with open(path,encoding='latin-1', mode="r") as file:
                for line in file:
                    oneLine = line.strip()
                    allLines.append(oneLine)
        except FileNotFoundError as ex:
            print(f"{ex.filename} nem található!")
        
        varosok: List[Varos] = []
        varos: Varos = None
        
        adatok: List[str] = []
        
        nev: str = None
        varostipus: str = None
        megye: str = None
        jaras: str = None
        kisterseg: str = None
        nepesseg: int = None
        terulet: float = None

        for line in allLines:
            adatok = line.split('\t')

            nev = adatok[0]
            varostipus = adatok[1]
            megye = adatok[2]
            jaras = adatok[3]
            kisterseg = adatok[4]
            nepesseg = int(adatok[5])
            terulet = float(adatok[6])

            varos = Varos(nev, varostipus, megye, jaras, kisterseg, nepesseg, terulet)
            varosok.append(varos)

        return varosok

# 2.f
    @staticmethod
    def megyejoguvaroswrite(fileName: str, varosok: List[Varos]) -> None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)

            with open(path, encoding="latin-1", mode="w") as file:
                for varos in varosok:
                    file.write(f"{varos.nev}\n")
        except Exception as ex:
            print(f"{ex} nem található!")

# 3.f
    @staticmethod
    def nepessegErtekekkozottwrite(fileName: str, varosok: List[Varos]) -> None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)

            with open(path, encoding="latin-1", mode="w") as file:
                for varos in varosok:
                    file.write(f"{varos.nev}\n{varos.varostipus}\n{varos.megye}\n{varos.jaras}\n{varos.kisterseg}\n{varos.nepesseg}\n{varos.terulet}\n")
        except Exception as ex:
            print(f"{ex} nem található!")

# 4.f
    @staticmethod
    def nagyteruletuVarosokwrite(fileName: str, varosok: List[Varos]) -> None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)

            with open(path, encoding="latin-1", mode="w") as file:
                for varos in varosok:
                    file.write(f"{varos.nev}\n")
        except Exception as ex:
            print(f"{ex} nem található!")

# 5.f
    @staticmethod
    def bekesmegyeTelepuleswrite(fileName: str, varosok: List[Varos]) -> None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)

            with open(path, encoding="latin-1", mode="w") as file:
                for varos in varosok:
                    file.write(f"{varos.nev}\n")
        except Exception as ex:
            print(f"{ex} nem található!")

# 6.f
    @staticmethod
    def megyeEsTeruletwrite(fileName: str, varosok: List[Varos]) -> None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)

            with open(path, encoding="latin-1", mode="w") as file:
                for varos in varosok:
                    file.write(f"{varos.nev}\n{varos.terulet}\n")
        except Exception as ex:
            print(f"{ex} nem található!")
from statistics import mode
from jatekos import *
from jatekosok import *
from typing import *
import os

class JatekosIO:

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def read(fileName: str) -> List[Jatekos]:
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
        
        jatekosok: List[Jatekos] = []
        jatekos: Jatekos = None
        
        adatok: List[str] = []
        
        nev: str = None
        magassag: int = None
        poszt: str = None
        nemzetiseg: str = None
        csapat: str = None
        orszag: str = None

        for line in allLines:
            adatok = line.split('\t')

            nev = adatok[0]
            magassag = int(adatok[1])
            poszt = adatok[2]
            nemzetiseg = adatok[3]
            csapat = adatok[4]
            orszag = adatok[5]

            konyv = Jatekos(nev, magassag, poszt, nemzetiseg, csapat, orszag)
            jatekosok.append(jatekos)

        return jatekosok

# 2.f
    @staticmethod
    def utokwrite(fileName: str, jatekosok: List[Jatekos]) -> None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)

            with open(path, encoding="latin-1", mode="w") as file:
                for jatekos in jatekosok:
                    file.write(f"{jatekos.nev}\t{jatekos.magassag}\n{jatekos.poszt}\n{jatekos.nemzetiseg}\n{jatekos.csapat}\n{jatekos.orszag}\n")
        except Exception as ex:
            print(f"{ex} nem található!")

# 3.f
    @staticmethod
    def csapattagokwrite(fileName: str, jatekosok: List[Jatekos]) -> None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)

            with open(path, encoding="latin-1", mode="w") as file:
                for jatekos in jatekosok:
                    file.write(f"{jatekos.csapat}\t{jatekos.nev}\n")
        except Exception as ex:
            print(f"{ex} nem található!")

# 4.f
    @staticmethod
    def magassagSorrendwrite(fileName: str, magassag: List[Jatekos]) -> None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)

            with open(path, encoding="latin-1", mode="w") as file:
                for jatekos in magassag:
                    file.write(f"{jatekos.nev}\t{jatekos.magassag}\n")
        except Exception as ex:
            print(f"{ex} nem található!")

# 5.f
    @staticmethod
    def nemzetisegwrite(fileName: str, jatekosok: List[Jatekos]) -> None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)

            with open(path, encoding="latin-1", mode="w") as file:
                for jatekos in jatekosok:
                    file.write(f"{jatekos.nemzetiseg}\t{jatekos.nev}\n{jatekos.poszt}\n")
        except Exception as ex:
            print(f"{ex} nem található!")

# 6.f
    @staticmethod
    def atlagmagassagwrite(fileName: str, jatekosok: List[Jatekos]) -> None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)

            with open(path, encoding="latin-1", mode="w") as file:
                for jatekos in jatekosok:
                    file.write(f"{jatekos.nev}\t{jatekos.magassag}\n")
        except Exception as ex:
            print(f"{ex} nem található!")

# 8.f
    @staticmethod
    def nemzetisegwrite(fileName: str, jatekosok: List[Jatekos]) -> None:
        try:
            here: str = os.path.dirname(os.path.abspath(__file__))
            path: str = os.path.join(here, fileName)

            with open(path, encoding="latin-1", mode="w") as file:
                for jatekos in jatekosok:
                    file.write(f"{jatekos.nev}\t{jatekos.magassag}\n")
        except Exception as ex:
            print(f"{ex} nem található!")
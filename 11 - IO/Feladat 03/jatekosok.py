from statistics import mode
from jatekosio import *
from jatekos import *
from typing import *

class Jatekosok:

    def __init__(self, ) -> None:
        super().__init__()

    @staticmethod
    def uto(jatekosok: List[Jatekos]) -> List[Jatekos]:
        utok: List[Jatekos] = [jatekosok[0]]

        for i in range(1, len(jatekosok), 1):
            if (utok[i].poszt == utok[0].poszt):
                utok.append(jatekosok[i])

            elif (jatekosok[i].poszt > jatekosok[0].poszt):
                utok.clear()
                utok.append(jatekosok[i])

        return utok

    @staticmethod
    def atlagmagassag(jatekosok: List[Jatekos]) -> float:
        osszeg: float = 0
        atlag: float = 0

        for jatekos in jatekosok:
            osszeg += jatekos.atlag

        atlag = osszeg / len(jatekosok)

        return atlag

    @staticmethod
    def posztonkentiMagassag(poszt: List[Jatekos]) -> List[Jatekos]:
        temp: int = None

        for i in range(0, len(poszt) - 1, 1):
            for j in range(i + 1, len(poszt), 1):
                if (poszt[j] < poszt[i]):
                    temp = poszt[i]
                    poszt[i] = poszt[j]
                    poszt[j] = temp

        return poszt
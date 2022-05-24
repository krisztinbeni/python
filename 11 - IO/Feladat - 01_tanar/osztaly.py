from xmlrpc.client import Boolean, boolean
from diak import Diak
from typing import *
from diakio import *

class Osztaly:

    @staticmethod
    def atlag(diakok: List[Diak]) -> float:
        osszeg: float = 0
        atlag: float = 0

        for diak in diakok:
            osszeg += diak.atlag

        atlag = osszeg / len(diakok)

        return atlag

    @staticmethod
    def legjobbak(diakok: List[Diak]) -> List[Diak]:
        joDiakok: List[Diak] = [diakok[0]]

        for i in range(1, len(diakok), 1):
            if (diakok[i].atlag == joDiakok[0].atlag):
                joDiakok.append(diakok[i])
                #joDiakok = diakok[i]

            elif (diakok[i].atlag > joDiakok[0].atlag):
                joDiakok.clear()
                joDiakok.append(diakok[i])

        return joDiakok

    @staticmethod
    def atlagfelettiek(diakok: List[Diak], atlag: float) -> None:
        altlagfelettiek: List[Diak] = []

        for diak in diakok:
            if (diak.atlag > atlag):
                altlagfelettiek.append(diak)

        DiakIO.write("atlagfelettiek.txt", altlagfelettiek)

    @staticmethod
    def vanEkitunotanulo(diakok: List[Diak]) -> Boolean:
        vanE: boolean = False

        for diak in diakok:
            if (diak.atlag == 5.00):
                vanE = True
                break
        
        return vanE

    @staticmethod
    def atlagertekhatarok(diakok: List[Diak]) -> Dict[str, int]:

        diakAtlagok: Dict[str, int] = {}
        alsoHatarertek: int = 0

        hatarertekek: Dict[str, int] = {
            "elégtelen" : 2,
            "elégséges" : 3,
            "jó" : 4,
            "jeles" : 5,
            "kitünő" : 6,
        }

        for (key, value) in hatarertekek.items():
            darab: int = 0

            for diak in diakok:
                if (diak.atlag >= alsoHatarertek and diak.atlag < value):
                    darab += 1

            diakAtlagok[key] = darab
            alsoHatarertek = value

        return diakAtlagok
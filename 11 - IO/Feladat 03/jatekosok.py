from jatekosio import JatekosIO
from jatekos import *
from typing import *

class Jatekosok:

    def __init__(self, ) -> None:
        super().__init__()

# 2.f
    @staticmethod
    def uto(jatekosok: List[Jatekos]) -> List[Jatekos]:
        utok: List[Jatekos] = [jatekosok[0]]

        for i in range(1, len(jatekosok), 1):
            if (utok[i].poszt == utok[0].poszt):
                utok.append(jatekosok[i])

            elif (jatekosok[i].poszt > jatekosok[0].poszt):
                utok.clear()
                utok.append(jatekosok[i])

        JatekosIO.write("utok.txt", utok)

        return utok

# 3.f
    @staticmethod
    def csapatJatekosa(csapat: List[Jatekos]) -> None:

        #kikeressük a kulcsokat
        csapatok: set[str] = set()
        for jatekos in csapat:
            csapatok.add(jatekos.csapat)

        #minden kulcshoz a szotárban elkészítünk egy üres halmazt (listát)
        #mivel mamóriát kell neki(listának) lefoglalni
        #ennek a célja, hogy a következő for ciklusban az új elemet
        #jatekost a listába tudjuk tenni
        csapattagok: Dict[str, List[str]] = {}

        for csapat in csapatok:
            csapattagok[csapat] = []

        #jatekos nevek kikeresése csapatonként és szótárba rendezése csapatonként
        for csapat in csapatok:
            for jatekos in csapat:
                if (csapat == jatekos.csapat):
                    csapattagok[csapat].append(jatekos.nev)

        JatekosIO.write("csapattagok.txt", csapatok)

# 4.f 
    @staticmethod
    def magassagNovekvosorrend(magassag: List[Jatekos]) -> None:
        temp: int = None

        for i in range(1, len(magassag), 1):
            for j in range(i + 1, len(magassag), 1):
                if (magassag[j] < magassag[i]):
                    temp = magassag[i]
                    magassag[i] = magassag[j]
                    magassag[j] = temp

        JatekosIO.write("magaslatok.txt", magassag)

# 5.f
    @staticmethod
    def nemzetisegek(nemzetiseg: List[Jatekos]) -> None:

        JatekosIO.write("nemzetisegek.txt", nemzetiseg)

# 6.f
    @staticmethod
    def atlagmagassag(jatekosok: List[Jatekos]) -> float:
        osszeg: float = 0
        atlag: float = 0

        for jatekos in jatekosok:
            osszeg += jatekos.magassag

        atlag = osszeg / len(jatekosok)

        return atlag

# 7.f
    @staticmethod
    def posztonkentiMagassag(jatekosok: List[Jatekos]) -> List[Jatekos]:
        temp: int = None

        posztok: set[str] = set()
        for jatekos in poszt:
            posztok.add(jatekos.poszt)

        jatekos: Dict[str, List[str]] = {}

        for csapat in posztok:
            jatekos[csapat] = []

        for csapat in posztok:
            for jatekos in poszt:
                if (poszt == jatekos.poszt):
                    jatekos[poszt].append(jatekos.nev)

        for i in range(0, len(jatekosok) - 1, 1):
            for j in range(i + 1, len(jatekosok), 1):
                if (jatekosok[j] < jatekosok[i]):
                    temp = jatekosok[i]
                    jatekosok[i] = jatekosok[j]
                    jatekosok[j] = temp

        return temp

# 8.f
    @staticmethod
    def kisebbMagassag(atlagmagassag: List[Jatekos]) -> List[Jatekos]:
        magassag: float = None
        

        JatekosIO.write("alacsonyak.txt", atlagmagassag)
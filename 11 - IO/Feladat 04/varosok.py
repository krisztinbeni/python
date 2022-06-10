from varosio import VarosIO
from varos import Varos
from typing import *

class Varosok:

# 2.f
    @staticmethod
    def megyejoguVarosok(megyejog: List[Varos]) -> List[Varos]:
        megyeszekhely: List[Varos] = []

        for varos in megyejog:
            if (varos.varostipus == megyeszekhely):
                megyeszekhely.append(varos)

        VarosIO.write("megyejoguvarosok.txt", megyeszekhely)

# 3.f
    @staticmethod
    def nepessegErtekekkozott(nepessegek: List[Varos]) -> List[Varos]:
        nepessegErtekek: List[Varos] = []

        for varos in nepessegek:
            if (varos.nepesseg > 50000 and varos.nepesseg < 100000):
                nepessegErtekek.append(varos)

        VarosIO.write("nepesseg.txt", nepessegErtekek)

# 4.f
    @staticmethod
    def nagyteruletuVarosok(nagyterulet: List[Varos]) -> List[Varos]:
        nagyTerulet: List[Varos] = []

        for varos in nagyterulet:
            if (varos.terulet > 200):
                nagyTerulet.append(varos)

        VarosIO.write("nagyteruletek.txt", nagyTerulet)

# 5.f
    @staticmethod
    def bekesmegyeTelepules(bekestelepules: List[Varos]) -> List[Varos]:
        bekesmegye: List[Varos] = []

        for varos in bekestelepules:
            if (varos.telepules in bekesmegye):
                bekesmegye.append(varos)

        VarosIO.write("bekes.txt", bekesmegye)

# 6.f
    @staticmethod
    def megyeEsTerulet(megyeterulet: List[Varos]) -> List[Varos]:
        megyenagysag: List[Varos] = []

        for varos in megyeterulet:
            if (varos.terulet in megyenagysag):
                megyenagysag.append(varos)

        VarosIO.write("megyeterületek.txt", megyenagysag)
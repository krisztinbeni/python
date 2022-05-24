from konyvio import *
from konyv import *
from konyvtar import *
from typing import *

class Konyvtar:

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def informatika(konyvek: List[Konyv], inf: str) -> None:
        informatika: List[Konyv] = []

        for konyv in konyvek:
            if (konyv.inf > inf):
                informatika.append(konyv)

        KonyvIO.write("informatika.txt", informatika)

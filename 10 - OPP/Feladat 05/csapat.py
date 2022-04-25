from jatekos import *
from szekhely import *
from typing import *

class Csapat:
    def __init__(self, csapatnev: str, szekhely:List[Szekhely], jatekosok:List[Jatekos]):
        super().__init__()
        self.csapatnev: str = csapatnev
        self.jatekosok: List[Jatekos] = jatekosok
        self.szekhely: List[Szekhely] = szekhely

    def __str__(self) -> str:
        output : str = f"{self.csapatnev}:\n"
        for jatekos in self.jatekosok:
            output += f"- {str(jatekos)}\n"

        return output

    def legjobbJatekos(self) -> Jatekos:
        max: Jatekos = self.jatekosok[0]

        for i in range(1, len(self.jatekosok)):
            if(self.jatekosok[i].pontszam > max.pontszam):
                max = self.jatekosok[i]
            
        return max

    def novekvoMezSorrend(self) -> List[Jatekos]:
        rendezett: List[Jatekos] = self.jatekosok.copy()
        seged: Jatekos = None

        for i in range(0, len(self.jatekosok) -1, 1):
            for j in range(i + 1, len(self.jatekosok), 1):
                if(rendezett[j].mezszam < rendezett[i].mezszam):
                    seged = rendezett[i]
                    rendezett[i] = rendezett[j]
                    rendezett[j] = seged
                
        return rendezett
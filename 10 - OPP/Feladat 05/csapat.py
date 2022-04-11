from jatekos import *
from szekhely import *
from typing import *

class Csapat:
    def __init__(self, csapatnev: str, jatekosok:List[Jatekos]):
        super().__init__()
        self.csapatnev: str = csapatnev
        self.jatekosok: List[Jatekos] = jatekosok

    def __str__(self) -> str:
        output : str = f"{self.csapatnev}:\n"
        for jatekos in self.jatekosok:
            output += f"- {str(jatekos)}\n"

        return output
from Tanulo import Tanulo1, Tanulo2, Tanulo3

class Tanulok:

    def __init__(self,  csoportnev: str, tanulo1: Tanulo1, tanulo2: Tanulo2, tanulo3: Tanulo3) -> None:
        super().__init__()

        self.csoportnev: str = csoportnev
        self.tanulo1: Tanulo1 = tanulo1
        self.tanulo2: Tanulo2 = tanulo2
        self.tanulo3: Tanulo3 = tanulo3

    def __str__(self) -> str:
        return f"{self.csoportnev}:\nAz első tanuló adatai:\n{self.tanulo1}\nA második tanuló adatai:\n{self.tanulo2}\nA harmadik tanuló adatai:\n{self.tanulo3}"
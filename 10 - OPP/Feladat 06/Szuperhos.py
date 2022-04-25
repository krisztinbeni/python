import random

class Szuperhos:

    def __init__(self, nev: str) -> None:
        super().__init__()
        self.nev: str = nev
        self.ero: int = random.randint(50, 100)
        self.hp: int = random.randint(60, 90)

    def __str__(self) -> str:
        return f"Név: {self.nev}\tErő: {self.ero}\tÉleterő: {self.hp}"

    def tamadas(self, ellenseg: "Szuperhos") -> bool:
            return self.ero > ellenseg.hp
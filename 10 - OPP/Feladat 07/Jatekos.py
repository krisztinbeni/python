class Jatekos:

    def __init__(self, nev: str):
        self.nev: str = nev

    def __str__(self) -> str:
        return f"Név: {self.nev}"
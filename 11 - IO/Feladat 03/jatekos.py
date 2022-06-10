class Jatekos:

    def __init__(self, nev: str, magassag: int, poszt: str, nemzetiseg: str, csapat: str, orszag: str) -> None:
        super().__init__()

        self.nev: str = nev
        self.magassag: int = magassag
        self.poszt: str = poszt
        self. nemzetiseg: str = nemzetiseg
        self.csapat: str = csapat
        self.orszag: str = orszag

    def __str__(self) -> str:
        return f"Név: {self.nev}, Magasság: {self.magassag}, Poszt: {self.poszt}, Nemzetiség: {self.nemzetiseg}, Csapat: {self.csapat}, Ország: {self.orszag}\n"
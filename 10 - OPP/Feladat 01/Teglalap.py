class Teglalap:

    # konstruktor
    def __init__(self, hossz: float, szelesseg: float) -> None:
        super().__init__()

        # adattagok beírása
        self.hossz = hossz
        self.szelesseg = szelesseg

    #string függvény felületénekkiirasa
    def __str__(self) -> str:
        return f"hossz = {self.hossz}\nszélesség = {self.szelesseg}\nT = {self.terulet()}\nK = {self.kerulet()}"

    # függvények
    def terulet(self) -> float:
        return self.hossz * self.szelesseg

    def kerulet(self) -> float:
        return 2 * (self.hossz + self.szelesseg)
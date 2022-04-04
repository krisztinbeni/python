import math

class Derekszogu:

    def __init__(self, a: float, b: float, c: float, aMagassag: float) -> None:
        super().__init__()

        self.a = a
        self.b = b
        self.c = c
        self.aMagassag = aMagassag

    def __str__(self) -> str:
        return f"T = {self.terulet()}\nK = {self.kerulet()}"

    def terulet(self) -> float:
        return (self.a * self.aMagassag) / 2

    def kerulet(self) -> float:
        return self.a + self.b + self.c

class Egyenloszaru:


class Szabalyos:


class asd:
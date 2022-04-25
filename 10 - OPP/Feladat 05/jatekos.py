class Jatekos:

    def __init__(self, vezeteknev: str, keresztnev: str, mezszam: int, poszt: str, pontszam: int):
        super().__init__()
        self.vezeteknev: str = vezeteknev
        self.keresztnev: str = keresztnev
        self.mezszam: int = mezszam
        self.poszt: str = poszt
        self.pontszam: int = pontszam

    def __str__(self) -> str:
        return f"{self.vezeteknev} {self.keresztnev}:\n\tmezszám: {self.mezszam}\n\tposzt: {self.poszt}\n\tpontszám: {self.pontszam}"
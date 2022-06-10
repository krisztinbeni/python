class Varos:

    def __init__(self, nev: str, varostipus: str, megye: str, jaras: str, kisterseg: str, nepesseg: int, terulet: float) -> None:
        super().__init__()

        self.nev: str = nev
        self.varostipus: str = varostipus
        self.megye: str = megye
        self.jaras: str = jaras
        self.kisterseg: str = kisterseg
        self.nepesseg: int = nepesseg
        self.terulet: float = terulet

    def __str__(self) -> str:
        return f"Városnév: {self.nev}  Tipusa: {self.varostipus}  Megye: {self.megye}  Járás: {self.jaras}  Kistérség: {self.kisterseg}  Népesség: {self.nepesseg}  Terület: {self.terulet}\n"
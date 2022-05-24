class Konyv:

    def __init__(self, veznev: str, kernev: str, szul: int, cim: str, isbn: int, kiado: str, kiadev: int, ar: int, tema: str, oldal: int, honor: int) -> None:
        super().__init__()
        self.veznev = veznev
        self.kernev = kernev
        self.szul = szul
        self.cim = cim
        self.isbn = isbn
        self.kiado = kiado
        self.kiadev = kiadev
        self.ar = ar
        self.tema = tema
        self.oldal = oldal
        self.honor = honor

    def __str__(self) -> str:
        return f"{self.veznev} {self.kernev} : {self.szul} : {self.isbn} : {self.kiado} : {self.kiadev} : {self.ar} FT : {self.tema} : {self.oldal} : {self.honor}"
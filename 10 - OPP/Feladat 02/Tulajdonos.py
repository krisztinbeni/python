class Tulajdonos:

    def __init__(self, nev: str, szuletesidatum: str, nem: str, szuletesihely: str) -> None:
        super().__init__()

        self.nev = nev
        self.szuletesidatum = szuletesidatum
        self.nem = nem
        self.szuletesihely = szuletesihely

    def __str__(self) -> str:
        return f"név: {self.nev}\nszületési dátum: {self.szuletesidatum}\nnem: {self.nem}\nszületési hely: {self.szuletesihely}\n"
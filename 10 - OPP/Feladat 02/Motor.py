class Motor:

    def __init__(self, gyarto: str, tipus: str, kivitel: str, teljesitmeny: str, suly: str, hengerurtartalom: str,) -> None:
        super().__init__()

        self.gyarto = gyarto
        self.tipusa = tipus
        self.kivitel = kivitel
        self.teljesitmeny = teljesitmeny
        self.suly = suly 
        self.hengerurtartalom = hengerurtartalom

    def __str__(self) -> str:
        return f"gyarto = {self.gyarto}\ntipus = {self.tipusa}\nkivitel = {self.kivitel}\nteljesitmeny = {self.teljesitmeny}\nsuly = {self.suly}\nhengerurtartalom = {self.hengerurtartalom}\n tulajdonos = {tulajdonos}"

class Tulajdonos:

    def __init__(self, nev: str, szuletesidatum: str, nem: str, szuletesihely: str) -> None:
        super().__init__()

        self.nev = nev
        self.szuletesidatum = szuletesidatum
        self.nem = nem
        self.szuletesihely = szuletesihely

    def __str__(self) -> str:
        return f"név: {self.nev}\nszületési dátum: {self.szuletesidatum}\nnem: {self.nem}\nszületési hely: {self.szuletesihely}"
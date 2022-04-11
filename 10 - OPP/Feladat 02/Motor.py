from Tulajdonos import Tulajdonos

class Motor:

    def __init__(self, gyarto: str, tipus: str, kivitel: str, teljesitmeny: str, suly: str, hengerurtartalom: str, tulajdonos: Tulajdonos) -> None:
        super().__init__()

        self.gyarto: str = gyarto
        self.tipusa: str = tipus
        self.kivitel: str = kivitel
        self.teljesitmeny: str = teljesitmeny
        self.suly: str = suly 
        self.hengerurtartalom: str = hengerurtartalom
        self.tulajdonos: Tulajdonos = tulajdonos

    def __str__(self) -> str:
        return f"A tulajdonos adatai:\n{self.tulajdonos}\nA motor adatai: \ngyarto: {self.gyarto}\ntipus: {self.tipusa}\nkivitel: {self.kivitel}\nteljesitmeny: {self.teljesitmeny}\nsuly: {self.suly}\nhengerurtartalom: {self.hengerurtartalom}\n"
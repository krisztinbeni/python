import datetime
import time
import os

felhasznaloNev: str = None
szuletesiEv: int = None
kor: int = None

# nev bekerese
def nevBeolvasasa() -> str:
    eredmeny: str = None
    while (felhasznaloNev == None):
        data: str = input("Kérem a nevét: ")
        if (len(data) > 3):
            nev = data
            return eredmeny
        else:
            print("Túl rövid a név amit megadott!")
            time.sleep(3)
            os.system("cls")

# szuletesi ev bekerese
def szuletesiEvBekerese() -> int:
    eredmeny: int = None
    ma: Datetime = datetime.datetime.now()   # a mai dátumot adja vissza
    jelenlegiEv: int = int(ma.strftime("%Y"))  # visszaadja a jelenlegi évet a dátumból

    while (eredmeny == None):
        data: str = input("Kéremadja meg a születési évét: ")
        if (data.isnumeric()):
            eredmeny = int(data)

            if (eredmeny >= jelenlegiEv):
                eredmeny = None
                print("A születési év nem lehet nagyobb mint a jelenlegi év!")
                time.sleep(3)
                os.system("cls")
            else:
                return eredmeny

        else:
            print("Nem megfelelő születési évet adott meg!")
            time.sleep(3)
            os.system("cls")

# eletkor kiszamitasa
def eletkorKiszamitasa(ev: int) -> int:
    ma: Datetime = datetime.datetime.now()
    jelenlegiEv: int = int(ma.strftime("%Y"))

    return jelenlegiEv - ev

# kiiratas
def kiiratas(nev: str, ev: int) -> None:
    ma: Datetime = datetime.datetime.now()
    jelenlegiEv: int = int(ma.strftime("%Y"))
    print(f"{nev} ön az idén {ev} éves!")

# főprogram
felhasznaloNev = nevBeolvasasa()
szuletesiEv = szuletesiEvBekerese()

kor = eletkorKiszamitasa(szuletesiEv)

kiiratas(felhasznaloNev, kor)
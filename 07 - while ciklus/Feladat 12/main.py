penz: float = None
honapokSzama: int = 0
data: str = ""

while (penz == None or penz < 10000 or penz > 50000):
    data=input("Adja meg a pénzének a mennyiségét: ")
    if (data.isnumeric()):
        penz = float(data)
        if (penz < 10000 or penz > 50000):
            print("Nem jó pénz mennyiséget adott meg!")
    else:
        print("Nem számot adott meg!")

while (penz < 100000):
    penz = penz * 1.02
    honapokSzama += 1

print(f"{honapokSzama} hónap mÚlva éri el a 100000 FT-ot.")
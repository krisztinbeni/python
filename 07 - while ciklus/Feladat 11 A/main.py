import random

szamEgy: int == None
szamKetto: int = None
data: str = ""
negyelOszthatoSzamok: int = 0

while (szamEgy == None or szamEgy % 2 != 0):
    data = input("Adjon egy páros számot: ")
    if (data.replace("-", "").isnumeric):
        szamEgy = int(data)
        if (szamEgy % 2 != 0):
            print("Páros számot adjon meg!")
    else:
        print("Nem számot adott meg!")

while (szamKetto == None or szamKetto % 2 == 0 or szamKetto < szamEgy):
    data = input("Adjon egy páros számot: ")
    if (data.replace("-", "").isnumeric):
        szamKetto = int(data)
        if (szamKetto % 2 == 0):
            print("Páratlan számot adjon meg!")
        elif (szamKetto < szamEgy):
            print(f"{szamKetto}-nek nagyobbnak kell lennia a {szamEgy}-nél!")
    else:
        print("Nem számot adott meg!")

rnd: int = random.randint(szamEgy, szamKetto)
if (abs(abs (rnd)-abs(szamEgy)) < abs(abs (rnd)-abs (szamKetto))):
    print(f"A {rnd} a szamEgy-hez van közelebb!")
elif (abs(abs (rnd)-abs(szamEgy)) > abs(abs (rnd)-abs (szamKetto))):
    print(f"A {rnd} a szamKetto-höz van közelebb!")
else:
    print(f"A {rnd} a két számtól egyforma távolságra van!")

atlag: float = (szamEgy+szamKetto)/2
    print(f"A számok átlaga: {atlag}")

for i inr range(szamEgy, szamKetto+1, 1):
    if (i % 4 == 0):
        negyelOszthatoSzamok += i
        print(f"A 4-elosztható számok száma: {negyelOszthatoSzamok}")
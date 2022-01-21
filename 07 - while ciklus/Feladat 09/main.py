szam: int = None
data: str = ""

while (szam == None or szam < 100 or szam > 999):
    data = input("Adjon meg egy háromjegyű számot: ")
    if (data.replace("-", "").isnumeric()):
        szam = int(data)
        if (szam < 100 or szam > 999):
            print("100 és 999 között adjon megy számot!")
    else:
        print("Nem számot adott meg!")

if (szam % 7 == 0):
    print(f"A {szam} osztható 7-tel!")
else:
    print(f"A {szam} NEM osztható 7-tel!")
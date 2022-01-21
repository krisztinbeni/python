# 1. bekérni egy számot a: int <- bármelyik szám while ciklus
# 2. bekérni egy másik számot b: int      b > a   while ciklus
# 3. for i in range (vegErtek, kezdoErtek, -1)

kezdoErtek: int = None
vegErtek: int = None
data: str = ""

while (kezdoErtek == None):
    data = input("Adja meg a kezdőértéket: ")
    if (data.replace("-", "").isnumeric()):
        kezdoErtek = int(data)
    else:
        print("Nem szamot adott meg!")

while (vegErtek == None or vegErtek <= kezdoErtek):
    data = input("Adja meg a végértéket: ")
    if (data.replace("-", "").isnumeric()):
        vegErtek = int(data)
        if (kezdoErtek >= vegErtek):
            print("Ne legyen nagyobb a kezdőérték a végértéknél!")
    else:
        print("Nem számot adott meg!")

for i in range(vegErtek, kezdoErtek-1, -1):
    print(i)
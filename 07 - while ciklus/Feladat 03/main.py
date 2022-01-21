# 1. rnd generálása
# 2. tippek bekérése -> while:
#    while (tipp != rnd and tippekSzama <= 5):

import random

tipp: int = 0
rnd: int = 0
tippekSzama: int = 1
temp: str = ""

rnd: int = random.randint(0, 9)

while (tipp != rnd and tippekSzama <= 5):

    temp = ""  # a temp-et nullára állítja

    while (temp == "" or temp.isspace() or  not temp.isnumeric):
        temp = input(f"Kérem az {tippekSzama}, tippet:")
        if (temp.isnumeric()):
            tipp = int(temp)
            tippekSzama += 1
        else:
            print("Nem számot adott meg tippnek.")

if (tipp == rnd):
    print(f"Gratulálunk, eltalálta a számot: {rnd}")
else:
    print(f"Sajnos nem találta el a számot! A jó szám: {rnd}")
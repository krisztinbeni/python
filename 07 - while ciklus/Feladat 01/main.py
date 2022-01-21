import os
import time

number: int = None
data: str = ""

while(number == None or number < 0 or number > 9):
    data = input("Kérem a számot 1 és 9 között: ")
    if (data.replace("-", "").isnumeric()):
        number = int(data)
        if( number != None and (number < 0 or number > 9) ):
            print("\n Nem megfelelő a szám (nincs 0 és 9 közt)!")
            time.sleep(3)
            os.system("cls")
    else:
        print("\n Nem számot adott meg!")
        time.sleep(3)
        os.system("cls")

print(f"A beolvasott szam: {number}")
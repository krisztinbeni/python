harommalOszthatoSzamok: int=0

print("Kezdőérték:")
kezdoErtek: int=int(input())

print("Végérték:")
vegErtek: int=int(input())

for i in range(kezdoErtek, vegErtek+1, 1):
    if (i % 3 == 0):
        harommalOszthatoSzamok += 1

print(f"{harommalOszthatoSzamok} db szám osztahó hárommal.")
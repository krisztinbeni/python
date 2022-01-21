osszeg: int=0
szamokSzama: int=0
atlag: float=0

print("Kezdőérték:")
kezdoErtek: int=int(input())

print("Végérték:")
vegErtek: int=int(input())

for i in range(kezdoErtek, vegErtek+1, 1):
        szamokSzama += 1
        osszeg += i

atlag = osszeg / szamokSzama

print(f"{atlag}")
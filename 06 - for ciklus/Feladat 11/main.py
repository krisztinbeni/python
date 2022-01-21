parosSzamokOsszege: int=0
paratlanSzamokSzorzat: int=1

print("Kezdőérték:")
kezdoErtek: int=int(input())

print("Végérték:")
vegErtek: int=int(input())

for i in range(kezdoErtek, vegErtek+1, 1):
    if (i % 2 == 0):
        parosSzamokOsszege += i
    else:
        paratlanSzamokSzorzat *= i

print(f"A páros számok összege {parosSzamokOsszege}.")
print(f"A páratlan számok szorzata {paratlanSzamokSzorzat}.")
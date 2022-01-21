parosSzamokOsszege: int=0
paratlanSzamokOsszege: int=0

print("Kezdőérték:")
kezdoErtek: int=int(input())

print("Végérték:")
vegErtek: int=int(input())

for i in range(kezdoErtek, vegErtek+1, 1):
    if (i % 2 == 0):
        parosSzamokOsszege += i  
    else:
        paratlanSzamokOsszege += i

if (parosSzamokOsszege > paratlanSzamokOsszege):
    print(f"A páros számok összege a nyagyobb.")
elif (paratlanSzamokOsszege > parosSzamokOsszege):
    print(f"A páratlan számok összege a nyagyobb.")  
else:
    print(f"A páros és a páratlan számok összege egyenlő.")
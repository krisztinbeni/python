parosSzamokOsszege: int=0
paratlanSzamokOsszege: int=0
atlag: float=0

print("Kezdőérték:")
kezdoErtek: int=int(input())

print("Végérték:")
vegErtek: int=int(input())

for i in range(kezdoErtek, vegErtek+1, 1):
    if (i % 2 == 0):
        parosSzamokOsszege += i  
    else:
        paratlanSzamokOsszege += i

atlag = (paratlanSzamokOsszege + parosSzamokOsszege) / 

print(f"{atlag}")